package kr.ac.sunmoon.ledcontroller.common.mvp;

public interface Presenter<V extends MvpView> {

  void attachView(V mvpView);

  void detachView();
}
