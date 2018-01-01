package kr.ac.sunmoon.raspi.common.mvp;

public class BasePresenter<V extends MvpView> implements Presenter<V> {
  private V mvpView;

  @Override
  public void attachView(V mvpView) {
    this.mvpView = mvpView;
  }

  @Override
  public void detachView() {
    mvpView = null;
  }

  public boolean isViewAttached() {
    return mvpView != null;
  }

  public V getMvpView() {
    checkViewAttached();
    return mvpView;
  }

  public void checkViewAttached() {
    if (!isViewAttached()) throw new MvpViewNotAttachedException();
  }
}
