import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import glob
import env_details


data = []

# Searching and retrieving all the png file format name should be name.pay.png
def search_png_files():
	for d in glob.glob('*.png'):
		name = d.split('.',1)
		name2 = name[1].rsplit('.',1)
		data.append([name[0],name2[0],d])


# Searching the email of a given name
def search_email(name):
	mylist = {
		'charles':'copywritercharlesfrenoy@gmail.com',
		'elliot':'efigueira00@gmail.com',
		'emily':'amomugendi@gmail.com',
		'garrett':'Garrettgsmith87@gmail.com',
		'jackie':'Jappel2608@yahoo.com ',
		'jalil':'jaliljones1@gmail.com',
		'jani':'workaroundfamily@gmail.com',
		'lester':'lesterreandino@gmail.com',
	}
	#print(mylist.get(name,"No Name"))
	return mylist[name]


# Sending the emails to the email addresses
def send_emails(name, to_email, pay, png_file):
	# get the user details email and password
	user_details = env_details.login_user()
	msg = MIMEMultipart()
	msg['From'] = user_details['email']
	msg['To'] = to_email
	msg['Subject'] = 'Payment Breakdown'

	Message = 'Hey %s,<br><br>Here is your payment breakdown<br><br><img src="cid:image1"><br><br>Total:$%s<br><br>Thanks' % (name, pay)
	msgBody = MIMEText(Message,'html')

	fp = open(png_file,'rb')
	msgImg = MIMEImage(fp.read())
	fp.close()
	msgImg.add_header('Content-ID','<image1>')

	msg.attach(msgBody)
	msg.attach(msgImg)

	mail = smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login(user_details['email'],user_details['password'])
	mail.sendmail(msg['From'],msg['To'],msg.as_string())
	mail.close()



#Run the program
search_png_files()
for user in data:
	name = user[0]
	to_email = search_email(name)
	pay = user[1]
	png_file = user[2]
	send_emails(name, to_email,pay,png_file)
	#print( name + " - " + to_email + " - " + pay + " - " + png_file)
print('Emails Sent')

