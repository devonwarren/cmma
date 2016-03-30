from django.shortcuts import render
from programs.models import Program


def program_view(request, slug):
    program = Program.objects.get(slug=slug)

    trainers = program.trainers.all()

    return render(
        request,
        'program.html',
        {'program': program,
        'trainers': trainers})
