from time import time
import smtplib
from email.message import EmailMessage
import time
import datetime
import random
try:
    from local_files_and_variables import *
except Exception as f:
    from .local_files_and_variables import *


def start_SMTP_mailing(cursor,
                       sender_file,
                       sender_mail_type,
                       sender_mail_address,
                       sender_password,
                       sender_app_pass_phrase,
                       number_of_emails_sent,
                       number_of_days_to_warmup,
                       recipient_file,
                       recipeint_mail_address,
                       subject,
                       message,
                       sender_port_number,
                       sender_host_name):

    for Sent_rows in sender_file.index:
        actuall_mailsent = number_of_emails_sent[Sent_rows]
        query = ((number_of_days_to_warmup[Sent_rows])*(len(recipient_file)))
        if (number_of_emails_sent[Sent_rows]) <= (query):
            logger.info("Logging into {0}--for sending mail".format(
                sender_mail_address[Sent_rows]))
            schedule_logger.info("Logging into {0}--for sending mail".format(
                sender_mail_address[Sent_rows]))
            msg = EmailMessage()
            msg['From'] = sender_mail_address[Sent_rows]
            if sender_mail_type[Sent_rows] == 'gmail':
                try:
                    server = smtplib.SMTP_SSL(
                        'smtp.gmail.com', 465)
                    time.sleep(random_time)
                    server.login(
                        (msg['From']), sender_app_pass_phrase[Sent_rows])
                    time.sleep(random_time)
                    logger.info("{}--is got logged in".format(msg['From']))
                    schedule_logger.info(
                        "{}--is got logged in".format(msg['From']))

                except Exception as password_error_gamil:
                    logger.error(
                        "{}---password error and error is ---{}".format((msg['From']), password_error_gamil))
                    schedule_logger.error(
                        "{}---password error and error is ---{}".format((msg['From']), password_error_gamil))
                    mail_shoot_up(subject='Mailing flow error description',
                                  body="{}---password error and error is ---{}".format((msg['From']), password_error_gamil))

            elif sender_mail_type[Sent_rows] == 'outlook':
                try:
                    server = smtplib.SMTP('smtp.office365.com', 587)
                    server.starttls()
                    time.sleep(random_time)
                    server.login(msg["From"], sender_password[Sent_rows])
                    time.sleep(random_time)
                    logger.info(
                        "{}--is got logged in".format(msg['From']))
                    schedule_logger.info(
                        "{}--is got logged in".format(msg['From']))
                except Exception as password_error_outlook:
                    logger.error(
                        "{}---password error and error is ---{}".format((msg['From']), password_error_outlook))
                    schedule_logger.error(
                        "{}---password error and error is ---{}".format((msg['From']), password_error_outlook))
                    mail_shoot_up(subject="Mailing flow error description", body="{}---password error and error is ---{}".format(
                        (msg['From']), password_error_outlook))
            elif sender_mail_type[Sent_rows] == 'other_email':
                try:
                    try:
                    #     #     f'This is-------{sender_host_name[Sent_rows]} , {sender_port_number[Sent_rows]}')
                    #     try:
                    #         server = smtplib.SMTP(
                    #             sender_host_name[Sent_rows], sender_port_number[Sent_rows])
                    #     except:
                        server = smtplib.SMTP_SSL(
                            sender_host_name[Sent_rows], sender_port_number[Sent_rows])
                        try:
                            server.starttls()
                        except:
                            pass
                        server.login(
                            msg["From"], sender_password[Sent_rows])
                        time.sleep(random_time)
                        logger.info(
                            "{}--is got logged in".format(msg['From']))
                        schedule_logger.info(
                            "{}--is got logged in".format(msg['From']))
                    except:
                        server = smtplib.SMTP_SSL(
                            sender_host_name[Sent_rows], sender_port_number[Sent_rows])
                        # try:
                        #     server = smtplib.SMTP(
                        #         sender_host_name[Sent_rows], sender_port_number[Sent_rows])
                        # except:
                        
                        try:
                            server.starttls()
                        except:
                            pass
                        server.login(
                            msg["From"], sender_app_pass_phrase[Sent_rows])
                        time.sleep(random_time)
                        logger.info(
                            "{}--is got logged in".format(msg['From']))
                        schedule_logger.info(
                            "{}--is got logged in".format(msg['From']))
                except Exception as password_error_other:
                    logger.error(
                        "{}---password error and error is ---{}".format((msg['From']), password_error_other))
                    schedule_logger.error(
                        "{}---password error and error is ---{}".format((msg['From']), password_error_other))
                    mail_shoot_up(subject='Mailing flow error description', body="{}---password error and error is ---{}".format(
                        (msg['From']), password_error_other))
            else:
                logger.error(
                    "{}--This id is facing some issue".format(msg['From']))
                schedule_logger.error(
                    "{}--This id is facing some issue".format(msg['From']))
                mail_shoot_up(subject='Mailing flow error description',
                              body="{}--This id type is not mentioned in our data".format(msg['From']))
                continue
            try:
                for js in recipeint_mail_address:
                    # if recipeint_email_type[js] == 'gmail' or recipeint_email_type[js] == 'outlook' or recipeint_email_type[js] == 'other':
                    msg = EmailMessage()
                    msg['From'] = sender_mail_address[Sent_rows]
                    msg.set_content(random.choice(message))
                    msg['Subject'] = random.choice(subject)
                    msg["To"] = js
                    time.sleep(random_time)
                    server.send_message(msg)
                    time.sleep(random.uniform(25,35))
                    actuall_mailsent += 1
                    logger.info(
                        "actual mail sent this is for for loop--{}".format(actuall_mailsent))
                    schedule_logger.info(
                        "actual mail sent this is for for loop--{}".format(actuall_mailsent))

                server.quit()
                time.sleep(random_time)
                logger.info("Total mails sent ---{}".format(actuall_mailsent))
                schedule_logger.info(
                    "Total mails sent ---{}".format(actuall_mailsent))
                try:
                    # QUERY = f"update email_warmup_emailimprovement set number_of_emails_sent={actuall_mailsent} where id = {sender_file['id'][Sent_rows]}"
                    QUERY = """ UPDATE "email_warmup_emailimprovement" SET "number_of_emails_sent"='%s' WHERE "email_warmup_emailimprovement"."id"='%s'
                                                                        """ % (actuall_mailsent, sender_file['id'][Sent_rows])
                    cursor.execute(QUERY)
                    # conn.commit()
                except Exception as updation_error:
                    logger.error("Exception: ".format(updation_error))
                    schedule_logger.error("Exception: ".format(updation_error))
                    mail_shoot_up(subject='Mailing flow error description',
                                  body=f"while updating mailsent value for {msg['From']} an error occurred and the error is --{updation_error}")

            except Exception as mail_sending_internal_error:
                logger.error(
                    "This --{1}-- for this email error we got is---{0}".format((mail_sending_internal_error), (msg['From'])))
                schedule_logger.error(
                    "This --{1}-- for this email error we got is---{0}".format((mail_sending_internal_error), (msg['From'])))
                mail_shoot_up(subject='Mailing flow error description',
                              body="This --{1}-- for this email error we got is---{0}".format((mail_sending_internal_error), (msg['From'])))
                continue
        else:
            logger.info("This--- {} mail Domain is warmedup Successfully".format((sender_mail_address[Sent_rows])),
                        )
            schedule_logger.info("This--- {} mail Domain is warmedup Successfully".format((sender_mail_address[Sent_rows])),
                                 )
            mail_shoot_up(
                subject="Email improvement status", body=f"{sender_mail_address[Sent_rows]} mail Domain is warmedup Successfully,please check...")


