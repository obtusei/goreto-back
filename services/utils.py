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
    message_plain = f"""
        There is a new alert that needs your attention:

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
        return {'isSuccess': True, 'message': 'Email Sent'}

    return {'isSuccess': False, 'message': 'Failed to Send'}

    # return JsonResponse({'message':'OTP not Sent'},status=500)
# send_email()
