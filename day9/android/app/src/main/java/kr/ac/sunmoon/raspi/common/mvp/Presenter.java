package kr.ac.sunmoon.raspi.common.mvp;

public interface Presenter<V extends MvpView> {

  void attachView(V mvpView);

  void detachView();
}
