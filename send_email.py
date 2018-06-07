import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP_SSL(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = "xx"
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()
def main():
    send_email('smtp.qq.com','xxxx@qq.com','password授权码','xxxx@qq.com','测试下','哈哈哈哈哈哈哈哈或哈哈')

if __name__ == '__main__':
    main()