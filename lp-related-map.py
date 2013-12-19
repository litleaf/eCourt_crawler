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
    parser.add_argument('--keyword', default=u'', help='sequence name')
    parser.add_argument('--prevKeyword', default=u'', help='shot name')
    parser.add_argument('--startDate', default=u'', help='asset name')
    parser.add_argument('--endDate', default=u'', help='asset name')
    parser.add_argument('--sortField', default=u'%243%24', help='asset name')
    parser.add_argument('--startMoney', default=u'', help='asset name')
    parser.add_argument('--endMoney', default=u'', help='asset name')
    parser.add_argument('--startSentence', default=u'', help='asset name')
    parser.add_argument('--endSentence', default=u'', help='asset name')
    parser.add_argument('--caseNum', default=u'', help='asset name')
    parser.add_argument('--courts', default=u'', help='asset name')
    parser.add_argument('--rows', default=u'10', help='asset name')
    parser.add_argument('--page', default=u'1', help='asset name')

    args = parser.parse_args()
    return vars(args)

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def related_map(identifier):
    url = u'http://www.lawplus.com.tw/rest/search/report/relatedMap/%s' % identifier
    content = requests.get(url).content
    json_dict = json.loads(content)
    return json_dict

if __name__ == '__main__':
    result = related_map(sys.argv[1])
    for lawsuit in result['response']:
        print lawsuit['identifier']
