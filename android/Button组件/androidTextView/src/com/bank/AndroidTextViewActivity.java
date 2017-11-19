package com.bank;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class AndroidTextViewActivity extends Activity {
   private TextView text ;
   private Button btn1,btn2, btn3;	
	
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        text = (TextView) super.findViewById(R.id.text);
        btn1 =  (Button) super.findViewById(R.id.btn1);
        btn2 =  (Button) super.findViewById(R.id.btn2);
        btn3 =  (Button) super.findViewById(R.id.btn3);
        
        btn1.setOnClickListener(new MyOnclickListener() );
        btn2.setOnClickListener(new MyOnclickListener() );
        btn3.setOnClickListener(new MyOnclickListener() );
        
    }
    
    class MyOnclickListener implements OnClickListener{

		public void onClick(View v)
		{
		   if(v.getId() ==  R.id.btn1 ){
				Log.i("main","btn1 id=> "+ v.getId()+"");
				text.setText("button1 clicked");
		   }else  if(v.getId() ==  R.id.btn2 ){
				Log.i("main","btn2 id=> "+ v.getId()+"");
				text.setText("button2 clicked");
		   }else  if(v.getId() ==  R.id.btn3 ){
				Log.i("main","btn3 id=> "+ v.getId()+"");
				text.setText("button3 clicked");
		   }
			
		}
    	
    }
    
}