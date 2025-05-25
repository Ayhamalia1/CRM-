from django.contrib import admin
from .models import Customer,Service,CustomerService
from django.contrib.auth.admin import UserAdmin
from .models import User
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(CustomerService)
admin.site.register(User, UserAdmin)
admin.site.site_header= "CRM"
admin.site.site_title= "CRM"



