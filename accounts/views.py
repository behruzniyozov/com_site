from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, UserResetPasswordForm

import requests
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login

import uuid
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Optional: deactivate until email confirmed
            user.save()

            # Generate a simple token (you can store it or encode user id)
            token = str(uuid.uuid4())

            # Compose verification link (adjust domain & URL as needed)
            verification_link = request.build_absolute_uri(f'/verify-email/?token={token}')

            # Send email
            send_mail(
                'Verify your email',
                f'Click this link to verify your email: {verification_link}',
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )

            # Store or associate the token with user to verify later
            # (This part needs implementation: e.g. save token in DB)

            return redirect('email_sent')  # Redirect to “check your email” page
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = UserResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Here you would typically send a password reset email
            # For simplicity, we just redirect to a success page
            return redirect('password_reset_done')  # Redirect after processing
    else:
        form = UserResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})
