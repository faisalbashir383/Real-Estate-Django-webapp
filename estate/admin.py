from django.contrib import admin
from .models import Property,Service,Contact,Testmonial
# Register your models here.


admin.site.register((Property,Service,Contact,Testmonial))