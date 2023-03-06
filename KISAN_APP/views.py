from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import *
from ACCOUNTS.views import *
from ACCOUNTS.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# About Us
def AboutUs(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'services.html')

def Schemes(request):
    return render(request, 'schemes.html')

def Administration_Details(request):
    return render(request, 'admin-details.html')

def ContactUs(request):
    return render(request, 'contact.html')

def PrivacyPolicy(request):
    return render(request, 'privacy-policy.html')


# KRISHIBHAVAN LIST

def krishibhavanList(request):

    krishibhavan = KRISHIBHAVAN.objects.all()

    return render(request, 'krishibhavanlist.html',locals())


# addKrishibhavan

def addKrishibhavan(request):
    return render(request, 'addKrishibhavan.html')

def KrishibhavanRegistration(request):
    if request.method == "POST":
        place = request.POST.get('Place')
        municipality = request.POST.get('Municipality')
        Panchayath = request.POST.get('Panchayath')
        District = request.POST.get('District')
        State = request.POST.get('State')
        Country = request.POST.get('Country')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        image = request.FILES.get('image')

        import random

        lower = chr(random.randint(ord('a'),ord('z')))
        upper = chr(random.randint(ord('A'),ord('Z')))

        ecode = 'ekisan' + lower + upper
        try:
            User.objects.get(username=email)
            return render(request, 'addKrishibhavan.html', {'error': 'Username already exist'})
        except User.DoesNotExist:
            user = User.objects.create_user(email=email,username=email, password=ecode,
                                            is_staff=1,is_superuser=0)
            user.save()
            uid = user.id
            krishibhavan = KRISHIBHAVAN.objects.create(uid = uid,image=image, place=place,
                                                   municipality=municipality, panchayath=Panchayath,
                                                   district=District, state=State, country=Country,
                                                   pin_code=pincode, phone=Phone, email=email,  ecode=ecode)

            krishibhavan.save()



        return redirect(krishibhavanList)
    else:
        return render(request, 'addKrishibhavan.html')



def KrishibhavanMoreDetails(request,id):

    krishibhavan = KRISHIBHAVAN.objects.filter(uid=id)
    user_details = User.objects.filter(id=id)

    return render(request, 'KrishibhavanMoreDetails.html',locals())

def updateKrishibhavan(request,id):
    krishibhavan = KRISHIBHAVAN.objects.filter(uid=id)
    user_details = User.objects.filter(id=id)

    return render(request, 'Krishibhavan-Update.html', locals())


def Krishibhavan_delete(request,id):
    KRISHIBHAVAN.objects.filter(uid=id).delete()
    User.objects.filter(id=id).delete()
    return redirect(krishibhavanList)


# Krishibhavan Module - staff

# online services

def OnlineServices(request):
    services = ONLINE_SERVICES.objects.all()

    return render(request, 'onlineServices.html',locals())

def AddOnlineServices(request):
    return render(request, 'addOnlineServices.html')

def Add_NewOnlineServices(request):

    if request.method == "POST":
        service_name = request.POST.get('service_name')
        Description = request.POST.get('Description')
        Scheme = request.POST.get('Scheme')
        Eligibility = request.POST.get('Eligibility')
        apply = request.POST.get('apply')
        contactEnd = request.POST.get('contactEnd')
        apply_url = request.POST.get('apply_url')
        image = request.FILES.get('image')
        end_date = request.POST.get('end_date')
        id = request.user.id
        data = KRISHIBHAVAN.objects.filter(uid=id)
        for i in data:
            ecode = i.ecode
        new_service = ONLINE_SERVICES.objects.create(ecode=ecode,image=image,
                                                     ServiceName=service_name,
                                                     Description=Description,
                                                     Scheme=Scheme,
                                                     Eligibility=Eligibility,
                                                     How_To_Apply=apply,
                                                     Whom_To_Contact=contactEnd,
                                                     URL=apply_url,
                                                     Last_Date=end_date)
        new_service.save()
        return redirect(OnlineServices)
    else:
        return render(request, 'addOnlineServices.html')

def readMore_OnlineServices(request,id):

    data = ONLINE_SERVICES.objects.filter(id=id)
    return render(request, 'readMore_OnlineServices.html', locals())

def deleteOnlineServices(request,id):
    ONLINE_SERVICES.objects.filter(id=id).delete()
    return redirect(OnlineServices)


# User

# scheme details

def user_SchemeDetails(request):
    id = request.user.id
    address = ADDRESS.objects.filter(uid=id)
    services = ONLINE_SERVICES.objects.all()
    return render(request, 'user_SchemeDetails.html', locals())

def readMore_OnlineServices_user(request,id):
    uid = request.user.id
    address = ADDRESS.objects.filter(uid=uid)
    data = ONLINE_SERVICES.objects.filter(id=id)
    return render(request, 'readMore_OnlineServices_user.html', locals())

def Apply_Services_User(request,id):
    data = ONLINE_SERVICES.objects.filter(id=id)
    return render(request, 'Apply_Services_User.html', locals())

def Scheme_Application_Submit(request):

    if request.method == "POST":

        uid = request.user.id
        scheme_id = request.POST.get('scheme_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        aadhar = request.POST.get('aadhar')
        email = request.POST.get('email')
        area_code = request.POST.get('area_code')
        phone = request.POST.get('phone')
        village = request.POST.get('village')
        panchayath = request.POST.get('panchayath')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        kisan_card = request.POST.get('exist')
        try:
            SCHEME_APPLICATIONS.objects.get(Scheme_id=scheme_id)
            print("Exists already!")
            return redirect(userHome)
        except SCHEME_APPLICATIONS.DoesNotExist:
            new_application = SCHEME_APPLICATIONS.objects.create(uid=uid,
                                                                 Name=first_name + " " + last_name,
                                                                 Aadhar_No=aadhar,
                                                                 Email=email,
                                                                 Phone=area_code+" "+phone,
                                                                 Village=village,
                                                                 Panchayath=panchayath,
                                                                 District=district,
                                                                 pin_code=pincode,
                                                                 is_KisanCard=kisan_card,
                                                                 Scheme_id=scheme_id)
            new_application.save()

            text = "You have applied to the Scheme with Scheme Id : "+ scheme_id

            print(text)

            USER_NOTIFICATIONS.objects.create(user=request.user, read=False, text=text)



            return redirect(userHome)

    else:
        return redirect(Apply_Services_User)


# userside notifications


def User_Notifications(request):
    count = USER_NOTIFICATIONS.objects.filter(user=request.user, read=False).count()
    notifications = USER_NOTIFICATIONS.objects.filter(user=request.user).order_by('-id')
    return render(request, 'User_Notifications.html', {'notifications': notifications,
                                                  'user': request.user, 'count': count})


def MarkasRead(request, id):
    a = USER_NOTIFICATIONS.objects.get(id=id)
    a.read = True
    a.save()
    return redirect('User_Notifications')


# view all krishibhavan list

def User_KrishibhavanList(request):
    krishibhavan_list = KRISHIBHAVAN.objects.all()
    return render(request, 'User_KrishibhavanList.html', locals())

# kisan card details

def KisanCard(request):
    return render(request, 'KisanCard.html')

def KisanCardForm(request):
    return render(request, 'KisanCardForm.html')


def KisanCardApply(request):
    if request.method == "POST":
        uid = request.user.id
        fullname = request.POST.get("fullname")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        adar = request.POST.get("adar")
        pin = request.POST.get("pin")
        gender = request.POST.get("gender")

        return redirect(userHome)
    else:
        return redirect(KisanCardApply)