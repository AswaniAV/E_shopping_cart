from django.shortcuts import render, redirect
from customer.models import Customer 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout  
from django.contrib import messages

def show_accounts(request):
    context = {}

    if request.method == 'POST' and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            address = request.POST.get('address')

            if User.objects.filter(username=username).exists():  
                raise ValueError("Username already exists")
            if User.objects.filter(email=email).exists():
                raise ValueError("Email already exists")   

            user = User.objects.create_user(username=username, email=email, password=password)
            customer = Customer.objects.create(name=username, user=user, phone=phone, address=address)
            success_message = "Registration successful. You can now log in."
            messages.success(request, success_message)

        except ValueError as e:
            messages.error(request, str(e))
        except Exception:
            messages.error(request, "An error occurred during registration")

    if 'login' in request.POST: 
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')  
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    
    return render(request, 'account.html', context) 

def logout(request):
    auth_logout(request)
    messages.info(request, 'Logout successfully')
    return redirect('show_accounts')


def cart(request):
    return render(request,'cart.html')