def SMTP_mailing_job():
    try:
        Vpn_starter()
        time.sleep(60)
        ip_status_check = Ip_address_checker()
        if ip_status_check == "ip_not_changed":
            schedule_logger.error("Ip didn't changed please check vpn once")
            logger.error("Ip didn't changed please check vpn once")
            mail_shoot_up(subject="Mailing flow error description",
                          body="Ip didn't changed please check vpn once")
        mailing_object = DataReader()
        mailing_object.temporary_recipient_table_creater()
        cursor = mailing_object.cursor
        sender_file = mailing_object.sender_file
        mailing_object.parameters_definder_function()
        sender_mail_type = mailing_object.sender_mail_type
        sender_mail_address = mailing_object.sender_mail_address
        sender_password = mailing_object.sender_password
        sender_app_pass_phrase = mailing_object.sender_app_pass_phrase
        number_of_emails_sent = mailing_object.number_of_emails_sent
        number_of_days_to_warmup = mailing_object.number_of_days_to_warmup
        subject = mailing_object.subject
        message = mailing_object.message
        sender_port_number = mailing_object.sender_port_number
        sender_host_name = mailing_object.sender_host_name

        mailing_object.recipient_details()
        recipient_file = mailing_object.recipient_file
        recipeint_mail_address = mailing_object.recipeint_mail_address

        schedule_logger.info(
            "SMTP_mailing_flow is started at ---{0} and system time is  --{1}".format(mailing_object.mailing_time_value, datetime.now() + timedelta()))
        logger.info(
            "SMTP_mailing_flow is started at ---{0} and system time is  --{1}".format(mailing_object.mailing_time_value, datetime.now() + timedelta()))
        start_SMTP_mailing(cursor,
                           sender_file,
                           sender_mail_type,
                           sender_mail_address,
                           sender_password,
                           sender_app_pass_phrase,
                           number_of_emails_sent,
                           number_of_days_to_warmup,
                           recipient_file,
                           recipeint_mail_address,
                           subject,
                           message,
                           sender_port_number,
                           sender_host_name)
        Vpn_quiter()
        time.sleep(30)
        ip_status_check = Ip_address_checker()
        schedule_logger.info(
            "SMTP_mailing_flow completed at ----{}".format(datetime.now() + timedelta()))
        logger.info(
            "SMTP_mailing_flow completed at ----{}".format(datetime.now() + timedelta()))
    except Exception as main_mailing_error:
        logger.error(
            f"Got an main error in mailing_flow and the error is {main_mailing_error}")

        schedule_logger.error(
            f"Got an main error in mailing_flow and the error is {main_mailing_error}")

        mail_shoot_up(
            subject="Mailing flow error description", body=f"Got an main error in mailing_flow and the error is {main_mailing_error}")
        Vpn_quiter()
        time.sleep(30)
        ip_status_check = Ip_address_checker()
