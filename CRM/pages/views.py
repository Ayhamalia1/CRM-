from django.shortcuts import render
from django.shortcuts import get_object_or_404 ,redirect
from .models import CustomerService,Customer
from .forms import CreateCustomer,UpdateCustomer,loginForm,addServiceForm
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging
import datetime


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,'pages/index.html',{'data':Customer.objects.all()})
#get username

# Create Customer
@login_required(login_url='login')

def Create(request):
    form= CreateCustomer()
    if request.method=='POST':
         form=CreateCustomer(request.POST)
         if form.is_valid():
              form.save()
              return redirect('index')
    else:
     form= CreateCustomer()
    return render(request,'pages/create_customer.html',{'form':form})
@login_required(login_url='login')
#delete user
def deleteUser(request,id):
    user=get_object_or_404(Customer,id=id)
    user.delete()
    return redirect('index')
@login_required(login_url='login')

def updateUser(request,id):
     data=get_object_or_404(Customer,id=id)
     form=UpdateCustomer(instance=data) 
    #  put the data from recorde in form 
     if request.method=="POST":
      form =UpdateCustomer(request.POST ,instance=data)
      if form.is_valid():
          form.save()
          return redirect("index")
     return render(request,'pages/update.html',{"form":form})
@login_required(login_url='login')
def ShowServices(request, id):
    customer = get_object_or_404(Customer, id=id)
    services = CustomerService.objects.filter(customer=customer,end_date__isnull=True)

    if request.method == 'POST':
        form = addServiceForm(request.POST) 
        if form.is_valid():
            customer_service = form.save(commit=False)
            customer_service.customer = customer
            customer_service.save()
            return redirect('services', id=customer.id)
    else:
        form = addServiceForm()

    #stop service
    if request.method == 'POST':
        if 'stop_id' in request.POST:
            service_id = request.POST.get('stop_id')
            cs = get_object_or_404(CustomerService, id=service_id)
            cs.end_date = datetime.date.today()
            cs.save()
            return redirect('services', id=customer.id)

    return render(request, 'pages/services.html', {'form': form, 'services': services, 'customer': customer})






    # return render(request,"pages/service.html",{"servcies":servcies})
#Search
logger=logging.getLogger(__name__)
def Search(request):

    query=request.GET.get('query')
    result=[]
    try:
        result=Customer.objects.filter(Q(name__icontains=query) |Q(id__icontains=query))
    except Exception as e:    
        logger.error('Error: %s',e)
    return render(request,"pages/search.html",{"result":result ,'query':query})   

#Login 
def loginView(request):
    form=loginForm()
    if request.method=="POST":
       form=loginForm(request.POST)
       if form.is_valid():
           username=request.POST.get("username")
           password=request.POST.get("password")
           user = authenticate(request, username=username, password=password)
           if user is not None:
            login(request, user)  
            return redirect('index')
           else:
                form.add_error(None, "Username or Password incorrect")
    return render(request, 'pages/login.html', {'form': form})
#logout@login_required(login_url='login')
@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')
#User 
def userProfile(request):
    user = request.user  
    return render(request,'parts/profile.html', {'user':user})


           




