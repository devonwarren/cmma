from django.shortcuts import render
from staff.models import Trainer
from programs.models import Program


def trainer_view(request, slug):
    trainer = Trainer.objects.get(slug=slug)

    programs = Program.objects.filter(trainers=trainer.id)

    return render(
        request,
        'trainer.html',
        {'trainer': trainer,
        'programs': programs})
