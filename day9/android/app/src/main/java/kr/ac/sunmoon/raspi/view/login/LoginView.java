package kr.ac.sunmoon.raspi.view.login;

import kr.ac.sunmoon.raspi.common.mvp.MvpView;

public interface LoginView extends MvpView {

  void showMainUi();

  void showError(String msg);
}
