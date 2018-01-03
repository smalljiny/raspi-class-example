package kr.ac.sunmoon.ledcontroller;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;
import butterknife.BindView;
import butterknife.ButterKnife;

public class MainActivity extends AppCompatActivity implements LedView {
  @BindView(R.id.img_led_0)
  ImageView imgLed0;
  @BindView(R.id.img_led_1)
  ImageView imgLed1;
  @BindView(R.id.btn_led0)
  Button btnLed0;
  @BindView(R.id.btn_led1)
  Button btnLed1;
  @BindView(R.id.btn_close)
  Button btnClose;
  @BindView(R.id.progress)
  ProgressBar progressBar;

  private LedPresenter presenter;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    ButterKnife.bind(this);

    initView();

    presenter = new LedPresenter();
    presenter.attachView(this);
  }

  @Override
  protected void onDestroy() {
    presenter.detachView();
    super.onDestroy();
  }

  private void initView() {
    btnClose.setOnClickListener(new OnClickListener() {
      @Override
      public void onClick(View view) {
        finish();
      }
    });

    btnLed0.setOnClickListener(new OnClickListener() {
      @Override
      public void onClick(View view) {
        presenter.toggleLedStatus(0);
      }
    });

    btnLed1.setOnClickListener(new OnClickListener() {
      @Override
      public void onClick(View view) {
        presenter.toggleLedStatus(1);
      }
    });
  }

  @Override
  public void updateStatus(boolean led0, boolean led1) {
    if (led0) {
      imgLed0.setImageResource(R.drawable.led_on);
    } else {
      imgLed0.setImageResource(R.drawable.led_off);
    }

    if (led1) {
      imgLed1.setImageResource(R.drawable.led_on);
    } else {
      imgLed1.setImageResource(R.drawable.led_off);
    }
  }

  @Override
  public void showError(String message) {
    Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
  }

  @Override
  public void showLoading() {
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE,
        WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE);
    progressBar.setVisibility(View.VISIBLE);
  }

  @Override
  public void hideLoading() {
    getWindow().clearFlags(WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE);
    progressBar.setVisibility(View.INVISIBLE);
  }
}
