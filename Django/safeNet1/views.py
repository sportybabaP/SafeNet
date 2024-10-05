

# myapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
def home(request):
    return HttpResponse("Homepage")

def about(request):
    return HttpResponse("About")

def services(request):
    return HttpResponse("Services")

def contact(request):
    return HttpResponse("contact")

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Here you can handle the form data
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            mobile_number = form.cleaned_data['mobile_number']
            confirm_contact = form.cleaned_data['confirm_contact']
            email = form.cleaned_data['email']
            confirm_email = form.cleaned_data['confirm_email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # You can add further validation (e.g., check if emails match, etc.)
            # And then save the user to the database, send a welcome email, etc.
            if email == confirm_email and password == confirm_password and mobile_number == confirm_contact:
                # Create a user or process the data as needed
                return redirect('success')  # Redirect to a success page after sign-up
            else:
                form.add_error(None, "Email/Password or contact number mismatch.")
    else:
        form = SignUpForm()

    return render(request, 'sign_up.html', {'form': form})

