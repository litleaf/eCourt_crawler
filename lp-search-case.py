#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json
import argparse

def get_args():
    description = 'Crawler for lawplus'
    usage = "%(prog)s arg [options]"
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument('--querySentence', default=u'', help='project name')
    parser.add_argument('--startDate', default=u'', help='asset name')
    parser.add_argument('--endDate', default=u'', help='asset name')
    parser.add_argument('--sortField', default=u'%243%24', help='asset name')
    parser.add_argument('--startMoney', default=u'', help='asset name')
    parser.add_argument('--endMoney', default=u'', help='asset name')
    parser.add_argument('--startSentence', default=u'', help='asset name')
    parser.add_argument('--endSentence', default=u'', help='asset name')
    parser.add_argument('--caseNum', default=u'', help='asset name')

    args = parser.parse_args()
    return vars(args)

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def search_case(args):
    url = u'http://www.lawplus.com.tw/rest/search/case'
    content = requests.get(url, params=args).content
    json_dict = json.loads(content)
    return json_dict

if __name__ == '__main__':
    # ./lp-search-case.py --querySentence 食品安全
    result = search_case(get_args())
    for k, v in result['response'][0].items():
        print k, v
