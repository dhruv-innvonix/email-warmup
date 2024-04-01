try:
    from utility import encryption_util
    from utility.encryption_util import decrypt
except Exception as k:
    from .utility import encryption_util
    from .utility.encryption_util import decrypt
from email.message import EmailMessage
import smtplib
import requests
import subprocess
from datetime import datetime, date, timedelta
import random
from dotenv import load_dotenv
import warnings
import sys
import os
import time
import platform
import pandas as pd
import psycopg2 as pg
import logging
logger = logging.getLogger('django')
sys.path.append("/home/shiva/NewProjects3/email-warmup-tool")
warnings.filterwarnings('ignore')
load_dotenv()
today_time = date.today()
random_time = random.uniform(5, 7)
# Creating  and configuring logger for scheduling.py file whenever python file runs logs will be saved in this
logging.basicConfig(filename='./logs/python_sheduler.log',
                    format="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                    filemode='a')
schedule_logger = logging.getLogger("python_sheduler")
schedule_logger.setLevel(logging.DEBUG)

current_directory = os.path.dirname(os.path.abspath(__file__))

class DataReader:
    def __init__(self):
        self.gmail_and_outlook_pickup_value = 1
        self.other_email_pickup_value = 1
        self.conn = self.DataBase_Connector()
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True

    def DataBase_Connector(self):
        """ Connect to the PostgreSQL database server """
        engine = None
        try:

            try:
                # if django api runs
                from mailer import settings
                from mailer.settings import DATABASES
                dbHost = settings.DATABASES['default']['HOST']
                dbUsername = settings.DATABASES['default']['USER']
                dbPassword = settings.DATABASES['default']['PASSWORD']
                dbName = settings.DATABASES['default']['NAME']
                engine = pg.connect(
                    f'dbname={dbName} user={dbUsername} host={dbHost} password={dbPassword}')
            except Exception as e:
                # if python shedule runs
                DB_name = os.getenv('NAME')
                DB_user = os.getenv('pg_user')
                DB_host = os.getenv('HOST')
                DB_password = os.getenv('PASSWORD')
                engine = pg.connect(
                    f"dbname={DB_name} user={DB_user} host={DB_host} password={DB_password}")
        except (Exception, pg.DatabaseError) as error:
            logger.info(error)
            sys.exit(1)
        logger.info("Connection successful")
        return engine

    def fetching_DB_Tables(self):
        self.sender_file = pd.read_sql(
            'select * from "email_warmup_emailimprovement"', con=self.conn)
        # sender_file.reset_index(drop=True, inplace=True)
        self.gmail_recipient_file = pd.read_sql(
            'select * from "email_warmup_gmailrecipient"', con=self.conn)
        self.outlook_recipient_file = pd.read_sql(
            'select * from "email_warmup_outlookrecipient"', con=self.conn)
        self.other_email_recipient_file = pd.read_sql(
            'select * from "email_warmup_otherrecipient"', con=self.conn)
        self.replies_file = pd.read_sql(
            'select * from "email_warmup_reply"', con=self.conn)
        self.subject_file = pd.read_sql(
            'select * from "email_warmup_subject"', con=self.conn)
        self.messages_file = pd.read_sql(
            'select * from "email_warmup_message"', con=self.conn)
        self.timing_file = pd.read_sql(
            'select * from "email_warmup_timing"', con=self.conn)

    def merged_dataframe_creator(self):
        self.fetching_DB_Tables()
        try:
            try:
                self.gmail_dataframe = (self.gmail_recipient_file.assign(
                    email_type='gmail')).sample(self.gmail_and_outlook_pickup_value)
            except:
                self.gmail_dataframe=pd.DataFrame()
            try:
                self.outlook_dataframe = (self.outlook_recipient_file.assign(
                    email_type='outlook')).sample(self.gmail_and_outlook_pickup_value)
            except:
                self.outlook_dataframe = pd.DataFrame()
            try:
                self.other_emails_dataframe = (self.other_email_recipient_file.assign(
                    email_type='other_email')).sample(self.other_email_pickup_value)
            except:
                self.other_emails_dataframe = pd.DataFrame()
            self.merged_dataframe = [
                self.gmail_dataframe, self.outlook_dataframe, self.other_emails_dataframe]
            self.merged_dataframe = pd.concat(
                self.merged_dataframe, axis=0, ignore_index=True)
            # logger.info(f"this is data we get----{self.merged_dataframe}")
        except:
            logger.error(
                "data is not sufficient for sample mails")
            schedule_logger.error(
                "data is not sufficient for sample mails")
            mail_shoot_up(subject='Data error',
                          body="data is not sufficient for sample mails ")
            pass
        # return self.merged_dataframe

    def temporary_recipient_table_creater(self):
        self.merged_dataframe_creator()
        self.recipient_file = pd.read_sql(
            'select * from email_warmup_temporaryrecipient where today_email_sent= false', con=self.conn)
        if len(self.recipient_file) == 0:
            for row in self.merged_dataframe.index:
                query = "insert into email_warmup_temporaryrecipient (id,name,email,password,app_pass_phrase,smtp_port,smtp_host,today_email_sent,email_type,imap_port,imap_host) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                data_to_insert = (row, 
                                  self.merged_dataframe['name'][row], 
                                  self.merged_dataframe['email'][row], 
                                  self.merged_dataframe['password'][row],
                                  self.merged_dataframe['app_pass_phrase'][row],
                                  self.merged_dataframe['smtp_port'][row], 
                                  self.merged_dataframe['smtp_host'][row], 
                                  False, 
                                  self.merged_dataframe['email_type'][row], 
                                  self.merged_dataframe['imap_port'][row], 
                                  self.merged_dataframe['imap_host'][row])
                self.cursor.execute(query, data_to_insert)
                self.recipient_file = pd.read_sql(
                    'select * from email_warmup_temporaryrecipient where today_email_sent= false', con=self.conn)

    def recipient_details(self):
        self.recipient_file = pd.read_sql(
            'select * from email_warmup_temporaryrecipient where today_email_sent= false', con=self.conn)
        # self.temporary_recipient_table_creater()
        self.recipient_name = self.recipient_file['name']
        self.recipeint_mail_address = self.recipient_file['email']
        self.recipient_password = self.recipient_file['password'].apply(
            encryption_util.decrypt)
        self.recipient_app_pass_phrase = self.recipient_file['app_pass_phrase'].apply(
            encryption_util.decrypt)
        self.recipient_port = self.recipient_file['smtp_port']
        self.recipient_smtp_host = self.recipient_file['smtp_host']
        self.recipient_imap_host = self.recipient_file['imap_host']
        self.recipeint_email_type = self.recipient_file['email_type']
        self.recipeint_imap_port = self.recipient_file['imap_port']
        

    def parameters_definder_function(self):
        # timing_details
        self.mailing_time_value = (
            self.timing_file["mailing_time"]).to_string()[5:]
        self.reply_time_value = (
            self.timing_file["reply_time"]).to_string()[5:]
        # sender or user details
        self.sender_name = self.sender_file["name"]
        self.sender_mail_address = self.sender_file["email"]
        self.sender_password = self.sender_file["password"].apply(
            encryption_util.decrypt)
        self.sender_port_number = self.sender_file["smtp_port"]
        self.sender_host_name = self.sender_file["smtp_host"]
        self.number_of_days_to_warmup = self.sender_file["number_of_days_to_warmup"]
        self.sender_app_pass_phrase = self.sender_file["app_pass_phrase"].apply(
            encryption_util.decrypt)
        self.number_of_emails_sent = self.sender_file["number_of_emails_sent"]
        self.sender_mail_type = self.sender_file["email_type"]
        self.initial_mails = len(self.sender_file)
        # subjects
        self.subject = self.subject_file["subject"].tolist()
        # messages
        self.message = self.messages_file["message"].tolist()
        # replies
        self.reply_message = self.replies_file["message"]


