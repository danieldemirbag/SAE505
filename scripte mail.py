import smtplib

body = 'Subject: Subject Here.\nDear ContactName,\n\nEmail\'s BODY text\n OMG!!!!!!!!!!!!!!!!!!!!!'

try:
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)

smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('ticktask@outlook.fr', 'zy2wMUcZ44apkWc')

smtpObj.sendmail('ticktask@outlook.fr', 'stephane.gasser@uha.fr', body)

smtpObj.quit()
