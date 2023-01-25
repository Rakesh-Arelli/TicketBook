from django.shortcuts import render,HttpResponseRedirect
from .forms import Ticket
from .models import User
# Create your views here.
def testview(request):
    return render(request,'base.html')


def add_ticket(request):
    if request.method == 'POST':
        formobj = Ticket(request.POST)
        if formobj.is_valid():
            nm = formobj.cleaned_data["name"]
            sn = formobj.cleaned_data["sNumber"]
            em = formobj.cleaned_data["email"]
            img = formobj.cleaned_data["image"]
            pri = formobj.cleaned_data["price"]
            pw = formobj.cleaned_data["password"]
            a=User(name=nm,sNumber=sn,image=img,price=pri,email=em,password=pw)
            a.save()
            formobj = Ticket()
    else:
        formobj = Ticket()
    gro = User.objects.all()
    return render(request,'home.html',{'form':formobj})


def update_ticket(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        formobj = Ticket(request.POST,instance=pi)
        if formobj.is_valid():
            formobj.save()
    else:
        pi = User.objects.get(pk=id)
        formobj = Ticket(instance=pi)
    return render(request,'update.html',{'form' : formobj})



def delete_ticket(request,id):
    if request.method == 'GET':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def add_contactus(request):
    if request.POST:
        fm=formContact(request.POST or None)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
       #     phno=fm.cleaned_data['phoneno']

            modleObj=ContactUs(name=name,email=email,phoneno=phno
                               ,desc=desc)
            modleObj.save()
            fm=formContact()
    else:
        fm = formContact()
    data = ContactUs.objects.all()
    return render(request,'ItemDetails/contactUs.html',{"form":fm,"data":data})
#
#
# def update_contactus(request,id):
#     if request.method == 'POST':
#         obj=ContactUs.objects.get(pk=id)
#         fm=formContact(request.POST,instance=obj)
#         if fm.is_valid():
#             fm.save()
#     else:
#         obj = ContactUs.objects.get(pk=id)
#         fm = formContact(instance=obj)
#     return render(request,'ItemDetails/contactUpdate.html',{'form':fm})
#
#
# def delete_contactus(request,id):
#     if request.method == 'POST':
#         pi = ContactUs.objects.get(pk=id)
#         pi.delete()
#        return HttpResponseRedirect('/')