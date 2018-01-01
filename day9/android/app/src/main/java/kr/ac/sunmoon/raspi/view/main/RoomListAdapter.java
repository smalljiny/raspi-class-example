package kr.ac.sunmoon.raspi.view.main;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import butterknife.BindView;
import butterknife.ButterKnife;
import java.util.ArrayList;
import kr.ac.sunmoon.raspi.R;
import kr.ac.sunmoon.raspi.model.RoomSummary;

public class RoomListAdapter extends RecyclerView.Adapter<RoomListAdapter.ViewHolder> {

  ArrayList<RoomSummary> roomList;

  @Override
  public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
    View itemView = LayoutInflater.from(parent.getContext())
        .inflate(R.layout.item_room_summary, parent, false);
    return new ViewHolder(itemView);
  }

  @Override
  public void onBindViewHolder(ViewHolder holder, int position) {
    holder.setData(roomList.get(position));
  }

  @Override
  public int getItemCount() {
    return (roomList != null) ? roomList.size() : 0;
  }

  public void setRoomList(final ArrayList<RoomSummary> roomList) {
    this.roomList = roomList;
  }

  public class ViewHolder extends RecyclerView.ViewHolder {

    @BindView(R.id.tv_name)
    TextView tvName;
    @BindView(R.id.tv_ip)
    TextView tvIp;
    @BindView(R.id.btn_boiler)
    Button btnBoiler;
    @BindView(R.id.btn_humidifier)
    Button btnHumidifier;

    private RoomSummary room;

    public ViewHolder(View itemView) {
      super(itemView);

      ButterKnife.bind(this, itemView);
    }

    public void setData(RoomSummary room) {
      this.room = room;
      tvName.setText(room.getName());
      tvIp.setText(room.getIp());
      btnBoiler.setText(String.format("Boiler %s", (room.getBoiler() == 0 ? "OFF" : "ON")));
      btnHumidifier.setText(String.format("Boiler %s", (room.getHumidifier() == 0 ? "OFF" : "ON")));
    }
  }
}
