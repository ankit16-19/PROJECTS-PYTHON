#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
# from twilio.rest import TwilioRestClient 
import requests
import csv
import time
from random import randint
 


display = Display(visible=0, size=(800, 600))
display.start()



chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}#setting img to no load state 
chromeOptions.add_experimental_option("prefs",prefs)#adding prefs to the chrome options

browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver",chrome_options = chromeOptions)



browser.get('https://hib.iiit-bh.ac.in/Hibiscus/Login/?client=iiit')
#*****************locating filling space**********
uid = browser.find_element_by_name('uid')
pwd = browser.find_element_by_name('pwd')
txtInput = browser.find_element_by_name('txtInput')
#******************details******************
userid = "+xxxxx+"
password = "+xxxxxxx"
captcha = browser.find_element_by_id('txtCaptcha').get_attribute("value")
#*****************filling details**********
uid.send_keys(userid)
pwd.send_keys(password)
txtInput.send_keys(captcha)
#*****************submit************
submit = browser.find_element_by_xpath("/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/input").click()

def subject(currsemester,semester):

	start = (currsemester-semester)*11 + 1
	end = start + 10
	for i in range(start,end):
	 	browser.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/aisMenu.php")
	 	my_courses = browser.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/div[1]/a").click()
		xpath = "/html/body/div/div[2]/table/tbody/tr[i]/td[3]/a"
		xpath = xpath[:37] + str(i) + xpath[38:]
		subi = browser.find_element_by_xpath(xpath).click()
		attendance_linki = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[4]/li[3]/a").click()
		attendencei = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[2]/td/pre").text
		browser.execute_script("window.history.go(-1)")
		grades_linki = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[3]/li[2]/a").click()
		quiz1i = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[3]").text
		quiz2i = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[4]").text
		midsemi = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[5]").text
		# endsemi = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[6]").text
		# facultyi = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[7]").text
		# gpbfrpeni = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[8]").text
		# peni = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[9]").text
		# gradepointi = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[10]").text
		# finalgradei = browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[11]").text
		print attendencei,quiz1i,quiz2i,midsemi

def pseudofeedback(currsemester,semester):
	start = (currsemester-semester)*11+1
	end = start + 10
	for i in range (start,end):
		browser.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/aisMenu.php")
	 	my_courses = browser.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/div[1]/a").click()
		xpath = "/html/body/div/div[2]/table/tbody/tr[i]/td[3]/a"
		xpath = xpath[:37] + str(i) + xpath[38:]
		subi = browser.find_element_by_xpath(xpath).click()
		feedback_linki = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[4]/li[2]/a").click()
		feedback_first = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[2]/td[3]/a").click()
		for j in range (2,14):
			xpath = "/html/body/div/table/tbody/tr/td/table/tbody/tr[i]/td[4]/input"
			xpath = xpath[:48] + str(j) + xpath[49:]
			radiofillij = browser.find_element_by_xpath(xpath).click()
		fill1 = "Got to know something new"
		fill2 = "Nothhing"
		fill3 = "NONE"
		fill1_location	= browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[15]/td[3]/textarea")
		fill1_location.send_keys(fill1)
		fill2_location = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[16]/td[3]/textarea")
		fill2_location.send_keys(fill2)
		fill3_location = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[17]/td[3]/textarea")
		fill3_location.send_keys(fill3)

	

