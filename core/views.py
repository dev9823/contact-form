from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact

class ContactView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        name = request.data.get('name')
        subject = request.data.get('subject')
        message = request.data.get('message')

        contact = Contact.objects.create(
            email=email,
            name=name,
            subject=subject,
            message=message
        )
        
        email_message = f"Name: {name}\nEmail: {email}\n\n{message}"
        
        send_mail(
            subject=subject,
            message=email_message,
            from_email=email,
            recipient_list=['eyobabdellasharo@gmail.com'],
        )

        return Response({'detail': 'Email created successfully'}, status=status.HTTP_201_CREATED)