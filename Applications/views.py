from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import urllib.parse
import os
import requests
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


def oauth2callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponse("Error", status = 400)
    
    token_url = "https://oauth2.googleapis.com/token"

    payload = {
        'code': code,
        'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
        'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
        'redirect_uri': "http://127.0.0.1:8000/oauth2callback/",
        'grant_type': 'authorization_code',

    }
    response = requests.post(token_url, data = payload)

    if response.status_code != 200:
        # 
        # return JsonResponse(token_data)
        return HttpResponse(f"Failure Occured{response.status_code}", status= response.status_code)
   
   
    token_data = response.json()
    access_token = token_data.get('access_token')

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
    }
    gmail_uri = "https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=10"

    gmail_response = requests.get(gmail_uri, headers=headers)

    if gmail_response.status_code == 200:
        email_list = gmail_response.json()
        message = email_list.get('messages', [])
        first_message_id = message[0]['id']
        msg_url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{first_message_id}"
        msg_response = requests.get(msg_url, headers=headers)
        if msg_response.status_code == 200:
            return JsonResponse(msg_response.json())
    else:
        return HttpResponse("Oops something is not working!")