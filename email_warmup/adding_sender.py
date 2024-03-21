from utility.encryption_util import encrypt, decrypt
from utility import encryption_util

import psycopg2
import pandas as pd
# gmail_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_gamil.csv")
# hotmail_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_hotmail.csv")
# aol_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_aol.csv")
# yahoo_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_yahoo.csv")

gamil_df = pd.read_csv("/home/innvonix/Documents/gmail_demo_1.csv")
# print(gmail_df.head())
# print(hotmail_df.head())
# print(aol_df.head())
# print(yahoo_df.head())
conn = psycopg2.connect(database="emailwarmup_1",
                        user='postgres', password='admin',
                        host='localhost', port='5432'
                        )
conn.autocommit = True
cursor = conn.cursor()
# sender_df = pd.read_excel(
#     '/home/shiva/Downloads/Mails_data_to_test.xlsx', sheet_name='Sender_mails_data')
# recipient_df = pd.read_excel(
#     '/home/shiva/Downloads/Mails_data_to_test.xlsx', sheet_name='Recipient_mails_data')
# print(recipient_df.columns)

# # for entering data into email_warmup_emailimprovement
# sql_query = "INSERT INTO email_warmup_emailimprovement (id,name,email,password,smtp_port,smtp_host,is_active,number_of_days_to_warmup,app_pass_phrase,number_of_emails_sent,email_type) VALUES('%d', '%s', '%s', '%s', '%s', '%s','%s','%d','%s','%d','%s');"

# # for gmails
# for i in gamil_df.index:
#     cursor.execute(sql_query % ((i+1), sender_df['Name'][i],
#                                 sender_df['Mail_ID'][i], encrypt(sender_df['Password'][i]), 465, 'smtp.gmail.com', 't', 10, encrypt(sender_df['App_password'][i]), 0, 'gmail'))
#     print("working", i+1)
# print("done")


# # for entering data into email_warmup_temporaryrecipient
# query = "INSERT INTO email_warmup_temporaryrecipient (id,name,email,password,app_pass_phrase,smtp_port,smtp_host,today_email_sent,email_type,imap_port,imap_host) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# for i in recipient_df.index:
#     data_to_insert = (i+1,
#                       recipient_df["Name"][i],
#                       recipient_df["Mail_ID"][i],
#                       encrypt(str(recipient_df["Password"][i])),
#                       encrypt(str(recipient_df["App_password"][i])),
#                       int(recipient_df["Smtp_port"][i]),
#                       recipient_df["Smtp_host"][i],
#                       False,
#                       recipient_df["Mail_type"][i],
#                       int(recipient_df["Imap_port"][i]),
#                       recipient_df["Imap_host"][i])
#     cursor.execute(query, data_to_insert)

query = "INSERT INTO email_warmup_gmailrecipient (id,name,email,password,app_pass_phrase,smtp_port,smtp_host,imap_port,imap_host) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

for i in gamil_df.index:
    data_to_insert = (i+1,
                      gamil_df["Name"][i],
                      gamil_df["Mail_ID"][i],
                      encrypt(str(gamil_df["Password"][i])),
                      encrypt(str(gamil_df["App_password"][i])),
                      int(gamil_df["Smtp_port"][i]),
                      gamil_df["Smtp_host"][i],
                    #   False,
                    #   gamil_df["Mail_type"][i],
                      int(gamil_df["Imap_port"][i]),
                      gamil_df["Imap_host"][i])
    cursor.execute(query, data_to_insert)
# Commit the changes to the database and close the connection
conn.commit()
conn.close()


# # to delete email_warmup_emailimprovement table
# cursor.execute("delete from email_warmup_emailimprovement")

# # to delete email_warmup_temporaryrecipient table
# cursor.execute("delete from email_warmup_temporaryrecipient")


# conn.commit()
# conn.close()
