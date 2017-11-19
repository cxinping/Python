package com.json.service;

public class LoginService {

	
	public boolean login(String username, String password){
		boolean flag = false;
		if( username == null || "".equals(username) || password == null  || "".equals(password)  ){
			return false;
		}
		
		if( username.trim().equals("abc")  && password.trim().equals("123"))
		{
			flag = true;
		}
		
		return flag;
	}
	
	public static void main(String[] args){
		LoginService loginService = new LoginService();
		String username = "abc";
		String password = "123";
		boolean flag = loginService.login(username, password);
		System.out.println("flag=" + flag);
		
	}
	
}
