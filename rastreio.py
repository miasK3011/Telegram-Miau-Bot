import requests
from requests.structures import CaseInsensitiveDict
import json

def  rastreio(orderNo, lssId):
    url = "https://plusla.samsungscl.com/cello/tms/integration/json/TMS_PEXT_EX_0029"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    content = '{"shprOrderNo":"%s","lssId":"%s"}' % (orderNo, lssId)
    response = requests.post(url, headers=headers, data=content)
    response = json.loads(response.text)
    
    return response
