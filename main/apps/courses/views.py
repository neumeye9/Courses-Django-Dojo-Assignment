from django.shortcuts import render, redirect
from models import Courses
from django.contrib import messages

# Create your views here.

def index(request):
    courses = Courses.coursesManager.all()
    context = {
        "courses": courses
    }
    return render(request, 'courses/index.html', context)

def add(request):
    print "Added Course"

    check = Courses.coursesManager.add(request.POST['name'], request.POST['description'])

    if not check [0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)


    print check
    return redirect('/')

def remove(request, id):
    print "Remove Course?"
    context = {
        "course": Courses.coursesManager.get(id=id)
    }
    return render(request, 'courses/delete.html', context)

def back(request):
    print "Decided not to delete this"
    return redirect('/')

def delete(request, id):
    print "course deleted"
    this = Courses.coursesManager.get(id=id)
    this.delete()
    return redirect('/')
