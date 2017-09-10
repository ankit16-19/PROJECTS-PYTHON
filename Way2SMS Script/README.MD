# Way2SMS Python Script

### Python script to send SMS to any number within Indian subcontinent using Way2SMS.

#### 1. Parameters that need to be changed 
* Your Way2SMS Username and Password in the 

`login_form_data={
	'username':'XXXXXXXXXX',
	'password':'YOURPASSWORDGOESHERE'
}`

* Change the following parameters in the `#send sms` section.

`mobile = '10 DIGIT PHONE NUMBER OF THE RECEIVER'`

`mssg = "INSERT YOUR MESSAGE HERE (LESS THAN 280 CHARACTERS)'`

Do not alter the following parameters of the `#send sms` section.

`url_send = 'http://site24.way2sms.com/smstoss.action'`

`referer_send='http://site24.way2sms.com/sendSMS?Token='+Token`

###2. Source CSV file is mandatory.
* A source CSV file which contains all the name and numbers needs to be present for the script to work. To create a CSV file in a text editor, use the following format:

`name1,mobilenumber1`

`name2, mobilenumber2`

and save the file with a `.csv` file extension.
