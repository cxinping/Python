import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

public class Test1 {

	public static void main(String[] args) {

	  List list = new ArrayList();
	  list.add(1);
	  list.add(2);
	  list.add(3);
		
	  String  jsonArr =  (String) JSON.toJSONString(list);
	  System.out.println(jsonArr);
	  
	  
		
	}

}
