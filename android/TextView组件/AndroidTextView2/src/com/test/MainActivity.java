package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.util.Log;
import android.widget.TextView;

public class MainActivity extends Activity {
    private TextView textView1, textView2;
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        textView1 = (TextView) this.findViewById(R.id.textview1);
        textView2 = (TextView) this.findViewById(R.id.textview2);
        
        //添加一段html标志
        String html = "<font color='red'>我热爱学习 </font>";
        html = html + "<a href='www.baidu.om'>百度</a>";

        CharSequence charSequence =  Html.fromHtml(html);
        textView1.setText(charSequence);
        textView1.setMovementMethod(LinkMovementMethod.getInstance());
        
        String text = "网址: www.baidu.com\n";
        text+= "邮箱: xpws2006@163.com\n";
        text += "电话: 13512311212";
        Log.i("main", text);
        
        textView2.setText(text);
        textView2.setMovementMethod(LinkMovementMethod.getInstance());

    }
}