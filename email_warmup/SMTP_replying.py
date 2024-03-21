import pandas as pd
import imaplib
import email
import email.mime.multipart
import time
import pytz
import dateutil.parser
from email.mime.text import MIMEText
import random
try:
    from .local_files_and_variables import *
except Exception as f:
    from local_files_and_variables import *


class Reply_flow:
    def __init__(self, recipeint_mail_address,
                 recipient_app_pass_phrase,
                 recipient_password,
                 recipeint_email_type,
                 initial_mails,
                 recipient_port,
                 recipient_smtp_host,
                 recipient_imap_host,
                 reply_message,
                 sender_mail_address,
                 cursor,
                 recipient_imap_port):
        self.recipeint_mail_address = recipeint_mail_address
        self.recipient_app_pass_phrase = recipient_app_pass_phrase
        self.recipient_password = recipient_password
        self.recipeint_email_type = recipeint_email_type
        self.initial_mails = initial_mails
        self.recipient_port = recipient_port
        self.recipient_smtp_host = recipient_smtp_host
        self.recipient_imap_host = recipient_imap_host
        self.reply_message = reply_message
        self.sender_mail_address = sender_mail_address
        self.cursor = cursor
        self.recipient_imap_port = recipient_imap_port
        try:
            if self.recipeint_email_type == 'gmail':
                self.imap_ssl = imaplib.IMAP4_SSL(
                    host=str(self.recipient_imap_host), port=self.recipient_imap_port)
                logger.info(
                    f"Login to  {self.recipeint_mail_address}  for REPLY_FLOW")
                schedule_logger.info(
                    f"Login to  {self.recipeint_mail_address}  for REPLY_FLOW")
                try:
                    # Login to Mailbox
                    time.sleep(random_time)
                    resp_code, response = self.imap_ssl.login(
                        self.recipeint_mail_address, self.recipient_app_pass_phrase)

                    time.sleep(random_time)
                    logger.info("{} got logged in successfully...".format(
                        self.recipeint_mail_address))
                    schedule_logger.info("{} got logged in successfully...".format(
                        self.recipeint_mail_address))
                except Exception as gmail_configuration_error:
                    logger.error(
                        "{}--- credentials are incorrect and error is --{}".format(self.recipeint_mail_address, gmail_configuration_error))
                    schedule_logger.error(
                        "{}--- credentials are incorrect and error is --{}".format(self.recipeint_mail_address, gmail_configuration_error))
                    mail_shoot_up(subject="Reply flow error description", body="{}--- credentials are incorrect and error is --{}".format(
                        self.recipeint_mail_address, gmail_configuration_error))
            elif self.recipeint_email_type == 'outlook':
                self.imap_ssl = imaplib.IMAP4_SSL(
                    str(self.recipient_imap_host), self.recipient_imap_port)
                logger.info(
                    f"Login to  {self.recipeint_mail_address}  for REPLY_FLOW")
                schedule_logger.info(
                    f"Login to  {self.recipeint_mail_address}  for REPLY_FLOW")
                try:
                    # Login to Mailbox
                    time.sleep(random_time)
                    resp_code, response = self.imap_ssl.login(
                        self.recipeint_mail_address, self.recipient_password)

                    time.sleep(random_time)
                    logger.info("{} got logged in successfully...".format(
                        self.recipeint_mail_address))
                    schedule_logger.info("{} got logged in successfully...".format(
                        self.recipeint_mail_address))
                except Exception as outlook_configuration_error:
                    logger.error(
                        "{}--- credentials are incorrect and error is --{}".format(self.recipeint_mail_address, outlook_configuration_error))
                    schedule_logger.error(
                        "{}--- credentials are incorrect and error is --{}".format(self.recipeint_mail_address, outlook_configuration_error))
                    mail_shoot_up(subject='Reply flow error description', body="{}--- credentials are incorrect and error is --{}".format(
                        self.recipeint_mail_address, outlook_configuration_error))

            elif self.recipeint_email_type == 'other_email':
                self.imap_ssl = imaplib.IMAP4_SSL(
                    host=self.recipient_imap_host, port=self.recipient_imap_port)
                logger.info(
                    f"Login to  {self.recipeint_mail_address}  for REPLY_FLOW")
                schedule_logger.info(
                    f"Login to  {self.recipeint_mail_address}  for REPLY_FLOW")
                try:
                    # Login to Mailbox
                    time.sleep(random_time)
                    resp_code, response = self.imap_ssl.login(
                        self.recipeint_mail_address, self.recipient_password)

                    time.sleep(random_time)
                    logger.info("{} got logged in successfully...".format(
                        self.recipeint_mail_address))
                    schedule_logger.info("{} got logged in successfully...".format(
                        self.recipeint_mail_address))
                except Exception as other_mail_configuration_error:
                    logger.error(
                        "{}--- credentials are incorrect and error is --{}".format(self.recipeint_mail_address, other_mail_configuration_error))
                    schedule_logger.error(
                        "{}--- credentials are incorrect and error is --{}".format(self.recipeint_mail_address, other_mail_configuration_error))
                    mail_shoot_up(subject="Reply flow error description", body="{}--- credentials are incorrect and error is --{}".format(
                        self.recipeint_mail_address, other_mail_configuration_error))
            else:
                logger.error(
                    "{}--This id did't matched to definded email_type".format(self.recipeint_mail_address))
                schedule_logger.error(
                    "{}--This id did't matched to definded email_type".format(self.recipeint_mail_address))
                mail_shoot_up(subject="Reply flow error description",
                              body="{}--This id did't matched to definded email_type".format(self.recipeint_mail_address))
        except Exception as main_configuration_error:
            logger.error("Error is with mail id ---{}--- and error we get is --{}".format(
                self.recipeint_mail_address, main_configuration_error))
            schedule_logger.error("Error is with mail id ---{}--- and error we get is --{}".format(
                self.recipeint_mail_address, main_configuration_error))
            mail_shoot_up(subject="Reply flow error description", body="Error is with mail id ---{}--- and error we get is --{}".format(
                self.recipeint_mail_address, main_configuration_error))

        self.final_sender_df = self.todays_mails_collector()

    def copy_mails_and_deleteing_mails(self):
        if self.recipeint_email_type == 'gmail':
            # Set Mailbox for gmail
            resp_code, mail_count = self.imap_ssl.select(
                mailbox="[Gmail]/Spam", readonly=False)
            logger.info("{} got in for copying and deleting mails ...".format(
                self.recipeint_mail_address))
            schedule_logger.info("{} got in for copying and deleting mails ...".format(
                self.recipeint_mail_address))

        elif self.recipeint_email_type == 'outlook':
            # Set Mailbox for outlook
            time.sleep(random_time)
            resp_code, mail_count = self.imap_ssl.select(
                mailbox="Junk", readonly=False)
            logger.info("{} got in for copying and deleting mails ...".format(
                self.recipeint_mail_address))
            schedule_logger.info("{} got in for copying and deleting mails ...".format(
                self.recipeint_mail_address))
        elif self.recipeint_email_type == 'other_email':
            # Set Mailbox for gmail
            resp_code, mail_count = self.imap_ssl.select(
                mailbox="INBOX.spam", readonly=False)
            logger.info("{} got in for copying and deleting mails ...".format(
                self.recipeint_mail_address))
            schedule_logger.info("{} got in for copying and deleting mails ...".format(
                self.recipeint_mail_address))
        # Retrieve Mail IDs for given Directory
        time.sleep(random_time)
        resp_code, mails = self.imap_ssl.search(None, "ALL")
        time.sleep(random_time)
        mailes = mails[0].decode().split()
        time.sleep(random_time)
        logger.info("Total mails in spam is ---{}".format(mailes))
        schedule_logger.info(
            "Total mails in spam is ---{}".format(mailes))

        if len(mailes) != 0:
            # collecting mails for copying and deleting flow from spam-inbox
            time.sleep(random_time)
            mail_ids = mails[0].decode().split()[-2:]
            mail_ids = ":".join(mail_ids)
            resp_code, response = self.imap_ssl.copy(mail_ids, "INBOX")
            # Copying all Messages to inbox
            time.sleep(random_time)
            mail_ids = mails[0].decode().split()[:]
            for mail_id in mail_ids:
                resp_code, response = self.imap_ssl.copy(mail_id, "INBOX")
            logger.info("Total mails in spam got copied to inbox ")
            schedule_logger.info(
                "Total mails in spam got copied to inbox ")

            # Search and delete mails in a given Directory
            time.sleep(random_time)
            resp_code, mails = self.imap_ssl.search(None, "ALL")
            mail_ids = mails[0].decode().split()
            try:
                for mail_id in mail_ids[:]:
                    resp_code, mail_data = self.imap_ssl.fetch(
                        mail_id, '(RFC822)')
                    message = email.message_from_bytes(mail_data[0][1])
                    resp_code, response = self.imap_ssl.store(
                        mail_id, '+FLAGS', '\\Deleted')  # Setting Deleted Flag
                resp_code, response = self.imap_ssl.expunge()
                logger.info("Total mails in spam got deleted ")
                schedule_logger.info(
                    "Total mails in spam got deleted ")
            except Exception as w:
                # Close Selected Mailbox
                logger.info("while copying and deleting mails we got error and error is --- {}".format(
                    w))
                schedule_logger.info("while copying and deleting mails we got error and error is --- {}".format(
                    w))
        else:
            logger.info("this {} ID has {} mails so continuing to next function ".format(
                self.recipeint_mail_address, len(mailes)))
            schedule_logger.info("this {} ID has {} mails so continuing to next function ".format(
                self.recipeint_mail_address, len(mailes)))

    def todays_mails_collector(self):
        import pdb; pdb.set_trace()
        data_fetcher_data_list = []
        # Set Mailbox
        time.sleep(random_time)
        resp_code, mail_count = self.imap_ssl.select(
            mailbox="INBOX", readonly=True)
        logger.info("{} got in for todays_mails_collector ...".format(
                    self.recipeint_mail_address))
        schedule_logger.info("{} got in for todays_mails_collector ...".format(
            self.recipeint_mail_address))
        # Retrieve Mail IDs for given Directory
        time.sleep(random_time)
        resp_code, mail_ids = self.imap_ssl.search(None, "ALL")
        # Display Few Messages for given Directory
        time.sleep(random_time)
        for mail_id in mail_ids[0].decode().split()[-self.initial_mails:]:
            resp_code, mail_data = self.imap_ssl.fetch(
                mail_id, '(RFC822)')
            time.sleep(random_time)
            message = email.message_from_bytes(mail_data[0][1])
            from_email = message.get("From")
            try:
                from_email = from_email.split()
                from_email = from_email[-1]
                from_email = from_email.replace("<", '')
                from_email = from_email.replace(">", '')
            except Exception as email_id_splitting_error:
                logger.error(
                    "The error is with spliting is----{}".format(email_id_splitting_error))
                schedule_logger.error(
                    "The error is with spliting is----{}".format(email_id_splitting_error))
                from_email = message.get("From")
                mail_shoot_up(subject="Reply flow error description",
                              body="The error is with spliting is----{}".format(email_id_splitting_error))
                continue
            md = message.get('date')
            # converting the timezone to utc
            try:
                TZINFOS = {'PDT': pytz.timezone('US/Pacific')}
                datetime_obj = dateutil.parser.parse(
                    md, tzinfos=TZINFOS)
                datetime_in_utc = datetime_obj.astimezone(
                    pytz.utc)  # convert to UTC
                msg_date = (str(datetime_in_utc).split())[0]
            except Exception as time_zone_formatting_error:
                logger.error("this is timezone error{}".format(
                    time_zone_formatting_error))
                schedule_logger.error(
                    "this is timezone error{}".format(time_zone_formatting_error))
                mail_shoot_up(subject="Reply flow error description",
                              body="this is timezone error{}".format(time_zone_formatting_error))
            My_mail_id = mail_id
            message_id = message.get("MESSAGE-ID")
            to_email = message.get("To")
            subject = message.get("Subject")
            data_fetcher_data_list.append(
                (msg_date, from_email, message_id, to_email, subject, My_mail_id))
        df1 = pd.DataFrame(set(data_fetcher_data_list), columns=[
            "DF_msg_date", "DF_from_email", "DF_message_id", "DF_to_email", "DF_subject", "My_mail_id"])
        final_sender_df = df1[df1.DF_msg_date == str(date.today())]

        def low(x: str):
            return x.lower()
        self.sender_mail_address = list(map(low, self.sender_mail_address))
        final_sender_df = final_sender_df[final_sender_df['DF_from_email'].isin(
            self.sender_mail_address)]
        return final_sender_df

    def Marking_as_read_and_favourite(self):
        Mails_id_today = self.final_sender_df["My_mail_id"]
        try:
            # selecting mailbox
            resp_code, mail_count = self.imap_ssl.select(
                mailbox="INBOX", readonly=False)
            logger.info("{} got in for todays_Marking_as_read and adding_to_favourite process ...".format(
                self.recipeint_mail_address))
            schedule_logger.info("{} got in for todays_Marking_as_read and adding_to_favourite process ...".format(
                self.recipeint_mail_address))
            # Retrieve Mail IDs for given Directory
            resp_code, mails = self.imap_ssl.search(None, "ALL")
            mail_ids = mails[0].decode().split()
            for mail_id in Mails_id_today:
                resp_code, mail_data = self.imap_ssl.store(
                    mail_id, "+FLAGS", "\SEEN")
                resp_code, mail_data = self.imap_ssl.store(
                    mail_id, "+FLAGS", "\Flagged")

        except Exception as marking_as_read_and_favourite_error:
            logger.error("we got some error with {}  while marking as read and adding_to_favourite and error is ---{} ".format(
                self.recipeint_mail_address, marking_as_read_and_favourite_error))
            schedule_logger.error("we got some error with {}  while marking as read and adding_to_favourite and error is ---{} ".format(
                self.recipeint_mail_address, marking_as_read_and_favourite_error))
            mail_shoot_up(subject="Reply flow error description", body="we got some error with {}  while marking as read and adding_to_favourite and error is ---{} ".format(
                self.recipeint_mail_address, marking_as_read_and_favourite_error))

    def todays_replier(self):
        logger.info("{} got in for todays_replier process ...".format(
            self.recipeint_mail_address))
        schedule_logger.info("{} got in for todays_replier process ...".format(
            self.recipeint_mail_address))
        message_id = self.final_sender_df["DF_message_id"]
        subject = self.final_sender_df["DF_subject"]
        new_user_mail = self.final_sender_df["DF_from_email"]
        logger.info("{} --final_replier_dataframe is --{} ...".format(
            self.recipeint_mail_address, self.final_sender_df))
        schedule_logger.info("{} --final_replier_dataframe is --{} ...".format(
            self.recipeint_mail_address, self.final_sender_df))
        try:
            if self.recipeint_email_type == 'gmail':
                
                try:
                    server = smtplib.SMTP(
                        str(self.recipient_smtp_host), 587)
                    server.starttls()
                    time.sleep(random_time)
                    server.login(
                        self.recipeint_mail_address, self.recipient_app_pass_phrase)
                    logger.info(
                        "{}--got logged in for reply in final df_flow".format(self.recipeint_mail_address))
                    schedule_logger.info(
                        "{}--got logged in for reply in final df_flow".format(self.recipeint_mail_address))
                    time.sleep(random_time)
                except Exception as gmail_smtp_cinfiguration_error:
                    logger.error(
                        "the error is with inside final df_flow---{}---and error we got is--{}".format(self.recipeint_mail_address, gmail_smtp_cinfiguration_error))
                    schedule_logger.error(
                        "the error is with inside final df_flow---{}---and error we got is--{}".format(self.recipeint_mail_address, gmail_smtp_cinfiguration_error))
                    mail_shoot_up(subject="Reply flow error description", body="the error is with inside final df_flow---{}---and error we got is--{}".format(
                        self.recipeint_mail_address, gmail_smtp_cinfiguration_error))
            elif self.recipeint_email_type == 'outlook':
                try:
                    server = smtplib.SMTP(
                        str(self.recipient_smtp_host), int(self.recipient_port))
                    server.starttls()
                    time.sleep(random_time)
                    server.login(
                        self.recipeint_mail_address, self.recipient_password)
                    logger.info(
                        "{}--got logged in for reply in final df_flow".format(self.recipeint_mail_address))
                    schedule_logger.info(
                        "{}--got logged in for reply in final df_flow".format(self.recipeint_mail_address))
                    time.sleep(random_time)
                except Exception as outlook_smtp_cinfiguration_error:
                    logger.error(
                        "the error is with inside final df_flow---{}---and error we got is--{}".format(self.recipeint_mail_address, outlook_smtp_cinfiguration_error))
                    schedule_logger.error(
                        "the error is with inside final df_flow---{}---and error we got is--{}".format(self.recipeint_mail_address, outlook_smtp_cinfiguration_error))
                    mail_shoot_up(subject="Reply flow error description", body="the error is with inside final df_flow---{}---and error we got is--{}".format(
                        self.recipeint_mail_address, outlook_smtp_cinfiguration_error))
            elif self.recipeint_email_type == 'other_email':
                try:
                    server = smtplib.SMTP_SSL(
                        str(self.recipient_smtp_host), int(self.recipient_port))
                    time.sleep(random_time)
                    server.login(
                        self.recipeint_mail_address, self.recipient_password)
                    logger.info(
                        "{}--got logged in for reply in final df_flow".format(self.recipeint_mail_address))
                    schedule_logger.info(
                        "{}--got logged in for reply in final df_flow".format(self.recipeint_mail_address))
                    time.sleep(random_time)
                except Exception as othermail_smtp_cinfiguration_error:
                    logger.error(
                        "the error is with inside final df_flow---{}---and error we got is--{}".format(self.recipeint_mail_address, othermail_smtp_cinfiguration_error))
                    schedule_logger.error(
                        "the error is with inside final df_flow---{}---and error we got is--{}".format(self.recipeint_mail_address, othermail_smtp_cinfiguration_error))
                    mail_shoot_up(subject="Reply flow error description", body="the error is with inside final df_flow---{}---and error we got is--{}".format(
                        self.recipeint_mail_address, othermail_smtp_cinfiguration_error))

            else:
                logger.error(
                    "{}--This id not matched to our defined email_type".format(self.recipeint_mail_address))
                schedule_logger.error(
                    "{}--This id not matched to our defined email_type".format(self.recipeint_mail_address))
                mail_shoot_up(subject="Reply flow error description",
                              body="{}--This id not matched to our defined email_type".format(self.recipeint_mail_address))

            try:
                for sender in self.final_sender_df.index:
                    message = EmailMessage()
                    mail_content = random.choice(self.reply_message)
                    sender_address = self.recipeint_mail_address
                    # nixter_1@yahoo.com
                    receiver_address = new_user_mail[sender]
                    message['From'] = self.recipeint_mail_address
                    message['To'] = receiver_address
                    message.set_content(mail_content)
                    message['Subject'] = "RE:" + subject[sender]
                    message['In-Reply-To'] = message_id[sender]
                    message['References'] = message_id[sender]
                    text = message.as_string()
                    server.sendmail(sender_address,
                                    receiver_address, text)
                    time.sleep(random.uniform(25, 35))
                    logger.info("reply sent to {1} from {0}".format(
                        self.recipeint_mail_address, receiver_address))
                    schedule_logger.info("reply sent to {1} from {0}".format(
                        self.recipeint_mail_address, receiver_address))
                    try:
                        self.cursor.execute(
                            f"update email_warmup_temporaryrecipient set today_email_sent=True where email='{self.recipeint_mail_address}'")
                    except Exception as cursor_error:
                        logger.error(
                            "{}--has got the error while updating query as true and the error is ---{}".format(self.recipeint_mail_address, cursor_error))
                        schedule_logger.error(
                            "{}--has got the error while updating query as true and the error is ---{}".format(self.recipeint_mail_address, cursor_error))
                        mail_shoot_up(subject="Reply flow error description", body="{}--has got the error while updating query as true and the error is ---{}".format(
                            self.recipeint_mail_address, cursor_error))
            except Exception as mail_sending_in_forloop_error:
                logger.error(
                    "{}--has got the error while sending forloop mail and the error is ---{}".format(self.recipeint_mail_address, mail_sending_in_forloop_error))
                schedule_logger.error(
                    "{}--has got the error while sending forloop mail and the error is ---{}".format(self.recipeint_mail_address, mail_sending_in_forloop_error))
                mail_shoot_up(subject="Reply flow error description", body="{}--has got the error while sending forloop mail and the error is ---{}".format(
                    self.recipeint_mail_address, mail_sending_in_forloop_error))
            time.sleep(random_time)
            server.quit()
        except Exception as internal_error_on_reply_flow:
            logger.error("{} --got an error while replying today's mail and error is {}".format(
                self.recipeint_mail_address, internal_error_on_reply_flow))
            schedule_logger.error("{} --got an error while replying today's mail and error is {}".format(
                self.recipeint_mail_address, internal_error_on_reply_flow))
            mail_shoot_up(subject="Reply flow error description", body="{} --got an error while replying today's mail and error is {}".format(
                self.recipeint_mail_address, internal_error_on_reply_flow))

        resp_code, response = self.imap_ssl.logout()
        logger.info("The Reply_flow is successfully completed for ---{} ".format(
            self.recipeint_mail_address))
        schedule_logger.info("The Reply_flow is successfully completed for ---{} ".format(
            self.recipeint_mail_address))


