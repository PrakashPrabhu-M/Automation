import smtplib

From='mail id here'#a mil id
tos=["mail id's here"]
subject='subject'
message="message"
username='username'
password='password'

#587-port number
conn=smtplib.SMTP('smtp.gmail.com',587)
#starting connection
conn.ehlo()

#security for password encryption
conn.starttls()

conn.login(username,password)

for to in tos:
    header = 'To:' + to + '\n' + 'From: ' + From + '\n' + 'Subject:' + subject + '\n'
    message =header + '\n'+message
    conn.sendmail(From,to,message)

conn.quit()