package kr.ac.sunmoon.raspi.net;

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
public class LoginRequest {
  @Expose
  private String email;
  @Expose
  private String password;
}
