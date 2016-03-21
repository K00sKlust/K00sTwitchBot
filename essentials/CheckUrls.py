from urllib2 import urlopen, URLError
from Settings import WOT_KEY
import time
import json


def wot_request(sites):
    # -----------RATE LIMIT-----------
    global last_request
    try:
        last_request
    except NameError:
        last_request = time.time() - 3.456

    if time.time() - last_request >= 3.456:
        pass
    else:
        wait = 3.456 - (time.time() - last_request)
        print("sleeping for %s seconds" % wait)
        time.sleep(wait)

    # -----------CALL API-----------
    sites = '/'.join(sites)
    request = (" http://api.mywot.com/0.4/public_link_json2?hosts=%s/&callback=process&key="
               % sites + WOT_KEY)
    try:
        result = urlopen(request).read()
        last_request = time.time()
        return json.loads(result[8:-2])
    except URLError, e:
        print("URLError: " + str(e))


def readable_result(sites):
    request_result = wot_request(sites)

    result = []
    for key in request_result:
        result.append("%s's reputation: [%s/100]" % (key, request_result[key]['0'][0]))
    return ', '.join(result)
