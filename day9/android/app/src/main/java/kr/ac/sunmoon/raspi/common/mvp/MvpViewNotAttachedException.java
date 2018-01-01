package kr.ac.sunmoon.raspi.common.mvp;

public class MvpViewNotAttachedException extends RuntimeException {
  public MvpViewNotAttachedException() {
    super("Please call Presenter.attachView(MvpView) before requesting data to the Presenter");
  }
}
