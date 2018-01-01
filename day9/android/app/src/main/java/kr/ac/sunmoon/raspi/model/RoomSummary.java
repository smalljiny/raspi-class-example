package kr.ac.sunmoon.raspi.model;

import com.google.gson.annotations.Expose;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class RoomSummary {
  @Expose
  private long id;
  @Expose
  private String name;
  @Expose
  private String ip;
  @Expose
  private int boiler;
  @Expose
  private int humidifier;
}
