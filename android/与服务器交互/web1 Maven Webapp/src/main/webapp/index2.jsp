<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">    
    <title>信平的小屋</title>
    
  </head>
  
  <body>   
	<h2>Hello World!</h2>
	<h2>信平的小屋 </h2>

  </body>
</html>
