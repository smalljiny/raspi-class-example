package kr.ac.sunmoon.ledcontroller.net;

import kr.ac.sunmoon.ledcontroller.model.LedStatus;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.PUT;
import retrofit2.http.Path;

public interface LedApi {
  @GET("leds")
  Call<LedResponse<LedStatus>> getStatus();

  @PUT("leds/{id}")
  Call<LedResponse<LedStatus>> setStatus(@Path("id") long id, @Body LedRequest body);
}
