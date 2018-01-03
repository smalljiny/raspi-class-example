package kr.ac.sunmoon.ledcontroller.net;

import android.support.annotation.Nullable;
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
public class LedResponse<T> {
  @Expose
  private T body;
  @Expose
  private long code;
  @Nullable
  @Expose
  private String debug;
}
