package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;

public class MainActivity extends Activity
{
	private TextView textView1;

	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		textView1 = (TextView) this.findViewById(R.id.textview1);
		SeekBar seekBar1 = (SeekBar) this.findViewById(R.id.seekbar1);
		seekBar1.setOnSeekBarChangeListener(new MyOnSeekBarChangeListener());

	}

	class MyOnSeekBarChangeListener implements OnSeekBarChangeListener
	{

		// 当滑动滑竿的时候会触发的事件
		public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser)
		{
			textView1.setText("seekbar1的当前位置是：" + progress);
		}

		// 表示从哪里开始拖动
		public void onStartTrackingTouch(SeekBar seekBar)
		{
			textView1.setText("seekbar2开始拖动  " + seekBar.getProgress());
		}

		// 表示从哪里结束拖动
		public void onStopTrackingTouch(SeekBar seekBar)
		{
			textView1.setText("seekbar1停止拖动  " + seekBar.getProgress());

		}

	}
}