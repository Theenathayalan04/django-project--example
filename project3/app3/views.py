from django.shortcuts import render
from app3.forms import UserProfileInfoForm,UserForm
# Create your views here.



#login

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
def index(request):
    return render(request,'app3/index.html')


#login
@login_required
def special(request):
    return HttpResponse("you are logged in , awasome")




@login_required    #decoredor called
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered=False

    if  request.method=="POST":

        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid()  and profile_form.is_valid():

            user=user_form.save()
            #user.set_password(user.password)
            user.set_password(request.POST['password'])

            user.save()



            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic'  in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()



            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    
    return render(request,'app3/regeistration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})





#login 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))  # Redirect to a index after login
            else:
                return HttpResponse("account not active")
        else:
            print("some one tried invalid login!")
            print("username:{} and password {}".format(username,password))
            return HttpResponse("Invalid login")
    else:
        return render(request, 'app3/login.html',{})