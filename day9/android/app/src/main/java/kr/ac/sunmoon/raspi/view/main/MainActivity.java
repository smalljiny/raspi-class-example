package kr.ac.sunmoon.raspi.view.main;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.RecyclerView.LayoutManager;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import butterknife.BindView;
import butterknife.ButterKnife;
import java.util.ArrayList;
import kr.ac.sunmoon.raspi.R;
import kr.ac.sunmoon.raspi.model.RoomSummary;

public class MainActivity extends AppCompatActivity implements MainView {
  @BindView(R.id.toolbar)
  Toolbar toolbar;
  @BindView(R.id.list_rooms)
  RecyclerView listRooms;

  private MainPresenter presenter;
  private RoomListAdapter adapter;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    ButterKnife.bind(this);

    setSupportActionBar(toolbar);

    adapter = new RoomListAdapter();
    LinearLayoutManager layoutManager = new LinearLayoutManager(getBaseContext());
    layoutManager.setOrientation(LinearLayoutManager.VERTICAL);
    listRooms.setLayoutManager(layoutManager);
    listRooms.setAdapter(adapter);

    presenter = new MainPresenter(getBaseContext());
    presenter.attachView(this);
    presenter.loadRoomList();
  }

  @Override
  protected void onDestroy() {
    presenter.detachView();
    super.onDestroy();
  }

  @Override
  public void updateRoomList(ArrayList<RoomSummary> rooms) {
    adapter.setRoomList(rooms);
    adapter.notifyDataSetChanged();
  }
}
