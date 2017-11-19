//
//import java.util.HashMap;
//import java.util.Map;
//import org.apache.commons.httpclient.HttpClient;
//import org.apache.commons.httpclient.methods.DeleteMethod;
//import org.apache.commons.httpclient.methods.GetMethod;
//import org.apache.commons.httpclient.methods.PostMethod;
//import org.apache.commons.httpclient.methods.PutMethod;
//import org.apache.commons.httpclient.methods.StringRequestEntity;
//import org.apache.log4j.Logger;  
//
//public class RestClient
//{
//    static Logger logger = Logger.getLogger(RestClient.class);
//    
//    public static void main(String[] args){
//    	String uri = "http://v.juhe.cn/toutiao/index?type=top&key=2684a869977e50e76d6fab6739415927";
//    	String result = RestClient.doGet(uri, null);
//    	System.out.println(result);
//    	
//    }
//    
//    
//    public static String doGet(String uri , String authToken)
//    {
//        logger.info("--RestClient doGet method start--");
//        String csdpReturn = null;
//        //logger.info("* step1 uri=" + uri   + ",authToken=" + authToken);
//        HttpClient client = new HttpClient();
//        GetMethod method = new GetMethod(uri);
//        method.setRequestHeader("Content-Type", "applic ation/json; charset=UTF-8");
//        method.setRequestHeader("authToken", authToken);
//        try
//        {
//            client.executeMethod(method);
//            csdpReturn = method.getResponseBodyAsString();
//            logger.info("-- RestClient doGet method result from csdp string csdpReturn=\n" + csdpReturn);
//            method.releaseConnection();
//        } catch (Exception e)
//        {
//            e.printStackTrace();
//            throw new RuntimeException("csdp返回参数有误",e);
//        } 
//        logger.info("--RestClient doGet method end--");
//        return csdpReturn;
//    }
//    
//    public static String doPost(String uri, String jsonObj, String authToken)
//    {
//        logger.info("--RestClient doPost method start--");
//        // logger.info("doPost method params: uri=" + uri + ",jsonObj=" +
//        // jsonObj + ",authToken=" + authToken + ",hostUrl=" +hostUrl);
//        String csdpReturn = null;
//        logger.info("* step1 uri=" + uri + ",jsonObj=" + jsonObj + ",authToken=" + authToken);
//        HttpClient client = new HttpClient();
//        PostMethod method = new PostMethod(uri);
//        method.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
//        method.setRequestHeader("authToken", authToken);
//        method.setRequestEntity(new StringRequestEntity(jsonObj));
//        try
//        {
//            client.executeMethod(method);
//            csdpReturn = method.getResponseBodyAsString();
//            logger.info("doPost method result from csdp string csdpReturn=" + csdpReturn);
//            method.releaseConnection();
//        } catch ( Exception e)
//        {
//            e.printStackTrace();
//            throw new RuntimeException("csdp返回参数有误",e);
//        }
//        logger.info("--RestClient doPost method end--");
//        return csdpReturn;
//    }
//    
//    /**
//     * HttpClient PUT请求访问授权
//     * 
//     * @return 返回Map<String, Object>数据
//     */
//    public static String doPut(String uri, String jsonObj, String authToken)
//    {
//        logger.info("--RestClient doPut method start--");
//        logger.info("doPut method params: uri=" + uri + ",jsonObj=" + jsonObj + ",authToken=" + authToken  );
//        Map<String, Object> retResult = new HashMap<String, Object>();
//        HttpClient client = new HttpClient();
//        PutMethod method = new PutMethod(uri);
//        String csdpReturn = null;
//        method.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
//        method.setRequestHeader("authToken", authToken);
//        method.setRequestEntity(new StringRequestEntity(jsonObj));
//        try
//        {
//            client.executeMethod(method);
//            csdpReturn = method.getResponseBodyAsString();
//            logger.info("doPost method result from csdp string csdpReturn=" + csdpReturn);
//            method.releaseConnection();
//        } catch ( Exception e)
//        {
//            e.printStackTrace();
//            throw new RuntimeException("csdp返回参数有误",e);
//        } 
//        logger.info("--RestClient doPut method end--");
//        return csdpReturn;
//    }
//    
//      /**
//         * HttpClient DELETE请求访问授权
//         * 
//         * @return 返回Map<String, Object>数据
//         */
//        public static String doDelete(String uri , String authToken)
//        {
//            logger.info("--RestClient doDelete method start--");
//            logger.info("doDelete method params: uri=" + uri +   ",authToken=" + authToken  );
//            //Map<String, Object> retResult = new HashMap<String, Object>();
//            HttpClient client = new HttpClient();
//            DeleteMethod method = new DeleteMethod(uri);
//            String csdpReturn = null;
//            method.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
//            method.setRequestHeader("authToken", authToken);
//            try
//            {
//                client.executeMethod(method);
//                csdpReturn = method.getResponseBodyAsString();
//                logger.info("doDelete method result from csdp string csdpReturn=" + csdpReturn);
//                method.releaseConnection();
//            } catch ( Exception e)
//            {
//                e.printStackTrace();
//                throw new RuntimeException("csdp返回参数有误",e);
//            } 
//            logger.info("--RestClient doDelete method end--");
//            return csdpReturn;
//        }
//        
//    
//    
//
//}