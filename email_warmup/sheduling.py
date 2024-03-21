from SMTP_mailing import *
from SMTP_replying import *
import schedule
from local_files_and_variables import *
print("started")

def data_reader_class_intiator():
    data_reader_object = DataReader()
    data_reader_object.fetching_DB_Tables()
    data_reader_object.parameters_definder_function()
    mailing_time_value = data_reader_object.mailing_time_value
    reply_time_value = data_reader_object.reply_time_value
    return {
        "mailing_time_value": mailing_time_value,
        "reply_time_value": reply_time_value
    }


timing_function = data_reader_class_intiator()
mailing_time_value = timing_function["mailing_time_value"]
reply_time_value = timing_function["reply_time_value"]
schedule.every().day.at(mailing_time_value).do(SMTP_mailing_job)
schedule.every().day.at(reply_time_value).do(SMTP_reply_flow_starter_job)

while True:
    schedule.run_pending()
    time.sleep(3)
