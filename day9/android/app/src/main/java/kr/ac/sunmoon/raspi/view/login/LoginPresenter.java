package kr.ac.sunmoon.raspi.view.login;


import android.content.Context;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.support.annotation.NonNull;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.schedulers.Schedulers;
import java.util.concurrent.TimeUnit;
import kr.ac.sunmoon.raspi.common.mvp.BasePresenter;
import kr.ac.sunmoon.raspi.model.Session;
import kr.ac.sunmoon.raspi.net.LoginRequest;
import kr.ac.sunmoon.raspi.net.RaspiResponse;
import kr.ac.sunmoon.raspi.net.RestApi;
import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

public class LoginPresenter extends BasePresenter<LoginView> {

  @NonNull
  private Context context;
  @NonNull
  private RestApi api;

  private CompositeDisposable disposables;

  public LoginPresenter(@NonNull Context context) {
    this.context = context;
    disposables = new CompositeDisposable();
    api = initRestApi();
  }

  @Override
  public void detachView() {
    if (disposables != null && !disposables.isDisposed()) {
      disposables.dispose();
    }
    super.detachView();
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

  public void attemptLogin(String email, String password) {
    if (email == null || email.isEmpty() || password == null || password.isEmpty()) {
      getMvpView().showError("Invalid input!");
    } else {
      LoginRequest request = new LoginRequest(email, password);
      disposables.add(
          api.login(request)
              .map(this::getBody)
              .observeOn(AndroidSchedulers.mainThread())
              .subscribeOn(Schedulers.io())
              .subscribe(
                  this::onSuccessLogin,
                  this::onError
              )
      );
    }
  }

  private <T> T getBody(RaspiResponse<T> response) {
    if (response.getCode() != 0) {
      throw new IllegalStateException(response.getDebug());
    }
    return response.getBody();
  }

  private void onSuccessLogin(Session session) {
    saveSession(session);
    getMvpView().showMainUi();
  }

  private void onError(Throwable throwable) {
    getMvpView().showError(throwable.getLocalizedMessage());
  }

  private void saveSession(@NonNull Session session) {
    SharedPreferences sharedPref = context.getSharedPreferences("PREF_RASPI", Context.MODE_PRIVATE);
    Editor editor = sharedPref.edit();
    editor.putString("KEY_SESSION_TOKEN", session.getToken());
    editor.putLong("KEY_SESSION_UID", session.getUid());
    editor.apply();
  }
}