def SMTP_reply_flow_starter_job():
    try:
        Vpn_starter()
        time.sleep(60)
        ip_status_check = Ip_address_checker()
        if ip_status_check == "ip_not_changed":
            schedule_logger.error("Ip didn't changed please check vpn once")
            logger.error("Ip didn't changed please check vpn once")
            mail_shoot_up(subject="Reply flow error description",
                          body="Ip didn't changed please check vpn once")
        replying_object = DataReader()
        cursor = replying_object.cursor
        replying_object.recipient_details()
        recipient_file = replying_object.recipient_file
        recipeint_mail_address = replying_object.recipeint_mail_address
        recipient_app_pass_phrase = replying_object.recipient_app_pass_phrase
        recipient_password = replying_object.recipient_password
        recipeint_email_type = replying_object.recipeint_email_type
        recipient_port = replying_object.recipient_port
        recipient_smtp_host = replying_object.recipient_smtp_host
        recipient_imap_host = replying_object.recipient_imap_host
        recipient_imap_port = replying_object.recipeint_imap_port
        replying_object.fetching_DB_Tables()
        replying_object.parameters_definder_function()
        initial_mails = replying_object.initial_mails
        reply_message = replying_object.reply_message
        sender_mail_address = list(
            map(str.lower, (replying_object.sender_mail_address.to_list())))

        schedule_logger.info(
            "SMTP_REPLY_flow_started at----{0} and system time is ---{1}".format(replying_object.reply_time_value, datetime.now() + timedelta()))
        logger.info(
            "SMTP_REPLY_flow_started at----{0} and system time is ---{1}".format(replying_object.reply_time_value, datetime.now() + timedelta()))
        for i in recipient_file.index:
            if recipeint_email_type[i] == 'gmail' or recipeint_email_type[i] == 'outlook' or recipeint_email_type[i] == 'other_email':
                try:
                    reply_flow_object = Reply_flow(
                        recipeint_mail_address[i],
                        recipient_app_pass_phrase[i],
                        recipient_password[i],
                        recipeint_email_type[i],
                        initial_mails,
                        recipient_port[i],
                        recipient_smtp_host[i],
                        recipient_imap_host[i],
                        reply_message,
                        sender_mail_address,
                        cursor,
                        recipient_imap_port[i])
                    reply_flow_object.copy_mails_and_deleteing_mails()
                    reply_flow_object.Marking_as_read_and_favourite()
                    reply_flow_object.todays_replier()
                except Exception as replying_job_error:
                    logger.error("we got some error with {}  while SMTP_reply_flow_starter_job and error is ---{} ".format(
                        recipeint_mail_address[i], replying_job_error))
                    schedule_logger.error("we got some error with {}  while SMTP_reply_flow_starter_job and error is ---{} ".format(
                        recipeint_mail_address[i], replying_job_error))
                    mail_shoot_up(subject="Reply flow error description", body="we got some error with {}  while SMTP_reply_flow_starter_job and error is ---{} ".format(
                        recipeint_mail_address[i], replying_job_error))
            else:
                continue
        try:
            cursor.execute('delete from email_warmup_temporaryrecipient')
        except Exception as truncate_error:
            schedule_logger.error(
                f"Got an error while deleting the temporary table and error is ---{truncate_error}")
            logger.error(
                f"Got an error while deleting the temporary table and error is ---{truncate_error}")
            mail_shoot_up(subject="Reply flow error description",
                          body=f"Got an error while deleting the temporary table and error is ---{truncate_error}")
        Vpn_quiter()
        time.sleep(60)
        ip_status_check = Ip_address_checker()
        schedule_logger.info(
            "SMTP_REPLY_flow  completed at--{}".format(datetime.now() + timedelta()))
        logger.info(
            "SMTP_REPLY_flow  completed at--{}".format(datetime.now() + timedelta()))
    except Exception as SMTP_reply_flow_starter_job_error:
        schedule_logger.error(
            f"Got an main error while running SMTP_reply_flow_starter_job and the error is ---{SMTP_reply_flow_starter_job_error}")
        logger.error(
            f"Got an main error while running SMTP_reply_flow_starter_job and the error is ---{SMTP_reply_flow_starter_job_error}")
        mail_shoot_up(subject="Reply flow error description",
                      body=f"Got an main error while running SMTP_reply_flow_starter_job and the error is ---{SMTP_reply_flow_starter_job_error}")
        Vpn_quiter()
        time.sleep(30)
        ip_status_check = Ip_address_checker()
