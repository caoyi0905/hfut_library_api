#coding:utf-8
import requests,re,json
from bs4 import BeautifulSoup

url='http://210.45.242.5:8080/opac/item.php';

def main(marc_no):
	val={'marc_no':marc_no};
	r=requests.session().get(url,params=val)
	r.encoding='gbk'
	soup=BeautifulSoup(r.content,"lxml");
	tableStr=soup.find('table',{'id':'item'})
	res=[]
	soup=BeautifulSoup(str(tableStr),"lxml")
	lists=soup.findAll('tr')[1:]
	for l in lists:
		soup=BeautifulSoup(str(l),"lxml")
		tds,jsonRes=soup.find_all('td'),{}
		if len(tds)<5:
			continue
		jsonRes['callno']=tds[0].text.encode('utf-8').strip()
		jsonRes['school']=tds[3].text.encode('utf-8').strip()
		jsonRes['stat']=tds[4].text.encode('utf-8').strip()
		res.append(jsonRes)
	return json.dumps(res,ensure_ascii=False)