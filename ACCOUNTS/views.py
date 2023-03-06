from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def SignUpPage(request):
    return render(request, 'SignUp.html')

def userHome(request):
    id = request.user.id
    #print(id)
    address = ADDRESS.objects.filter(uid=id)
    # for i in address:
    #     print(i.city)
    #return render(request, 'userHome.html', {'address': address})
    return render(request, 'userHome.html', locals())

def adminHome(request):
    return render(request, 'adminHome.html')

def staffHome(request):
    return render(request, 'staffHome.html')

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff == 1:
                if user.is_superuser == 1:
                    auth.login(request, user)
                    return redirect('adminHome')
                else:
                    auth.login(request, user)
                    return redirect('staffHome')
            else:
                auth.login(request, user)

                return redirect('userHome')
        else:
            return render(request, 'SignUp.html', {'error': "Invalid Credential"})

def signupView(request):
    if request.method == "POST":
        fname = request.POST.get('fname').title()
        lname = request.POST.get('lname').title()
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # for address table
        city = request.POST.get('city').title()
        lmark = request.POST.get('lmark').title()
        district = request.POST.get('district').title()
        state = request.POST.get('state').title()
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')

        if password == cpassword:
            try:
                User.objects.get(username=email)
                return render(request, 'Signup.html', {'error': 'Username already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email,
                                                username=email, password=password, is_staff=0,
                                                is_superuser=0)
                user.save()

                uid = user.id

                address = ADDRESS.objects.create(uid=uid, image=image, city=city, land_mark=lmark,
                                                 district=district, state=state, pin_code=pin, phone=phone)
                address.save()
                auth.login(request, user)
                return redirect(userHome)
        else:
            return render(request, 'SignUp.html', {'error': 'Password mismatch'})
    else:
        return render(request, 'SignUp.html')




def LogoutView(request):
    logout(request)
    return redirect(index)


# profile

def profile(request):
    id = request.user.id
    address = ADDRESS.objects.filter(uid=id)
    return render(request, 'profile.html', {'address': address})

def profileUpdate(request):
    id = request.user.id
    address = ADDRESS.objects.filter(uid=id)
    return render(request, 'profile-update.html', locals())

def updateMyProfile(request):
    if request.method == "POST":
        id = request.user.id
        fname = request.POST.get('fname')
        lanem = request.POST.get('lname')
        city = request.POST.get('city')
        state = request.POST.get('state')
        district = request.POST.get('district')
        lmark = request.POST.get('lmark')
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        ADDRESS.objects.filter(uid=id).update(city=city, land_mark=lmark, district=district,
                                              state=state, pin_code=pin, phone=phone)
        User.objects.filter(id=id).update(first_name=fname, last_name=lanem, email=email,
                                          username=email)
        return redirect('profile')
    else:
        return redirect('profileUpdate')



