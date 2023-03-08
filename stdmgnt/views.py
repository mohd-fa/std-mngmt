from django.shortcuts import render
from .models import Student, User, Department, Staff
# Create your views here.

def student(request):
    depts = Department.objects.all()
    if request.method == "POST":
       student = Student()
       student.name = request.POST.get('name')
       student.address = request.POST.get('address')
       student.semester = request.POST.get('semester')
       student.admnno = request.POST.get('admnno')
       user = User(user_type=3)
       user.save()
       student.user = user
       student.dept = Department.objects.get(pk = request.POST.get('dept'))
       student.save()

    return render(request,'student.html',{'depts':depts})


def staff(request):
    depts = Department.objects.all()
    if request.method == "POST":
       staff = Staff()
       staff.name = request.POST.get('name')
       staff.address = request.POST.get('address')
       staff.staffid = request.POST.get('staffid')
       user = User(user_type=2)
       user.save()
       staff.user = user
       staff.dept = Department.objects.get(pk = request.POST.get('dept'))
       staff.save()

    return render(request,'staff.html',{'depts':depts})