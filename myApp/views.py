from django.shortcuts import render
from myApp.models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize
import json
from django.views.generic import View

class EmployeeDetails(View):
	def get(self,request,*args,**kwargs):
		emp=Employee.objects.all()
		json_data=serialize('json',emp)
		p_dict=json.loads(json_data)
		result=[]
		for ob in p_dict:
			emp_data=ob['fields']
			result.append(emp_data)
		json_data=json.dumps(result)
		return HttpResponse(json_data,content_type="application/json")

		# emp=Employee.objects.all()
		# json_data=serialize('json',emp)
		# return HttpResponse(json_data,content_type="application/json")



		# emp=Employee.objects.get(id=id)
		# json_data=serialize('json',[emp],fields=('eno','ename'))
		# return HttpResponse(json_data,content_type="application/json")

		# emp=Employee.objects.get(id=id)
		# json_data=serialize('json',[emp])
		# return HttpResponse(json_data,content_type="application/json")

		# emp=Employee.objects.get(id=id)
		# emp_data={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}
		# json_data=json.dumps(emp_data)
		# return HttpResponse(json_data,content_type="application/json")



