import win32com.client as win32
import pandas as pd
from datetime import timedelta, datetime

today = datetime.today()

df = pd.DataFrame({'ColA':[1,2],'ColB':[2,3]})

receiver_addr = 'receiver@email'# change receiver@email
attachment_path = r'attachment_path'# change attachment_path

df.to_csv(attachment_path)

outlook = win32.gencache.EnsureDispatch('outlook.application')


def send_mail(receiver_addr = receiver_addr,attachment_path = attachment_path):
    mail = outlook.CreateItem(0)
    mail.To = receiver_addr    
    mail.Subject = 'Record Counts:  {} , executed by {}'.format(len(df), today.strftime('%Y-%m-%d:%H:%M:%S'))
    mail.HTMLBody = df.to_html()
    mail.Attachments.Add(attachment_path)
    mail.Send()

send_mail()

