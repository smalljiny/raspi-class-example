package kr.ac.sunmoon.ledcontroller.model;

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
public class LedStatus {

  @Expose
  private int led0;
  @Expose
  private int led1;
}
