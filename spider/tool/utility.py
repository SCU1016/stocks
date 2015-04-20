__author__ = 'joeyzhao'
# -*-coding:utf-8-*-

import urllib
import sqlite3
import datetime


class MarketDataFromDCE:
    def __init__(self, date, SaveUrl):
        self.date = date[0:4] + date[5:7] + date[-2:]  #"2014/05/23"
        self.url = r"http://www.dce.com.cn/PublicWeb/MainServlet"
        self.PostDic = {'action': 'Pu00011_result', 'Pu00011_Input.trade_date': self.date,
                        'Pu00011_Input.trade_type': '0', 'Pu00011_Input.variety': 'all',
                        'Submit': u'查 询'}

        self.Rename = {'大豆': 'a', '豆二': 'b', '豆粕': 'm', '豆一': 'a', '豆油': 'y', '鸡蛋': 'jd', \
                       '焦煤': 'jm', '焦炭': 'j', '玉米': 'c', '胶合板': 'bb', '聚丙烯': 'pp', '聚乙烯': 'l', '铁矿石': 'i', '纤维板': 'fb',
                       '棕榈油': 'p', '聚氯乙烯': 'v'}
        self.SaveUrl = SaveUrl
        self.Data = {}

    def GetWebPage(self):
        PostDicDecoded = urllib.parse.urlencode(self.PostDic).encode(encoding='gbk')
        Request = urllib.request.Request(self.url, PostDicDecoded)
        MyPage = urllib.request.urlopen(Request).read().decode("gbk", "ignore")
        if not MyPage:
            print("Dear Host,I can not find the web page")
        return MyPage

    def GetTheTradingDay(self):
        TradingDay = datetime.datetime(int(self.date[0:4]), int(self.date[4:6]), int(self.date[-2:]))
        return TradingDay

    def GetNeededData(self):
        MyPage = self.GetWebPage()
        TradingDay = self.GetTheTradingDay()
        #print(Contents)


    def InsertDataToDB(self):
        self.GetNeededData()
        conna = sqlite3.connect(self.SaveUrl)
        #if conna:
        #    print("database is successfully connected")
        cursor = conna.cursor()
        SQLquery1 = "create table if not exists DCE(Contracts varchar(20),date datetime,Symbol nvarchar(30),Open numeric(15,2),\
                  High numeric(15,2),Low numeric(15,2),Close numeric(15,2),PreSettlement numeric(15,2),Settlement numeric(15,2),\
                  Change1 numeric(15,2),Change2 numeric(15,2),Volume numeric(25,2),OpenInt numeric(25,2),\
                  ChangeofOpenInt numeric(25,2),Turnover numeric(30,2))"
        cursor.execute(SQLquery1)
        for key, value in self.Data.items():
            Iter = (
            key, value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9],
            value[10], value[11], value[12], value[13])
            #print(Iter)
            SQLquery2 = "insert into DCE" + " " + "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            cursor.execute(SQLquery2, Iter)
        conna.commit()
        conna.close()


if __name__ == "__main__":
    try:
        test = MarketDataFromDCE("2014/10/15")
        test.InsertDataToDB()
    except Exception as e:
        print("something wrong")
        print(e)