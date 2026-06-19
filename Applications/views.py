from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

def home_view(request):
    return render(request, 'Applications/home.html')




def connect_gmail(request):
    client_id = os.environ.get('GOOGLE_CLIENT_ID')
    redirect_uri = "http://127.0.0.1:8000/oauth2callback/"
    scope = "https://www.googleapis.com/auth/gmail.readonly"
    response_type = "code"
    google_auth_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': scope,
        'response_type': response_type,
        'access_type': 'offline', # Optional: Forces Google to give a refresh_token
        'prompt': 'consent'       # Optional: Guarantees consent screen triggers
    }

    url_args = urllib.parse.urlencode(params)
    auth_url = f"{google_auth_base_url}?{url_args}"
    return redirect(auth_url)