package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.CheckBox;
import android.widget.Toast;

public class MainActivity extends Activity
{
	private CheckBox box1, box2;

	@Override
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		box1 = (CheckBox) this.findViewById(R.id.url1);
		box2 = (CheckBox) this.findViewById(R.id.url1);

		// box1.setChecked(true);
		// box1.setText("www.cnblogs.com");

		box1.setOnClickListener(new MyOnclickListener());
		box2.setOnClickListener(new MyOnclickListener());
	}

	class MyOnclickListener implements OnClickListener
	{

		public void onClick(View v)
		{
			CheckBox checkBox = (CheckBox) v;
			String msgString = checkBox.getText().toString();

			Log.i("main",msgString);
			
			if (checkBox.isChecked())
			{
				Toast.makeText(MainActivity.this, msgString, Toast.LENGTH_SHORT).show();
			}

		}
	}

}