package kr.ac.sunmoon.raspi.net;

import io.reactivex.Single;
import java.util.ArrayList;
import kr.ac.sunmoon.raspi.model.RoomSummary;
import kr.ac.sunmoon.raspi.model.Session;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.POST;

public interface RestApi {

  @POST("sessions")
  Single<RaspiResponse<Session>> login(@Body LoginRequest request);

  @GET("rooms")
  Single<RaspiResponse<ArrayList<RoomSummary>>> getRoomList(@Header("Authorization") String authorization);
}
