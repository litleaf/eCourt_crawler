#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json
import yaml

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def search_report(identifier):
    url = u'http://www.lawplus.com.tw/rest/search/report/%s' % identifier
    content = requests.get(url).content
    json_dict = json.loads(content)
    return json_dict

if __name__ == '__main__':
    # ./lp-search-report.py TPS,99,台上,8096-af2372e4-b2f2-4c67-b1ab-9865f94afa4d
    identifier = sys.argv[1]
    result = search_report(identifier)
    with open(u'%s.search_report.yaml' % identifier, 'w') as f:
        f.write(yaml.safe_dump(result, allow_unicode=True))
