
# Overview
This project comprises four APIs designed for managing sender emails, email status checks, SMTP flow, and email replies. Additionally, there are nine database tables in the models.py file to store various email-related information. The implementation also integrates the ProtonVPN service for secure communication.

*APIs*
### EmailImprovementRegistrationAPI
Purpose: Registers new accounts for sender emails.

### Email_improve_status_checkAPI
Purpose: Checks the status of the sender account.

### SMTP_flowAPI
Purpose: Sends emails to all recipient email addresses.

### SMTP_ReplierAPI
Purpose: Manages email replies and includes the following functions:
    *copy_mails_and_deleteing_mails*: Deletes emails from spam and adds them to the index.
    *todays_mails_collector*: Collects email information and returns it as a DataFrame.
    *Marking_as_read_and_favourite*: Reads emails and adds them to the favorites list.
    *todays_replier*: Sends replies to received emails.

*Database Tables (models.py)*

### emailimprovement
Purpose: Stores sender mail addresses.

### GmailRecipients
Purpose: Stores Gmail recipients' addresses.

### OtherRecipients
Purpose: Stores other recipients' addresses.

### OutlookRecipients
Purpose: Stores Outlook recipients' addresses.

### TemporaryRecipients
Purpose: Stores temporary email addresses.

### Message
Purpose: Stores the message content for emails.

### Subject
Purpose: Stores the subject lines for emails.

### Reply
Purpose: Stores reply messages for emails.

### Timing
Purpose: Stores timestamps for email scheduling.

*Integration: ProtonVPN Service*
Purpose: Implements ProtonVPN service for secure communication within the project.