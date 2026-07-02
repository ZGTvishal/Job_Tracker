from django.utils import timezone
from email.utils import parseaddr
from ..models import Application

def email_processor(email_data: dict):
    
    company_key = email_data['sender_email'].split('@')[-1].strip()
    company_name = company_key.split('.')[0].strip()
    role_title = email_data["role_title"]
    snippet = email_data['snippet']

    if 'thank you for your application' in snippet.lower():
        status = 'applied'
    elif 'interview' or 'assessment' in snippet.lower():
        status = 'interview'
    elif 'unfortunately' or 'regret' in snippet.lower():
        status = 'rejected'
    elif 'offer' or 'congratulations' in snippet.lower():
        status = 'offer'
    else:
        status = 'applied'
    
    email_data['status'] = status


    return email_data 


