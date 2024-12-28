from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def course_list(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses, 'students': students})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'courses/student_detail.html', {'student': student})
