from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from programs.models import Program


def homepage(request):
    t = get_template('homepage.html')
    return HttpResponse(t.render(RequestContext(request, {
            'programs': Program.objects.all()
        })))
