from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

browser.get('https://hib.iiit-bh.ac.in/Hibiscus/Login/?client=iiit')
#*****************locating filling space**********
uid = browser.find_element_by_name('uid')
pwd = browser.find_element_by_name('pwd')
txtInput = browser.find_element_by_name('txtInput')
#******************details******************
userid = "GB216008"
password = "Ankit123@"
captcha = browser.find_element_by_id('txtCaptcha').get_attribute("value")
#*****************filling details**********
uid.send_keys(userid)
pwd.send_keys(password)
txtInput.send_keys(captcha)
#*****************submit************
submit = browser.find_element_by_xpath("/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/input").click()

def subjectgrades(currsemester,semester):

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
	browser.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/?w=1366&h=338")
	browser.switch_to.frame(browser.find_element_by_name("main"))
	date = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[1]").text
	title = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a").text
	posted_by = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[3]/font").text
	attention = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[4]/font").text
	title_link = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
	title_text = browser.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td/div").text
	print (title_text)

def attendence(currsemester,semester):
	start = (currsemester-semester)*11+1
	end = start + 10
	browser.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/aisMenu.php")
	attendence_link = browser.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/div[4]/a").click()
	for i in range (start,end):
		xpath_name = "/html/body/div/div[2]/table/tbody/tr[1]/td[3]"
		xpath_attendence = "/html/body/div/div[2]/table/tbody/tr[1]/td[4]"
		xpath_name = xpath_name[:37] + str(i) + xpath_name[38:]
		xpath_attendence = xpath_attendence[:37] + str(i) + xpath_attendence[38:] 
		subnamei = browser.find_element_by_xpath(xpath_name).text
		subattendencei = browser.find_element_by_xpath(xpath_attendence).text
		print subnamei
		print "Present	   Absent	Leave	Total"
		print subattendencei
		print ""



attendence(2,1)
notification()
subject(2,1)
pseudofeedback(2,1)


browser.close()
