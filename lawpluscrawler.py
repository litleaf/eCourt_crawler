#coding:utf-8
import sys,os,time
import requests
import json
import urllib
import pprint
import yaml

#url = "http://httpbin.org/user-agent"
#url = "http://www.lawplus.com.tw/rest/search/adv?querySentence=%E9%A3%9F%E5%93%81%E5%AE%89%E5%85%A8&keyword=%E9%A3%9F%E5%93%81%E5%AE%89%E5%85%A8&prevKeyword=%E9%A3%9F%E5%93%81%E5%AE%89%E5%85%A8&startDate=&endDate=&sortField=%243%24&startMoney=0&endMoney=0&startSentence=0&endSentence=0&caseNum=&courts=&rows=10000&page=1"
#url = "http://www.pingluweb.com/rest/search/report/KSH,101,%E5%8B%9E%E4%B8%8A,16-95ae00c2-13a0-4485-b2c8-3070f7756a84"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
}

s = requests.Session()
inputkeyword = "食品安全"
encodedkeyword = urllib.quote(inputkeyword)
#print encodedkeyword

url = "http://www.lawplus.com.tw/rest/search/adv?querySentence=" + encodedkeyword + "&keyword=" + encodedkeyword + "&prevKeyword=" + encodedkeyword + "&startDate=&endDate=&sortField=%243%24&startMoney=0&endMoney=0&startSentence=0&endSentence=0&caseNum=&courts=&rows=10000&page=1"
print "url is :", url

myjson = s.get(url,headers=headers).content
objectjson = json.loads(myjson)
rowslist = objectjson['rows']
#pprint.pprint(objectjson)
for i in range(0,len(rowslist)):
    uniqueid = objectjson['rows'][i]['identifier']
    url2 = "http://www.pingluweb.com/rest/search/report/" + uniqueid
    lp_result = s.get(url2,headers=headers).content
    lp_result_object = json.loads(lp_result)
    if not os.path.isdir("example2"):
        os.makedirs("example2")
    open("example2//"+ uniqueid +".yaml","w").write(yaml.safe_dump(lp_result_object,allow_unicode=True))
    #sys.exit()
