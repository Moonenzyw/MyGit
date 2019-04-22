import requests
import time
import random
import selenium,time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0


option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=C:\Users\悠唯\AppData\Local\Google\Chrome\User Data");

driver = webdriver.Chrome(options=option);
driver.get("https://poi5.com/index?category=4")
time.sleep(3);
everyday = driver.find_elements_by_xpath("//div[@class='post-list__item clearfix']//a[@target='_blank']");
numlist = []

for ss in everyday:
	numlist.append(ss.get_attribute("href"));

print(numlist);
hh = 22;
while hh < len(numlist):
	number = numlist[hh];
	print(hh,number);
	driver.get(number);
	time.sleep(5);
	urllist = [];

	print("111");
	preview = driver.find_elements_by_xpath("//div[@class='preview']//img");
	i = 0;
	for each in preview:
		i += 1;
		url = each.get_attribute("src");
		print(url);
		url = url.replace('/t/','/a/');
		url = url.replace('png','jpg');
		urllist.append(url);

	print("end");

	count = 0
	cookie = '_ga=GA1.2.1203952754.1555931011; _gid=GA1.2.1246918588.1555931011; sentinel=eyJpdiI6ImVCc1lDTzZ2cUozVlJxM1FPenNjV3c9PSIsInZhbHVlIjoiMjRoQkxLZ3NXdlRRUGNRdGgzbGdyaWhLV1wvOUE1Z3FUMkp0S0pLS3hxZTdnK1lFXC9yck5yZVc4c1ordUpnMHJsIiwibWFjIjoiMzUxOGE0YjQ2NzZjZTM1YmM2OTdmY2ZkYjY4Nzk0MmRjN2ZmMjE0YjIzMzc1MjI5ZGUyZDMxMWRmZTc1ODQ0ZiJ9; auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjM1NTgwLCJpc3MiOiJodHRwczovL3BvaTUuY29tL2luZGV4IiwiaWF0IjoxNTU1OTMzNjk2LCJleHAiOjE1NTU5NTUyOTYsIm5iZiI6MTU1NTkzMzY5NiwianRpIjoidW9lQUNQSmFqS295bURndyJ9.Sjgld3LlOyp1CZYDUW3g94CbHqmyXnpsE8o9YTqB0AA; poi_session=eyJpdiI6IitYVWViV1N3bU5hdlRzd2NKeDNBeXc9PSIsInZhbHVlIjoiZGhRZTdxQlNRQ0dZbnZrQUN3VDJOd2hyVWJoXC9KSVlHVEFmQTNobFZqNDFWSUpOREVjMDNoMnZua1gyTTNzS2QiLCJtYWMiOiIzYTcyZDUxNzQzYzJkYzU2MDc3NTgzYzkwYWU2Yzg5ZmUzM2M2ZmVjODJmOGE5NWI0NjlmOGI4MTM2YzE3ZGVlIn0%3D; st=1555936222'

	header = {
		'authority': 'poi5.com',
	    'scheme': 'https',
	    'method' : 'GET',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'zh-CN,zh;q=0.9',
	    'cache-control': 'max-age=0',
	    'cookie': cookie,
	    'referer': 'https://poi5.com/index',
	    'upgrade-insecure-requests': '1',
	    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
	}

	i = 0;
	for url in urllist:
		i += 1;
		html = requests.get(url,headers=header);
		print(html);
		with open("img/" + str(hh).zfill(3) + '_' + str(i).zfill(3) + '.jpg', 'wb') as file:
			file.write(html.content);

	hh += 2;
