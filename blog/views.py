from django.shortcuts import render
from blog.models import Entry


def blog_list(request):
    entries = Entry.objects.all()

    return render(request,'blog_list.html', {'blog': entries})