def notification():
	burl_i=browser.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/?w=1366&h=338")
	
	browser.switch_to.frame(browser.find_element_by_name("main"))
	href_file = open("/home/ankit/Desktop/href_details.txt","r")

	last_mssg_id = href_file.readline()
	href_file.close()
	last_mssg_id = last_mssg_id[64:]
	last_mssg_id = last_mssg_id[:4]


	href = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a").get_attribute("href")
	href = href[64:]
	href = href[:4]	
	diff = int(href) - int(last_mssg_id)	
	for i in range (diff,0,-1):
		burl_i=browser.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/?w=1366&h=338")
		browser.switch_to.frame(browser.find_element_by_name("main"))
		xpathdate = "/html/body/div/div[2]/table/tbody/tr[1]/td[1]"
		xpathdate = xpathdate[:37] + str(i) + xpathdate[38:]
		xpathtitle = "/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a"
		xpathtitle = xpathtitle[:37] + str(i) + xpathtitle[38:]
		xpathposted_by="/html/body/div/div[2]/table/tbody/tr[1]/td[3]/font"
		xpathposted_by= xpathposted_by[:37] + str(i) + xpathposted_by[38:]
		xpathattention="/html/body/div/div[2]/table/tbody/tr[1]/td[4]/font"
		xpathattention = xpathattention[:37] + str(i) + xpathattention[38:]
		xpathtitle_link = "/html/body/div/div[2]/table/tbody/tr[i]/td[2]/a"
		xpathtitle_link = xpathtitle_link[:37] +str(i) + xpathtitle_link[38:]
		
		xpathhref = "/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a"
		xpathhref = xpathhref[:37] + str(i) + xpathhref[38:] 


		date = browser.find_element_by_xpath(xpathdate).text
		title = browser.find_element_by_xpath(xpathtitle).text
		posted_by = browser.find_element_by_xpath(xpathposted_by).text
		attention = browser.find_element_by_xpath(xpathattention).text
		href = browser.find_element_by_xpath(xpathhref).get_attribute("href")

		
		title_link = browser.find_element_by_xpath(xpathtitle_link).click()
		title_text = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td/div").text



		# browser.get("http://textuploader.com/")
		# text_area = browser.find_element_by_xpath("//*[@id=\"textdata\"]")
		# text_area.send_keys(title_text)
		# submitpaste = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div/div[2]/form/div[2]/div/div[5]/input").click()
		# current_url = browser.current_url



		mssg = date+"|"+title+"|"+posted_by+"|"+attention
		print mssg + " " + time.strftime("%I:%M:%S") + " "  + time.strftime("%d/%m/%Y")
		#*****************************************************************************************************
		#***************************************************************************************************
		#put your own credentials here 	
		data = {
		    'id':'xnfx',
		    'ec':'0001',
		    'username':''
		}
		z  = randint(1,2)
		if(z==1):
			login_form_data={
		   		'username':'+xxxxxxxx',
		    	'password':'++xxxxxxx'
			}
		if(z==2):
			login_form_data={
		    	'username':'+xxxxxxxxx',
		    	'password':'++xxxxxxxx'
			}	


		with requests.session() as s:
		    pre_login = s.get("http://site24.way2sms.com/entry.action?id=xnfx&ec=0001&username=",data = data)
		       
		    login = s.post("http://site24.way2sms.com/Login1.action",data = login_form_data,headers={'referer':'http://site24.way2sms.com/entry.action?id=xnfx&ec=0001&username='})
		    Token =  login.url[42:]
		    
		    params_sms_page = {
		    'section':'s',
		    'Token':Token,
		    'vfType':'register_verify'
		    }
		    sms_page_url = "http://site24.way2sms.com/main.action?section=s&Token="+Token+"&vfType=register_verify"    
		    sms_page_referer = "http://site24.way2sms.com/ebrdg.action?id="+Token
		    sms_page = s.get(url = sms_page_url,params = params_sms_page,headers={'referer':sms_page_referer})



		    send_sms_page_url = "http://site24.way2sms.com/jsp/ReAdd.jsp?Token="+Token
		    send_sms_page_referer = "http://site24.way2sms.com/main.action?section=s&Token="+Token+"&vfType=register_verify"
		    parms_send_sms_page={
		    'Token':Token
		    }
		    send_sms_page  = s.get(url = sms_page_url,params = parms_send_sms_page,headers={'referer':sms_page_referer})
		    

		    open_contact_csv = open('/home/ankit/Desktop/test.csv')
		    read_csv = csv.reader(open_contact_csv)
		    contact_list =list(read_csv)

		    #send sms
		    url_send = 'http://site24.way2sms.com/smstoss.action'
		    referer_send='http://site24.way2sms.com/sendSMS?Token='+Token
		    

		    for i in contact_list:
		        mobile = i[1]
		        len_mssg = len(mssg)
		        if(len_mssg>140):
		            mssg1 = mssg[:140]
		            mssg2 = mssg[140:]
		            mssglist = [mssg1, mssg2]
		        else:
		            mssglist = [mssg]
		                    
		        for j in mssglist:
		            form_data_send = {
		            'ssaction':'ss',
		            'Token':Token,
		            'mobile':mobile,
		            'message':j,
		            'msgLen':140 - len(j)
		            }
		            time.sleep(1)
		            send = s.post(url = url_send,data = form_data_send,headers={'referer':referer_send})
		            z = int(z) + 1
	

		href_file_update = open("/home/ankit/Desktop/href_details.txt","w+")
		href_file_update.write(href)




notification()
# subject(2,1)
# pseudofeedback(2,1)


browser.quit()
display.stop()

