from django.contrib import admin

# Register your models here.

from myApp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    l=['id','eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)
