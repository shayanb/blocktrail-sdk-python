__author__ = 'sbeta'

from time import mktime
from wsgiref.handlers import format_date_time
from datetime import datetime
import hmac
import hashlib
import base64

def Signer(key_id = 'BLOCKTRAIL_API_KEY', secret = 'BLOCKTRAIL_API_SECRET', algorithm="hmac-sha256", payload={}, headers= {}):

    def Signer(data, secret = secret):
        signature = hmac.new(secret, data, hashlib.sha256).digest()
        return base64.b64encode(signature)

    def HeaderSign(headers):
        headers["keyId"] = key_id
        headers["algorithm"] = algorithm
        if 'Date' not in headers:
            now = datetime.now()
            stamp = mktime(now.timetuple())
            headers['Date'] = format_date_time(stamp)
        if headers:
            signable_list = [headers[x] for x in headers]
            signable = '\n'.join(signable_list)
        else:
            signable = headers['Date']

        signature = Signer(signable)
        #headers["Authorization"] =
        headers['signature'] = signature
        return headers

    headers = HeaderSign(headers)
    return headers
