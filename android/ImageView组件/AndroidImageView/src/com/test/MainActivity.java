package com.test;

import java.io.IOException;
import java.io.InputStream;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends Activity
{
	private Button button;
	private ImageView imageView;

	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		button = (Button) this.findViewById(R.id.button);
		imageView = (ImageView) this.findViewById(R.id.imageview);
		button.setOnClickListener(new View.OnClickListener()
		{

			public void onClick(View v)
			{
				Log.i("main", "---- hello ----");

				try
				{
					InputStream inputStream = HttpUtils.getImageViewInputStream();
					// Î»Í¼ÎÄ¼þ
					Bitmap bitmap = BitmapFactory.decodeStream(inputStream);
					imageView.setImageBitmap(bitmap);
				} catch (IOException e)
				{
					e.printStackTrace();
				}

			}
		});

	}
}