#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def search_report_relatedMap(identifier):
    url = u'http://www.lawplus.com.tw/rest/search/report/relatedMap/%s' % identifier
    content = requests.get(url).content
    json_dict = json.loads(content)
    return json_dict

if __name__ == '__main__':
    # ./lp-search-report-relatedMap.py TPS,99,台上,8096-af2372e4-b2f2-4c67-b1ab-9865f94afa4d
    # ./lp-search-report-relatedMap.py TPH,100,重上,369-5f1a7a91-b5b4-4926-95b3-1c090775fcb5
    result = search_report_relatedMap(sys.argv[1])
    for lawsuit in result['response']:
        print lawsuit['identifier']
