package com.json.action;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.alibaba.fastjson.JSON;
import com.json.service.LoginService;

public class LoginAction extends HttpServlet {

	private LoginService loginService;

	
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		String username = request.getParameter("username");
		String password = request.getParameter("password");
		
		System.out.println("=== LoginAction doPost ===");
		System.out.println("username=" + username );
		System.out.println("password=" + password );
		
		boolean flag = loginService.login(username, password);
		Map result = new HashMap();
		result.put("flag", flag);
		if(flag ){
			result.put("timestamp", System.currentTimeMillis() );
		}else{
			result.put("desc", "登录失败，用户名或密码错误。");
		}
		
		String json = JSON.toJSONString(result);
		System.out.println("json=" + json );
		
		response.setContentType("text/html;charset=utf-8");
		request.setCharacterEncoding("utf-8");
		response.setCharacterEncoding("utf-8");
		PrintWriter out = response.getWriter();	
		out.println(json);
		out.flush();
		out.close();
	}

	
	public void init() throws ServletException {
		loginService = new LoginService();
	}

}
