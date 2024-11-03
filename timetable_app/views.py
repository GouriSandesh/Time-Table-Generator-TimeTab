import random

from django.http import HttpResponse
from .timetable_generator import generate_timetable
from django.shortcuts import render, redirect, get_object_or_404

from timetable_app.forms import CourseForm, SubjectForm, StaffForm
from timetable_app.models import Course, Subject, Staff


def homepage(request):
    return render(request,'index.html')


def courseView(request):
    data =Course.objects.all()
    return render(request,'courses.html',{'data': data})


def addCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseView')
    return render(request,'add_course.html',{'form':form})


def updateCourse(request,id):
    data = Course.objects.get(id=id)
    form = CourseForm(instance=data)
    if request.method == 'POST':
        form =CourseForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('courseView')
    return render(request,'update_course.html',{'form':form})


def delCourse(request,id):
    data = Course.objects.get(id=id)
    data.delete()
    return redirect('courseView')



def subjectView(request):
    data = Subject.objects.all()
    return render(request,'subject.html',{'data':data})



def addSubject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjectView')
    return render(request,'add_subject.html',{'form':form})


def updateSubject(request,id):
    data = Subject.objects.get(id=id)
    form = SubjectForm(instance=data)
    if request.method == 'POST':
        form =SubjectForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('subjectView')
    courses =Course.objects.all()
    return render(request,'update_subject.html',{'form':form,'courses':courses})


def delSubject(request,id):
    data =Subject.objects.get(id=id)
    data.delete()
    return redirect('subjectView')



def staffView(request):
    data = Staff.objects.all()
    return render(request,'staff.html',{'data':data})



def addStaff(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffView')
    return render(request, 'add_staff.html', {'form': form})


def updateStaff(request,id):
    data = Staff.objects.get(id=id)
    form = StaffForm(instance=data)
    if request.method == 'POST':
        form =StaffForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('staffView')
    return render(request,'update_staff.html',{'form':form})


def delStaff(request,id):
    data =Staff.objects.get(id=id)
    data.delete()
    return redirect('staffView')


def select_course_view(request):
    if request.method == 'POST':
        selected_course_id = request.POST.get('course')  # Get the selected course ID
        selected_course = Course.objects.get(id=selected_course_id)  # Retrieve the course object
        timetable_data = generate_timetable(selected_course)  # Pass the selected course to your function
        return render(request, 'timetable_generate.html', {'timetable_data': timetable_data, 'form': form})

    # For GET request, display the list of courses
    courses = Course.objects.all()
    form = CourseForm()  # Assuming you have a form for your courses
    return render(request, 'timetable_select.html', {'courses': courses, 'form': form})


def generate_timetable_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')  # Get the selected course ID

        try:
            selected_course = Course.objects.get(id=course_id)  # Retrieve the selected course
        except Course.DoesNotExist:
            return HttpResponse("Course matching query does not exist.", status=404)

        try:
            timetable = generate_timetable(selected_course)  # Pass the selected course to the function
            return render(request, 'timetable_generate.html', {
                'timetable': timetable,  # Pass the timetable directly
                'course_name': selected_course.course_name
            })
        except Exception as e:
            return HttpResponse(f"Error generating timetable: {e}")
    else:
        courses = Course.objects.all()  # Fetch all courses for selection
        return render(request, 'timetable_select.html', {'courses': courses})
