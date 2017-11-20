package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.widget.RatingBar;
import android.widget.RatingBar.OnRatingBarChangeListener;
import android.widget.Toast;

public class RatingBarActivity extends Activity implements OnRatingBarChangeListener
{
	private RatingBar ratingBar;

	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		ratingBar = (RatingBar) this.findViewById(R.id.ratingBar);
		ratingBar.setMax(100);// 设置最大刻度
		ratingBar.setProgress(20);// 设置当前的刻度
		ratingBar.setOnRatingBarChangeListener(this);

	}

	public void onRatingChanged(RatingBar ratingBar, float rating, boolean fromUser)
	{
		int progress = ratingBar.getProgress();
		Toast.makeText(RatingBarActivity.this, "progress:" + progress + "rating:" + rating, 1).show();

	}

}