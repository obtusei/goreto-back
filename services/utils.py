import datetime
from email.message import EmailMessage
from smtplib import SMTPDataError, SMTPException, SMTPRecipientsRefused
from django.http import BadHeaderError, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.html import strip_tags
import secrets
import json
# from recomendation.models import User
# from .models import Otp


# def send_otp(request):
def send_email(receiver_email, issue):
    subject = "ISSUE REPORT"
    message = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Issue Details</title>

    </head>
    <body>
        <div class="container">
            <h1>Issue Details</h1>
            <div class="issue-card">
                <h2>Issue Reported By { issue.user.username }</h2>
                <p><strong>Coordinate:</strong> Latitude: { issue.latitude }  Longitude: { issue.longitude } </p>
            <strong> Will be replaced by map UI </strong> 
                <br/> <br/> 
                <p><strong>Trail:</strong> { issue.trail.name }</p>
                <p><strong>Problem Description:</strong></p>
                <p>{ issue.problem }</p>
                <p><strong>Reported At:</strong> { issue.created_at }</p>
            </div>
        </div>
    </body>
    </html>
    """
    message_plain = f"""
            Issue Reported By { issue.user.username }

            Coordinate: Latitude: { issue.latitude }  Longitude: { issue.longitude } 

            Trail: { issue.trail.name }

            Problem Description: { issue.problem }
            
            Reported At:  { issue.created_at }
    """
    sender = "rajukarki467@gmail.com"
    receivers = [receiver_email]

    # send email
    result = send_mail(
        from_email=sender,
        subject=subject,
        message=message_plain,
        recipient_list=receivers,

        # html_message=strip_tags(message),
        fail_silently=False,

    )
    if (result):
        # Save OTP
        # Otp.objects.create(token=otp, userid=user, createdat=datetime.datetime.now())
        # return JsonResponse({'message':'Email sent'})
        return 'Email Sent'

    return 'Failed to Sent'

    # return JsonResponse({'message':'OTP not Sent'},status=500)
# send_email()
