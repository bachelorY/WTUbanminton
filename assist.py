# coding-UTF-8
import requests
import datetime
import time
import calendar
from urllib import parse

# URL
GET_URL="http://m.chaojibiaodan.com/form/1d1u2Nk8"
PSOT_URL="https://m.chaojibiaodan.com/saveFormData.json"

# 头部
HEADERS1 = {
    "Host":"m.chaojibiaodan.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://m.chaojibiaodan.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Connection": "keep-alive",
    "Referer": "https://m.chaojibiaodan.com/form/1d1u2Nk8",
	"Cookie":"area_level=1; area_name=%E5%85%A8%E5%9B%BD;"
}

HEADERS2 = {
    "Host": "m.chaojibiaodan.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en,en-US;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://m.chaojibiaodan.com/form/1d1u2Nk8",
    "Content-Length": "2600",
    "Cookie": "area_level=1; area_name=%E5%85%A8%E5%9B%BD; ",
    "DNT": "1",
    "Connection": "close",
}

PAYLOAD_start = "formVerificationMobile=&formVerificationMobileCode=&device=2&formId=5bf80161b6330f294c164000&customFieldsData="
PAYLOAD_last = "&country=&province=&city=&platform=Win32&os=Windows&browser=firefox&osVersion=10&browserVersion=52&source="
PAYLOAD_JSON = [{#0
	"id": "n6fhbr2s5k1e2sn5q972pzwp0t4blccl",
	"title": "学（工）号",
	"type": "number",
	"value": ""
	}, {#1
	"id": "2jxe0zmpig8vt024ojgyel7369iwdsyy",
	"title": "姓&nbsp;&nbsp;名",
	"type": "input",
	"value": ""
	}, {#2
	"id": "qu0j9h3flvr1veie",
	"title": "手机号码",
	"type": "number",
	"value": ""
	}, {#3
	"id": "bcmfp7vf2kwo67dvwf5nter8cknftxwl",
	"title": "预订日期",
	"type": "time",
	"value": ""
	}, {#4
	"id": "pjgay090mj73uqtl4kuk36zhegteuv8e",
	"title": "预订时段",
	"type": "radio",
	"value": "",
	"code": "",
	"other": ""
	}, {#5
	"id": "vxglipb4ow99sjua7qyk5nlt1ql38kfw",
	"title": "周一至周五时段",
	"type": "select",
	"value": "",
	"code": "",
	"other": ""
	}, {#6
	"id": "11j596qnl98s7id2jqh5no7tyknmed5p",
	"title": "周六、周日时段",
	"type": "select",
	"value": "",
	"code": "",
	"other": ""
	}, {#7
	"id": "68kddm30us3qltwdhlstiadb875i9jpv",
	"title": "预订结果",
	"type": "radio",
	"value": "我已知晓查询方式",
	"code": "",
	"other": ""
	},{#8
	"id":"1jgr7a7q5wc9nyz8",
	"title": "学院",
	"type": "input",
	"value": ""
	}]
BOOKTIME = "19：30--21：30"
class Book():
	def __init__(self,name,id,phone,academy):
		self.name = name
		self.id = id
		self.phone = phone
		self.academy = academy
		self.session = requests.session()

	def get_info(self):
		self.info = {}
		#爪巴取网页
		resp = self.session.get(url=GET_URL,headers=HEADERS1)
		self.headers = HEADERS2
		self.headers["Cookie"] = self.headers["Cookie"] + resp.headers["Set-Cookie"].replace("; Path=/","")
		self.info["weekdayscode"] = "g6ei580l83znpeu5dgcf500kl3udnle0"
		self.info["weekendscode"] = "jgroyeu18cx2xjws5yu0thgrs5n40ec2"
		self.info["weekdaytimecode"] = "3ie0hwvro6mkf1qyp2gjm3vyi9viyn5c"
		self.info["weekendtimecode"] = "fuqx96timxmx0o032c34xwdh8w8y38me"
		self.info["confimecode"] = "0lyamkdtrhotq1bvaq5wszou4c0ob90q"

	def init_payload(self):
		#非星期有关内容初始化
		self.payload_json = PAYLOAD_JSON
		self.payload_json[0]["value"] = self.id
		self.payload_json[1]["value"] = self.name
		self.payload_json[2]["value"] = self.phone
		self.payload_json[8]["value"] = self.academy
		nextday = (datetime.datetime.now()+datetime.timedelta(hours=24)).strftime('%Y-%m-%d')
		# print(nextday)
		self.payload_json[3]["value"] = nextday
		self.payload_json[7]["code"] = self.info["confimecode"]
		#获取当前星期,决定第二天的订场
		year = int(nextday.split('-')[0])
		month = int(nextday.split('-')[1])
		day = int(nextday.split('-')[2])
		week = calendar.weekday(year,month,day)
		#依据星期决定填写内容
		if (week == 5 or week == 6):
			self.payload_json[4]["value"] = "周六、周日时段"
			self.payload_json[4]["code"] = self.info["weekendscode"]
			self.payload_json[6]["value"] = BOOKTIME
			self.payload_json[6]["code"] = self.info["weekendtimecode"]
		else:
			self.payload_json[4]["value"] = "周一--周五时段"
			self.payload_json[4]["code"] = self.info["weekdayscode"]
			self.payload_json[5]["value"] = BOOKTIME
			self.payload_json[5]["code"] = self.info["weekdaytimecode"]
		#封装成json

		jsonstr = str(self.payload_json)
		# print(jsonstr)
		jsonstr = jsonstr.replace(" ", "")
		jsonstr = jsonstr.replace("'", '\\"')
		# print(jsonstr)
		jsonstr = parse.quote(jsonstr)
		# print(jsonstr)
		self.payload = PAYLOAD_start+jsonstr+PAYLOAD_last
		# print(self.payload)

	def send_data(self):
		#发送数据
		resp = self.session.post(url = PSOT_URL,data=self.payload,headers=HEADERS2)
		print(resp.text)
		print(datetime.datetime.now())
		print(resp.status_code)

def main():
    starttime = datetime.datetime.now()
    namelist=[]
    peopleY = {
    	"name":"",
    	"id":"",
    	"phone":"",
		"academy":""
    }
    namelist.append(peopleY)
    fuck = Book(namelist[0]["name"], namelist[0]["id"], namelist[0]["phone"],namelist[0]["academy"])
    fuck.get_info()
    fuck.init_payload()
    fuck.send_data()
    endTime = datetime.datetime.now()
    print(endTime-starttime)
    print(endTime)
    


if __name__ == '__main__':
	# 调整发送时间
    time.sleep(0.7)
    main()













