package kr.ac.sunmoon.ledcontroller;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.concurrent.TimeUnit;
import kr.ac.sunmoon.ledcontroller.common.mvp.BasePresenter;
import kr.ac.sunmoon.ledcontroller.model.LedStatus;
import kr.ac.sunmoon.ledcontroller.net.LedApi;
import kr.ac.sunmoon.ledcontroller.net.LedRequest;
import kr.ac.sunmoon.ledcontroller.net.LedResponse;
import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class LedPresenter extends BasePresenter<LedView> {
  private boolean led0;
  private boolean led1;

  private LedApi api;
  private Call<LedResponse<LedStatus>> call;

  public LedPresenter() {
    api = initApi();
  }

  @Override
  public void attachView(LedView mvpView) {
    super.attachView(mvpView);

    getMvpView().showLoading();
    call = api.getStatus();

    call.enqueue(new Callback<LedResponse<LedStatus>>() {
      @Override
      public void onResponse(Call<LedResponse<LedStatus>> call,
          Response<LedResponse<LedStatus>> response) {
        getMvpView().hideLoading();
        LedResponse<LedStatus> resp = response.body();
        onLedResponse(resp);
      }

      @Override
      public void onFailure(Call<LedResponse<LedStatus>> call, Throwable t) {
        getMvpView().hideLoading();
        getMvpView().showError(t.getMessage());
      }
    });
  }

  private LedApi initApi() {
    Gson gson = new GsonBuilder()
        .excludeFieldsWithoutExposeAnnotation()
        .create();

    HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
    logging.setLevel(Level.BODY);
    OkHttpClient client = new OkHttpClient.Builder()
        .readTimeout(30, TimeUnit.SECONDS)
        .addInterceptor(logging)
        .build();

    Retrofit retrofit = new Retrofit.Builder()
        .baseUrl("http://192.168.25.61:5002")
        .client(client)
        .addConverterFactory(GsonConverterFactory.create(gson))
        .build();

    return retrofit.create(LedApi.class);
  }

  public void toggleLedStatus(final long led) {
    int status = ((led == 0 && !led0) || (led == 1 && !led1)) ? 1 : 0;
    final LedRequest request = new LedRequest(status);
    call = api.setStatus(led, request);
    getMvpView().showLoading();
    call.enqueue(new Callback<LedResponse<LedStatus>>() {
      @Override
      public void onResponse(Call<LedResponse<LedStatus>> call,
          Response<LedResponse<LedStatus>> response) {
        getMvpView().hideLoading();
        LedResponse<LedStatus> resp = response.body();
        onLedResponse(resp);
      }

      @Override
      public void onFailure(Call<LedResponse<LedStatus>> call, Throwable t) {
        getMvpView().hideLoading();
        getMvpView().showError(t.getMessage());
      }
    });
  }

  private void onLedResponse(LedResponse<LedStatus> resp) {
    if (resp != null) {
      if (resp.getCode() == 0L) {
        LedStatus result = resp.getBody();
        led0 = (result.getLed0() == 1);
        led1 = (result.getLed1() == 1);
        getMvpView().updateStatus(led0, led1);
      } else {
        getMvpView().showError(resp.getDebug());
      }
    }
  }
}