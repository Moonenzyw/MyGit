import requests
import time
import re

proxies = {
    "http": "http://127.0.0.1:8123/proxy.pac:8123",
    'https': 'http://127.0.0.1:8123/proxy.pac:8123'
}
count = 0
cookie = '__cfduid=d036e783f66b36f8a5699c2320c3f7a6f1555735829; first_visit_datetime_pc=2019-04-20+18%3A39%3A03; p_ab_id=7; p_ab_id_2=0; p_ab_d_id=202115461; yuid_b=GIVECQc; __utmz=235335808.1555753178.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.2051412040.1555753178; device_token=708e32105013519eb35d0ac0cc4a085b; c_type=21; a_type=0; b_type=1; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=39961293=1^9=p_ab_id=7=1^10=p_ab_id_2=0=1^11=lang=zh=1; is_sensei_service_user=1; __utma=235335808.2051412040.1555753178.1555753178.1556010312.2; __utmc=235335808; _gid=GA1.2.1235069551.1556010313; login_bc=1; PHPSESSID=39961293_540f491e7ec60894f95ce4cad6f16ec4; privacy_policy_agreement=0; ki_r=; ki_s=196842%3A0.0.0.0.0; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~jH0uD88V6F~YmvrRNXF4U~_hSAdpN9rx~PTyxATIsK0~gViOFugGmJ~wQHVo2hTj4~Z9-nCs5pRr~88tVpKNFa-~K3gxHs5Luj~vsExduLMzo~_pwIgrV8TB~BU9SQkS-zU~y8GNntYHsi~NpsIVvS-GF~nYWbewrX1G~3A-jjuTSCD~q303ip6Ui5~9cOsTL8JKg~MhuNMsFpmN~oGXC5UutK0~LJo91uBPz4~2fTx4fs8a8~9C2OGUs0bc~2mHMFxA0cV~XMeKnjoeVa~OXID0M1Z5f~6C2rPwIfet~fWCK3-i_Fl~JL8rvDh62i~pzzjRSV6ZO~1LN8nwTqf_~8e-OBkgs0n~HY55MqmzzQ~F8PpzxrSXM~k35Wz91NYe~EdHvbaqh4D~TALRqPdJaG~U8h3GelEcb~IW_3omZpzB~9M_NEWv6tQ~3W4zqr4Xlx~qtVr8SCFs5~04ihaap-18~ZZltVrbyeV~qiHi8O6vAJ~jfd1JmTcbW~2NnAAahBhr~YRDwjaiLZn~o2vM33GyaO~nQRrj5c6w_; __utmt=1; __utmb=235335808.22.10.1556010312; ki_t=1556012429116%3B1556012429116%3B1556013215250%3B1%3B2'
header = {
	'authority': 'www.pixiv.net',
    'scheme': 'https',
    'path': '/OneSignalSDKWorker.js?appId=b2af994d-2a00-40ba-b1fa-684491f6760a',
    'method' : 'GET',
    'referer': 'https://www.pixiv.net/OneSignalSDKWorker.js?appId=b2af994d-2a00-40ba-b1fa-684491f6760a',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': cookie,
    'pragma': 'no-cache',
    'service-worker': 'script',
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
i = 0;

for date in range(20190401,20190401+1):
	mainurl = 'https://www.pixiv.net/ranking.php?format=json&mode=daily&p=1&content=illust&date=' + str(date);
	json = requests.get(mainurl,headers=header,proxies=proxies,timeout=(5,10)).text;

	urllist = re.findall(r'url":"(.+?)","illust_type',json);

	i = 0
	for url in urllist:
		i += 1;
		url = url.replace("\\","");
		url = url.replace("/c/240x480","");
		url = url.replace("_master1200","");
		url = url.replace("master","original");

		print(url);

		try:
			html = requests.get(url,headers=header,proxies=proxies,timeout=(10,20));
		except:
			continue;
		print(html);
		if (html.status_code == 200):
			with open("pixivImg/" + str(date) + '_' + str(i).zfill(2) + '.jpg', 'wb') as file:
				file.write(html.content);
			continue;

		url = url.replace("jpg","png");

		print(url);
		try:
			html = requests.get(url,headers=header,proxies=proxies,timeout=(10,20));
		except:
			continue;
		print(html);
		if (html.status_code == 200):
			with open("pixivImg/" + str(date) + '_' + str(i).zfill(2) + '.png', 'wb') as file:
				file.write(html.content);