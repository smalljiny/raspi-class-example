package kr.ac.sunmoon.raspi.view.login;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import butterknife.BindView;
import butterknife.ButterKnife;
import kr.ac.sunmoon.raspi.R;
import kr.ac.sunmoon.raspi.view.main.MainActivity;

public class LoginActivity extends AppCompatActivity implements LoginView {

  @BindView(R.id.toolbar)
  Toolbar toolbar;
  @BindView(R.id.edit_email)
  EditText editEmail;
  @BindView(R.id.edit_password)
  EditText editPassword;
  @BindView(R.id.btn_login)
  Button btnLogin;

  private LoginPresenter presenter;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_login);

    ButterKnife.bind(this);

    presenter = new LoginPresenter(getBaseContext());
    presenter.attachView(this);

    setSupportActionBar(toolbar);

    btnLogin.setOnClickListener(new OnClickListener() {
      @Override
      public void onClick(View view) {
        presenter.attemptLogin(editEmail.getText().toString(),
            editPassword.getText().toString());
      }
    });
  }

  @Override
  protected void onDestroy() {
    presenter.detachView();
    super.onDestroy();
  }

  @Override
  public void showMainUi() {
    Intent intent = new Intent(this, MainActivity.class);
    startActivity(intent);
    finish();
  }

  @Override
  public void showError(String msg) {
    Toast.makeText(this, msg, Toast.LENGTH_SHORT).show();
  }
}
