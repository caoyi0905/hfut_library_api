#coding:utf-8
import json,requests,re
from bs4 import BeautifulSoup

url='http://210.45.242.5:8080/opac/openlink.php';
strSearchTypeList=['title','author','keyword','callno','publisher','series','tpinyin','apinyin'];
val={'strSearchType':strSearchTypeList[0],'match_flag':'forward','historyCount':'1','doctype':'ALL',
     'showmode':'list','sort':'CATA_DATE','orderby':'desc','dept':'ALL'};

def main(strText,displaypg,page):
    val['strText']=strText
    val['page']=page if type(page)!='None' else 1
    val['displaypg']=displaypg if type(displaypg)!='None' else 20
    r=requests.session().get(url,params=val)
    r.encoding='gbk'
    res=r.content
    soup=BeautifulSoup(res,"lxml");
    tag=re.compile('</?\w+[^>]*>')
    tot=[]
    lists=soup.findAll('li',{'class':'book_list_info'});
    for i in lists:
        tt=re.sub(tag,' ',str(i.findAll('h3')[0])).split(' ');
        while '' in tt:
            tt.remove('');
        bookType=tt[0];
        bookName=re.sub(tag,' ',str(i.findAll('a')[0])).strip();
        bookTP=tt[-1];

        getmarc=BeautifulSoup(str(i),"lxml");
        marc=str(getmarc.find('a')['href'][17:]);

        ttt=re.sub(tag,' ',str(i.findAll('p')[0])).split('  ');
        while '' in ttt:
            ttt.remove('');
        totnum=ttt[0].strip();
        avalnum=ttt[2].strip();
        author=ttt[3].strip();
        press=ttt[5].strip();
        x={"bookType":bookType,"bookName":bookName,"bookTP":bookTP,"bookmarc":marc,"totnum":totnum,"avalnum":avalnum,"author":author,"press":press};
        tot.append(x)
    data=json.dumps(tot,ensure_ascii=False)
    return data