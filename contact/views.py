from django.shortcuts import render
from .models import Info
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_message(request):
    myinfo = Info.objects.first()
    

    if request.method == 'POST':
        myform = EmailForm(request.POST)
        if myform.is_valid():

            subject = request.POST['subject']
            email = request.POST['email']
            message = request.POST['message']
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )

    else:
        myform = EmailForm()

    context = {
        'myinfo':myinfo,
        'form':myform,
    }
    return render(request,'contact.html',context)