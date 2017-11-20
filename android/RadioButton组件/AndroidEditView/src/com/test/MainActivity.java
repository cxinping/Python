package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class MainActivity extends Activity
{
	private RadioGroup group;
	private Button button;

	@Override
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		group = (RadioGroup) this.findViewById(R.id.sex);
		button = (Button) this.findViewById(R.id.button);

		button.setOnClickListener(new OnClickListener()
		{

			public void onClick(View v)
			{
				int len = group.getChildCount();// 获得单选按钮组的选项个数
				String msgString = "";
				for (int i = 0; i < len; i++)
				{
					RadioButton radioButton = (RadioButton) group.getChildAt(i);
					if (radioButton.isChecked())
					{
						msgString = radioButton.getText().toString();
						break;
					}
				}

				Toast.makeText(MainActivity.this, msgString, Toast.LENGTH_SHORT).show();
			}

		});

	}
}