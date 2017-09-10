#!/usr/bin/env python

import requests
import time


login_req = requests.get("http://www.iiit-bh.ac.in")
login_req_url = login_req.url
magic_token = login_req_url[32:]

if(login_req_url!="http://www.iiit-bh.ac.in/"):
	with requests.session() as s:
		login_url = "http://172.16.1.11:1000/"
		referer = login_req_url

		login_form = {
		"4Tredir":"http://www.iiit-bh.ac.in/",
		"magic":magic_token,
		"username":"B1xxxx",
		"password":"xxxxxx"
		}

		login = s.post(url = login_url,data = login_form,headers={'referer':referer})
		if(login.headers['Content-Length']!=1559):
			print "success" + " " +  time.strftime("%I:%M:%S") + " " + time.strftime("%d/%m/%Y")
		else:
			print "Target overflow" + " " + time.strftime("%I:%M:%S")	+ " " + time.strftime("%d/%m/%Y")


	

