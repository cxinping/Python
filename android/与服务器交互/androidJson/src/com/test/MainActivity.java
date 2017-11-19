package com.test;

import com.test.service.LoginService;
import com.test.tools.HttpUtils;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends Activity {
  
	private Button subBtn = null;
	private Button clearBtn = null;
	private EditText userEdit  = null;
	private EditText pwdEdit  = null;
	private LoginService loginService;
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        subBtn = (Button) super.findViewById(R.id.subBtn);
        clearBtn = (Button) super.findViewById(R.id.clearBtn);
        userEdit =  (EditText) super.findViewById(R.id.userEdit);
        pwdEdit =  (EditText) super.findViewById(R.id.pwdEdit);
        loginService = new LoginService();
        
        subBtn.setOnClickListener(new OnClickListener()
		{
			public void onClick(View v)
			{
				int viewId = v.getId();
				Log.i("main", "viewId="+viewId);
				
				String username = userEdit.getText().toString();
				String pwd = pwdEdit.getText().toString();
				
				Log.i("main", "username="+username);
				Log.i("main", "pwd="+pwd);
				
//				userEdit.setText("aaa");
//				pwdEdit.setText("123");
				
				loginService.login2Server(username, pwd);
				
			}
		});
        
        clearBtn.setOnClickListener(new OnClickListener()
		{
			public void onClick(View v)
			{
				userEdit.setText("");
				pwdEdit.setText("");
				
			}
		});
        
    }
    
    
}