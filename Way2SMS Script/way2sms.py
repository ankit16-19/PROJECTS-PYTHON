import requests
import csv

data = {
    'id':'xnfx',
    'ec':'0001',
    'username':''
}
login_form_data={
    'username':'/YOUR MOBILE NUMBER/',
    'password':'/YOUR PASSWORD/'
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
    
    
    open_contact_csv = open('test.csv') #Set the location to the source CSV file.
    read_csv = csv.reader(open_contact_csv)
    contact_list =list(read_csv)

    #send sms
    mobile = '/PHONE NUMBER WHOM U WANT TO SEND  SMS/'
    url_send = 'http://site24.way2sms.com/smstoss.action'
    referer_send='http://site24.way2sms.com/sendSMS?Token='+Token
    mssg = "/HERE YOU WRITE YOUR MSSG/"

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
            send = s.post(url = url_send,data = form_data_send,headers={'referer':referer_send})

    
