package com.test.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.test.tools.HttpUtils;

import android.util.Log;

public class LoginService
{

	public void login2Server(String name, String pwd){
		String path = "http://42.185.61.153:8020/web1/ok.html";
		String jsonStr = HttpUtils.getJsonContent(path);
		
		Log.i("main", jsonStr);
		JSONObject jsonObject = JSON.parseObject(jsonStr);
		
		
		
	}
	
}
