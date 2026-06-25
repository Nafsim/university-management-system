from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import CustomUser
from courses.models import Course
from results.models import Result

def upload_marks(request):
    students = CustomUser.objects.filter(role="student")  # all students
    courses = Course.objects.all()
    selected_course = None
    selected_course_id = None

    if request.method == "POST":
        selected_course_id = request.POST.get("course")
        if selected_course_id:
            selected_course = Course.objects.get(id=selected_course_id)

            # Save marks for each student
            for student in students:
                marks_value = request.POST.get(f"marks_{student.id}")
                if marks_value:
                    Result.objects.update_or_create(
                        student=student,
                        course=selected_course,
                        defaults={
                            "semester": 1,          # adjust dynamically
                            "grade": "A+",          # or calculate from marks
                            "gpa": 4.00             # or calculate from marks
                        }
                    )
            messages.success(request, "Marks uploaded successfully!")
            return redirect("upload_marks")

    return render(request, "teacher/upload_marks.html", {
        "students": students,
        "courses": courses,
        "selected_course": selected_course,
        "selected_course_id": selected_course_id
    })
