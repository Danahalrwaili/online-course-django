from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.get(user=request.user, course=course)

    submission = Submission.objects.create(enrollment=enrollment)

    selected_choices = request.POST.getlist('choice')
    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    return HttpResponseRedirect(
        reverse(
            'onlinecourse:show_exam_result',
            args=(course.id, submission.id)
        )
    )


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(pk=submission_id)

    total_score = 0
    for question in course.question_set.all():
        if question.is_get_score(submission):
            total_score += question.grade

    context = {
        'course': course,
        'submission': submission,
        'score': total_score,
    }

    return render(request, 'onlinecourse/exam_result.html', context)
