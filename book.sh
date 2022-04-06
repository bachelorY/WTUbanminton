#!/bin/bash

source ~/script/urlencode.sh
source /etc/profile

sid=''
sname=''
phone=''
academy=''

PSOT_URL="https://m.chaojibiaodan.com/saveFormData.json"

PAYLOAD_pre="formVerificationMobile=&formVerificationMobileCode=&device=2&formId=5bf80161b6330f294c164000&customFieldsData="
PAYLOAD_suf='{\"id\":\"68kddm30us3qltwdhlstiadb875i9jpv\",\"title\":\"预订结果\",\"type\":\"radio\",\"value\":\"我已知晓查询方式\",\"code\":\"0lyamkdtrhotq1bvaq5wszou4c0ob90q\",\"other\":\"\"}]&country=&province=&city=&platform=iPhone&os=iOS&browser=weixin&osVersion=14.0.1&browserVersion=7&source='

WEEKDAYCODE="g6ei580l83znpeu5dgcf500kl3udnle0"
WEEKENDSCODE="jgroyeu18cx2xjws5yu0thgrs5n40ec2"
WEEKDAYTIMECODE="3ie0hwvro6mkf1qyp2gjm3vyi9viyn5c"
WEEKENDTIMECODE="fuqx96timxmx0o032c34xwdh8w8y38me"
CONFIMECODE="0lyamkdtrhotq1bvaq5wszou4c0ob90q"

COMMON_suf1='\"},'
COMMON_suf2='\",\"code\":\"'
COMMON_suf3='\",\"other\":\"\"},'
SID_pre='[{\"id\":\"n6fhbr2s5k1e2sn5q972pzwp0t4blccl\",\"title\":\"学（工）号\",\"type\":\"number\",\"value\":\"'
SNAME_pre='{\"id\":\"2jxe0zmpig8vt024ojgyel7369iwdsyy\",\"title\":\"姓&nbsp;&nbsp;名\",\"type\":\"input\",\"value\":\"'
ACADEMY_pre='{\"id\":\"1jgr7a7q5wc9nyz8\",\"title\":\"学院\",\"type\":\"input\",\"value\":\"'
PHONE_pre='{\"id\":\"sqi19jifv9pss06zojohnmk2vbqrft1h\",\"title\":\"手机号码\",\"type\":\"number\",\"value\":\"'
BOOKDATE_pre='{\"id\":\"bcmfp7vf2kwo67dvwf5nter8cknftxwl\",\"title\":\"预订日期\",\"type\":\"time\",\"value\":\"'
WEEK_pre='{\"id\":\"pjgay090mj73uqtl4kuk36zhegteuv8e\",\"title\":\"预订时段\",\"type\":\"radio\",\"value\":\"'
WEEKDAYSTR="周一--周五时段"
WEEKENDSSTR='周六、周日时段'
TIME='19：30--21：30'
WEEKSTR=''
WEEKDAYTIME_pre='{\"id\":\"vxglipb4ow99sjua7qyk5nlt1ql38kfw\",\"title\":\"周一至周五时段\",\"type\":\"select\",\"value\":\"'
WEEKDAYTIME=''
WEEKENDTIME_pre='{\"id\":\"11j596qnl98s7id2jqh5no7tyknmed5p\",\"title\":\"周六、周日时段\",\"type\":\"select\",\"value\":\"'
WEEKENDTIME=''

bookdate=$(date -d 'tomorrow' "+%Y-%m-%d")
#echo $bookdate
weekday=$(date "+%w")

if [[ $weekday -eq 5 || $weekday -eq 6 ]]; then
	weekstr=$WEEKENDSSTR
	weekcode=$WEEKENDSCODE
	weekdaytime=''
	weekdaycode=''
	weekendtime=$TIME
	weekendcode=$WEEKENDTIMECODE
	else
	weekstr=$WEEKDAYSTR
	weekcode=$WEEKDAYCODE
	weekdaytime=$TIME
	weekdaycode=$WEEKDAYTIMECODE
	weekendtime=''
	weekendcodd=''	
fi


PAYLOAD=${PAYLOAD_pre}
customFieldsData=''
customFieldsData=${customFieldsData}${SID_pre}${sid}${COMMON_suf1}
customFieldsData=${customFieldsData}${SNAME_pre}${sname}${COMMON_suf1}
customFieldsData=${customFieldsData}${ACADEMY_pre}${academy}${COMMON_suf1}
customFieldsData=${customFieldsData}${PHONE_pre}${phone}${COMMON_suf1}
customFieldsData=${customFieldsData}${BOOKDATE_pre}${bookdate}${COMMON_suf1}
customFieldsData=${customFieldsData}${WEEK_pre}${weekstr}${COMMON_suf2}${weekcode}${COMMON_suf3}
customFieldsData=${customFieldsData}${WEEKDAYTIME_pre}${weekdaytime}${COMMON_suf2}${weekdaycode}${COMMON_suf3}
customFieldsData=${customFieldsData}${WEEKENDTIME_pre}${weekendtime}${COMMON_suf2}${weekendcode}${COMMON_suf3}

customFieldsData=$(urlencode ${customFieldsData})

PAYLOAD=${PAYLOAD}${customFieldsData}${PAYLOAD_suf}


#echo $PAYLOAD

sleep 57

res=$(curl 'https://m.chaojibiaodan.com/saveFormData.json' \
-A 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.21(0x17001525) NetType/WIFI Language/zh_CN' \
-H 'Host: m.chaojibiaodan.com' \
-H 'Accept: application/json, text/javascript, */*; q=0.01' \
-H 'X-Requested-With: XMLHttpRequest' \
-H 'Accept-Language: zh-cn' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
-H 'Origin: https://m.chaojibiaodan.com' \
-H 'Connection: keep-alive' \
-H 'Referer: https://m.chaojibiaodan.com/form/1d1u2Nk8' \
-H 'Cookie: area_level=1; area_name=%E5%85%A8%E5%9B%BD;' \
--data-binary ${PAYLOAD} \
-X POST) 
 

echo -e $res
