# homepage/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Cre_Acc, publish_ride
from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cre_Acc

def home(request):
    return render(request, 'homepage/home.html')

def passenger_page(request):
    return render(request, 'homepage/passenger.html')

def driver_page(request):
    return render(request, 'homepage/driver.html')



def register_page(request):
    if request.method == 'POST':
        # Retrieve form data
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        mobilenumber = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        
        # Check if mobile number or email already exist
        if Cre_Acc.objects.filter(mobilenumber=mobilenumber).exists():
            messages.error(request, "Mobile number already exists")
            return redirect('register_page')
        elif Cre_Acc.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register_page')
             
        # Save additional user details to Cre_Acc model
        cre_acc = Cre_Acc(firstname=firstname, lastname=lastname,
                          mobilenumber=mobilenumber, email=email,
                          password=password, username=username)
        cre_acc.save()
        
        messages.success(request, "Account created successfully")
        return render(request, "homepage/home.html")
    
    return render(request, "homepage/register.html")


def login_page(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # If the user credentials are correct, log in the user
            login(request, user)
            # Redirect to the login attributes page
            return redirect('login_attributes')
        else:
            # If the user credentials are incorrect, redirect back to the login page
            return redirect('login_page')

    # Render the login page template for GET requests
    return render(request, 'homepage/login.html')

def passenger_attributes(request):
    # Retrieve and process the data submitted on the register page (form data)
    # Save the data to the database (optional)

    # Render the passenger attributes page
    return render(request, 'homepage/passenger_attributes.html')

def login_attributes(request):
    # Retrieve and process the data submitted on the login page (form data)
    # Save the data to the database (optional)

    # Render the login attributes page
    return render(request, 'homepage/login_attributes.html')

def login_check(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
    

        # Redirect to the login attributes page
        return redirect('login_attributes')

    # Redirect back to the login page if accessed via GET request
    return redirect('login_page')

def bookings_page(request):
    return render(request, 'homepage/bookings.html')

def ride_history_page(request):
    return render(request, 'homepage/ride_history.html')

def profile_page(request):
    if request.method == 'POST':
        # Check if the user clicked "Yes" (edit_profile_page) or "No" (login_attributes)
        selection = request.POST.get('selection')

        if selection == 'yes':
            return redirect('edit_profile_page')
        elif selection == 'no':
            return redirect('login_attributes')

    return render(request, 'homepage/profile.html')

def edit_profile_page(request):
    return render(request, 'homepage/edit_profile.html')

def logout_user(request):
    logout(request)
    return redirect('passenger_attributes')

def features_page(request):
    return render(request, 'homepage/features.html')

def pricing_page(request):
    return render(request, 'homepage/pricing.html')

def notifications_page(request):
    return render(request, 'homepage/notifications.html')

def help_and_support_page(request):
    return render(request, 'homepage/help_and_support.html')

def terms_of_service_page(request):
    return render(request, 'homepage/terms_of_service.html')

def privacy_policy_page(request):
    return render(request, 'homepage/privacy_policy.html')

def about_us_page(request):
    return render(request, 'homepage/about_us.html')

def pricing_page(request):
    return render(request, 'homepage/pricing.html')

def disabled_attributes_page(request):
    return render(request, 'homepage/disabled_attributes.html')

def search_page(request):
    return render(request, 'homepage/search_page.html')

def filters_page(request):
    return render(request, 'homepage/filters_page.html')

def results_page(request):
    return render(request, 'homepage/results_page.html')

def book_ride_page(request):
    return render(request, 'homepage/book_ride_page.html')

def book_ride_attributes_page(request):
    return render(request, 'homepage/book_ride_attributes.html')

def driver_register_page(request):
    return render(request, 'homepage/driver_register.html')

def driver_login_page(request):
    return render(request, 'homepage/driver_login.html')

def driver_register_page(request):
    return render(request, 'homepage/driver_register.html')

def driver_attributes_page(request):
    return render(request, 'homepage/driver_attributes.html')

def driver_login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        return redirect('driver_attributes_page')  # Redirect to driver login page
    else:
        return redirect('driver_login_page')  # Redirect to driver login page
    
def vehicle_verification_page(request):
    return render(request, 'homepage/vehicle_verification.html')

def notifications_area_page(request):
    return render(request, 'homepage/notifications_area.html')

def conversations_panel_page(request):
    return render(request, 'homepage/conversations_panel.html')

def ride_management_page(request):
    return render(request, 'homepage/ride_management.html')

def manage_rides_page(request):
    # Implement the logic to display and manage rides
    return render(request, 'homepage/manage_rides.html')

def payment_details_page(request):
    # Implement the logic to display payment details
    return render(request, 'homepage/payment_details.html')

def reviews_ratings_page(request):
    # Implement the logic to display reviews and ratings
    return render(request, 'homepage/reviews_ratings.html')

def driver_analytics_page(request):
    # Implement the logic to display driver analytics
    return render(request, 'homepage/driver_analytics.html')