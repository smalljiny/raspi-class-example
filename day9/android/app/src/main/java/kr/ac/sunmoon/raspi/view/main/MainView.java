package kr.ac.sunmoon.raspi.view.main;

import java.util.ArrayList;
import kr.ac.sunmoon.raspi.common.mvp.MvpView;
import kr.ac.sunmoon.raspi.model.RoomSummary;

public interface MainView extends MvpView {
  void updateRoomList(ArrayList<RoomSummary> rooms);
}
