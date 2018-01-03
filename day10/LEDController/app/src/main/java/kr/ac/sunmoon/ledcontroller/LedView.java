package kr.ac.sunmoon.ledcontroller;

import kr.ac.sunmoon.ledcontroller.common.mvp.MvpView;

public interface LedView extends MvpView {

  void updateStatus(boolean led0, boolean led1);

  void showError(String message);

  void showLoading();

  void hideLoading();
}
