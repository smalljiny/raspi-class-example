package kr.ac.sunmoon.raspi.view.main;

import android.content.Context;
import android.content.SharedPreferences;
import android.support.annotation.NonNull;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.schedulers.Schedulers;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;
import kr.ac.sunmoon.raspi.common.mvp.BasePresenter;
import kr.ac.sunmoon.raspi.model.RoomSummary;
import kr.ac.sunmoon.raspi.net.RaspiResponse;
import kr.ac.sunmoon.raspi.net.RestApi;
import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainPresenter extends BasePresenter<MainView> {
  @NonNull
  private Context context;
  @NonNull
  private RestApi api;

  private CompositeDisposable disposables;

  public MainPresenter(@NonNull Context context) {
    this.context = context;
    disposables = new CompositeDisposable();
    api = initRestApi();
  }

  @NonNull
  private RestApi initRestApi() {
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
        .baseUrl("http://192.168.25.61:5000")
        .client(client)
        .addConverterFactory(GsonConverterFactory.create(gson))
        .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
        .build();

    return retrofit.create(RestApi.class);
  }

  private <T> T getBody(RaspiResponse<T> response) {
    if (response.getCode() != 0) {
      throw new IllegalStateException(response.getDebug());
    }
    return response.getBody();
  }

  public void loadRoomList() {
    SharedPreferences sharedPref = context.getSharedPreferences("PREF_RASPI", Context.MODE_PRIVATE);
    String token = sharedPref.getString("KEY_SESSION_TOKEN", "");
    disposables.add(
        api.getRoomList(token)
            .map(this::getBody)
            .observeOn(AndroidSchedulers.mainThread())
            .subscribeOn(Schedulers.io())
            .subscribe(
                this::onLoaded,
                this::onError
            )
    );
  }

  private void onLoaded(ArrayList<RoomSummary> rooms) {
    getMvpView().updateRoomList(rooms);
  }

  private void onError(Throwable throwable) {

  }
}
