package com.test.tools;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpUtils {


	public static String getJsonContent(String url_path) {
		try {
			URL url = new URL(url_path);
			HttpURLConnection connection = (HttpURLConnection) url
					.openConnection();
			connection.setConnectTimeout(3000);
			connection.setRequestMethod("GET");
			connection.setDoInput(true);
			int code = connection.getResponseCode();
			if (code == 200) {
				return changeInputStream(connection.getInputStream());
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return "";
	}

	private static String changeInputStream(InputStream inputStream) {
		String jsonString = "";
		ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
		int len = 0;
		byte[] data = new byte[1024];
		try {
			while ((len = inputStream.read(data)) != -1) {
				outputStream.write(data, 0, len);
			}
			jsonString = new String(outputStream.toByteArray());
		} catch (IOException e) {
			e.printStackTrace();
		}
		return jsonString;
	}
}
