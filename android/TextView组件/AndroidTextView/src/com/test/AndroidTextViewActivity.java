package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class AndroidTextViewActivity extends Activity
{
	TextView text = null;

	@Override
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		text = (TextView) super.findViewById(R.id.test1);

		Button button = (Button) super.findViewById(R.id.btn1);
		button.setOnClickListener(new ClickListener());

	}

	private class ClickListener implements OnClickListener
	{

		public void onClick(View v)
		{
			text.setText("hello herbin");
		}
	}

}