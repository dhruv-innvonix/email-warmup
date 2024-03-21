# from utility.encryption_util import encrypt,decrypt
# from utility import encryption_util

# import psycopg2
# import pandas as pd
# gmail_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_gamil.csv")
# hotmail_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_hotmail.csv")
# aol_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_aol.csv")
# yahoo_df = pd.read_csv(
#     "/home/shiva/Desktop/For testing and examples/new_yahoo.csv")

# # print(gmail_df.head())
# # print(hotmail_df.head())
# # print(aol_df.head())
# # print(yahoo_df.head())
# conn = psycopg2.connect(database="EmailwarmupDB",
#                         user='postgres', password='postgres',
#                         host='localhost', port='5432'
#                         )
# conn.autocommit = True
# cursor = conn.cursor()
# # gmail_df = pd.read_excel(
# #     '/home/shiva/Downloads/Mails_data_to_test.xlsx', sheet_name='Sender_mails_data')
# # print(gmail_df.columns)
# # query = "insert into email_warmup_temporaryrecipient (id,name,email,password,app_pass_phrase,smtp_port,smtp_host,today_email_sent,email_type,imap_port,imap_host) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# # data_to_insert = (1,
# #                   "rec",
# #                   "sivaramakrishna.innvonix@gmail.com",
# #                   encrypt("krishna@046"),
# #                   encrypt("yqkdjhzphuvojsog"),
# #                   465,
# #                   "smtp.gmail.com",
# #                   False,
# #                   "gmail",
# #                   993,
# #                   "imap.gmail.com")
# # cursor.execute(query,data_to_insert)
# # cursor.execute("delete from email_warmup_emailimprovement")

# # sql_query = "INSERT INTO email_warmup_emailimprovement (id,name,email,password,smtp_port,smtp_host,is_active,number_of_days_to_warmup,app_pass_phrase,number_of_emails_sent,email_type) VALUES('%d', '%s', '%s', '%s', '%s', '%s','%s','%d','%s','%d','%s');"

# # # my_list = ["clemmiebrouillard662@hotmail.com",
# # #            "emmetbosheers319@hotmail.com",
# # #            "rebeccaprester958@hotmail.com",
# # #            "lillianvollick8932@hotmail.com"]




# # # for gmails
# # for i in gmail_df.index:
# #     # b_user="gmail_nixter_"+str(i+1)
# #     cursor.execute(sql_query % ((i+1), gmail_df['Name'][i],
# #                                 gmail_df['Mail_ID'][i], encrypt(gmail_df['Password'][i]), 465, 'smtp.gmail.com', 't', 10, encrypt(gmail_df['App_password'][i]), 0, 'gmail'))
# #     print("working",i+1)
# # print("done")


# # # # for aol mails
# # # aol_d=103
# # # for i in aol_df.index:
# # #     b_user = "aol_nixter_"+str(i+1)
# # #     cursor.execute(sql_query % ((aol_d+i), b_user,
# # #                                 aol_df['Username'][i], encrypt(aol_df['Password'][i]), 465, 'smtp.aol.com', 't', 10, encrypt(aol_df['App Password'][i]), 0, 'other'))
# # #     print("working", i+1)
# # # print("done")

# # # # for yahoo mails
# # # yahoo_d = 208
# # # for i in yahoo_df.index:
# # #     b_user = "yahoo_nixter_"+str(i+1)
# # #     cursor.execute(sql_query % ((yahoo_d+i), b_user,
# # #                                 yahoo_df['Username'][i], encrypt(yahoo_df['Password'][i]), 465, 'smtp.mail.yahoo.com', 't', 10, encrypt(yahoo_df['App Paassword'][i]), 0, 'other'))
# # #     print("working", i+1)
# # # print("done")

# # # for hotmail mails
# # # hotmail_d = 263
# # # for i in hotmail_df.index:
# # #     b_user = "hotmail_nixter_"+str(i+1)
# # #     cursor.execute(sql_query % ((hotmail_d+i), b_user,
# # #                                 hotmail_df['Email id'][i], encrypt(hotmail_df['Password'][i]), 587, 'smtp.office365.com', 't', 10, "None", 0, 'outlook'))
# # #     print("working", i+1)
# # # print("done")

# # # converting non working mails list ot csv
# # # my_list=[]
# # # cursor.execute(
# # #     "SELECT email FROM email_warmup_emailimprovement WHERE number_of_emails_sent = 3;")
# # # rows = cursor.fetchall()

# # # for row in rows:
# # #     my_list.append(row[0])
# # # # print(f"this is list--{my_list} and length of list is --{len(my_list)}")
# # # df = pd.DataFrame(my_list, columns=["working emails"])
# # # df.to_csv("wroking_aol_mails.csv")
# # # print(df)
