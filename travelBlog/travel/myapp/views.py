from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import UserData

# Create your views here.
def user_dat(request):
    user = UserData.objects.all().values()
    template = loader.get_template('user_data.html')
    context = {
'myuser': user,
}
    return HttpResponse(template.render(context, request))


def index(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        #print("first_name is",firstname)
        lastname = request.POST.get('lastname')
        #print("lastname is",lastname)
        email = request.POST.get('email')
        #print("email is",email)
        subject = request.POST.get('subject')
        #print("subject is",subject)
        description= request.POST.get('description')
        #print("description is",description)
        regis=UserData.objects.create(firstname=firstname,lastname=lastname,email=email,subject=subject,description=description)
        print(regis)
        return redirect('user_data')
    return render(request,'index.html')