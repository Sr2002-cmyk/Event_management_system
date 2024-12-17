from django.shortcuts import render,redirect
from . models import Event,Booking
from .forms import BookingForm



def index(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def events(request):
    dict_event={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_event)

def contact(request):
    return render(request,'contact.html')

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)


def index(request):
    return render(request,'index.html')


 