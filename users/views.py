from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UpdateUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def createUser(request):
    page = True
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User was successfully created!.")
            return redirect('login')
       
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'register-login.html', context)


def deleteUser(request):
    profile = request.user.profile
    notifications = profile.notifications.filter(read=False).order_by("-created")
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Account was successfully deleted')
        return redirect('login')
    context = {
        'notifications': notifications
    }
    return render(request, 'delete-user.html', context)
    
    




def userAccount(request):
    profile = request.user.profile
    notifications = profile.notification.filter(read=False).order_by("-created")
    tasks = profile.tasks.filter(completed=True)
    context = {
        'profile':profile,
        'tasks': tasks
    }
    
    context = {
        'notifications': notifications
    }
    return render(request, 'user-account.html', context)


def updateUserProfile(request):
    profile = request.user.profile
    notifications = profile.notification.filter(read=False).order_by("-created")
    form = UpdateUserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateUserProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Profile was successfully updated.")
            return redirect('user-account')
    context = {
        'form': form,
        'notifications': notifications
    }
    return render(request, 'user-update-form.html', context)
    
    
    
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        
        else:
             messages.warning(request, "Invalid Username or Password.")
    return render(request, 'register-login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logout.")
    return redirect('login')