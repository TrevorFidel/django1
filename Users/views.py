from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Index.html')
def aboutus(request):
    return render(request, 'Aboutus.html')
def register(request):
    return render(request, 'Register.html')
def login(request):
    return render(request, 'Login.html')
def contact(request):
    return render(request, 'Contacts.html')
def logout(request):
    return render(request, 'logout.html')
def gallery(request):
    return render(request, 'Gallery.html')