def mail_shoot_up(subject, body):
    pass
    # mail_content = body
    # sender_address = 'siva.nidamanuri@innvonix.com'
    # sender_pass = '9L*WBo0D/m8GKy|_'
    # receiver_address = 'abhishek.innvonix@gmail.com'
    # message = EmailMessage()
    # message['From'] = sender_address
    # message['To'] = receiver_address
    # message.set_content(mail_content)
    # message['Subject'] = subject
    # session = smtplib.SMTP_SSL("cs2.bluehost.in", 465)
    # session.login(sender_address, sender_pass)
    # text = message.as_string()
    # session.sendmail(sender_address, receiver_address, text)
    # session.quit()


def os_checker():
    if platform.system() == "Windows":
        return "windows system"
    else:
        return "other system"


def Vpn_starter():
    username = "WLAvsVNko3D6V4z6"
    password = "seZvOzgml9bhb6p0UYWue1uaOgcbJp3k"
    system_type_checker = os_checker()
    if system_type_checker == "windows system":
        with open(r"C:\Users\Administrator\Desktop\vpn setup\credentials.txt", "w") as f:
            f.write(f"{username}\n{password}")
        subprocess.Popen(
            "openvpn --config us-windows-free-41.protonvpn.net.udp.ovpn --auth-user-pass credentials.txt", shell=True)
        schedule_logger.info("Activated VPN")
        logger.info("Activated VPN")

    else:
        # Construct the dynamic paths for the VPN configuration file and credentials file
        vpn_config_file = os.path.join(current_directory, 'us-linux-free-41.protonvpn.net.udp.ovpn')
        credentials_file = os.path.join(current_directory, 'credentials.txt')
        
        # with open(r"/home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/credentials.txt", "w") as f:
        # with open(r"/mnt/c/Users/kaush/Innvonix/email_warmup/email-warmup-tool/email_warmup/credentials.txt", "w") as f:    
        #     f.write(f"{username}\n{password}")

        with open(credentials_file, "w") as f:
            f.write(f"{username}\n{password}")

        # # subprocess.Popen('echo "invx@123" | sudo -S openvpn --config /home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/us-linux-free-41.protonvpn.net.udp.ovpn --auth-user-pass /home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/credentials.txt', shell=True)
        # subprocess.Popen('echo "invx@123" | sudo -S openvpn --config /mnt/c/Users/kaush/Innvonix/email_warmup/email-warmup-tool/email_warmup/us-linux-free-41.protonvpn.net.udp.ovpn --auth-user-pass /mnt/c/Users/kaush/Innvonix/email_warmup/email-warmup-tool/email_warmup/credentials.txt', shell=True)
        
        # Run the subprocess command with dynamic file paths
        command = f'openvpn --daemon --config {vpn_config_file} --auth-user-pass {credentials_file}'
        subprocess.Popen(command, shell=True)
        
        schedule_logger.info("Activated VPN")
        logger.info("Activated VPN")


def Ip_address_checker():
    original_ip = "103.106.20.183"
    ip_address_ckeck = requests.get("https://api.ipify.org").text
    if ip_address_ckeck != original_ip:
        schedule_logger.info(f"present ip address is---> {ip_address_ckeck}")
        logger.info(f"present ip address is---> {ip_address_ckeck}")
        return "ip_changed"
    else:
        schedule_logger.info(f"present ip address is---> {ip_address_ckeck}")
        logger.info(f"present ip address is---> {ip_address_ckeck}")
        return "ip_not_changed"


def Vpn_quiter():
    system_type_checker = os_checker()
    if system_type_checker == "windows system":
        subprocess.Popen(
            "taskkill.exe /F /IM openvpn.exe", shell=True)
        schedule_logger.info("Deactivated VPN")
        logger.info("Deactivated VPN")
        return "Windows Vpn_is_not_running"
    else:
        subprocess.Popen('pkill -9 openvpn', shell=True)
        schedule_logger.info("Deactivated VPN")
        logger.info("Deactivated VPN")
        return "Linux Vpn_is_not_running"
