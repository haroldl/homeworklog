from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Log

def index(request):
    logs = Log.objects.all()
    if len(logs) == 0:
        log = Log(first_name = "Bob", assignment_title = "Foo")
        log.save()
    else:
        log = logs[0]
    return render_to_response('log/index.html')

def submit(request):
    if not(request.POST):
        return HttpResponseRedirect(reverse('log.views.index'))
    log = Log()
    log.first_name        = request.POST['first_name']
    log.assignment_title  = request.POST['assignment_title']
    log.save()
    return HttpResponseRedirect(reverse('log.views.thanks', args=(log.first_name,)))

def thanks(request, first_name):
    return render_to_response('log/thanks.html', {'first_name': first_name})
