from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from main.views import home_page_view
from .forms import NewUserForm

def login_view(request):
    """
    login view has 2 requests, one is the get method and when it happens:
            then we will render the form
        the second one when the post request happens
            then we will pass the data 
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('the authinticated user is: ', user)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect(home_page_view)
            else:
                # if the user not saved in the database then the user should create 
                # a new account (register)
                # then redirect him/her into login page
                messages.error(request, 'unfortunatly we cant see ur name with us try to register')
        else:
          messages.error(request, 'unfortunatly we cant see u with us')  
    elif request.method == 'GET':
        login_form = AuthenticationForm
    return render(request, 'views/login.html', {'login_form': login_form})

def register_view(request):
    register_form = NewUserForm()
    if request.method == 'POST':
       register_form = NewUserForm(request.POST)
       if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, 'Registration is successfully')
            return redirect(home_page_view)
    form = NewUserForm()
    return render(request, 'views/register.html', {'register_form':register_form})

# another way to create views based on class
class RegisterView(View):

    def get(self, request):
        """
        method to handle the get request in class based view
        """
        register_form = NewUserForm()
        return render(request, 'views/register.html', {'register_form':register_form})
    
    def post(self, request):
        # register_form = UserCreationForm(data=request.POST) # initialize register form in post method
        register_form = NewUserForm(request.POST)
        if register_form.is_valid(): # if the form is valid (data is correct)
            user = register_form.save() # then save the user into database
            user.refresh_from_db() # to get the current data for the user that saved
            login(request, user) # then login the user
            messages.success(request, f'user {user.username} registered successfully') # print a success message
            return redirect(home_page_view)

        else:
            messages.error(request, 'unfortunatly, error happen when register')
            return render(request, 'views/register.html', {'register_form':register_form})
