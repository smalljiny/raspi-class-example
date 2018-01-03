package kr.ac.sunmoon.ledcontroller.net;

import android.support.annotation.IntRange;
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
public class LedRequest {
  @Expose
  @IntRange(from = 0, to = 1)
  private int status;
}
