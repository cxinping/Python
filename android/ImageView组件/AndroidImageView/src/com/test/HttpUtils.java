package com.test;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpUtils
{
	private final static String URL_PATH = "http://42.185.61.153:8020/web1/deskclock.png";// 访问网路图片的路径

	public HttpUtils() {
	}

	/**
	 * 从网络中获取图片信息，以流的形式返回
	 * 
	 * @return
	 */
	public static InputStream getImageViewInputStream() throws IOException {
		InputStream inputStream = null;

		URL url = new URL(URL_PATH);
		if (url != null) {
			HttpURLConnection httpURLConnection = (HttpURLConnection) url
					.openConnection();
			httpURLConnection.setConnectTimeout(3000);// 设置连接超时的时间
			httpURLConnection.setRequestMethod("GET");
			httpURLConnection.setDoInput(true);
			
			int response_code = httpURLConnection.getResponseCode();
			if (response_code == 200) {
				inputStream = httpURLConnection.getInputStream();
			}
		}
		return inputStream;
	}

}
