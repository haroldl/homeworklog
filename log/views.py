from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import logging

from models import *
from helpers import *

logger = logging.getLogger(__name__)

def index(request):
    name = cookie_value(request, 'name', '')
    args = { 'name': name }

    group = cookie_value(request, 'group', None)
    groups = ['', '', '', '']
    if group:
        groups[int(group)] = ' checked="checked"'
    for i, v in zip(xrange(0, len(groups)), groups):
        args["group%d" % i] = v

    return render_to_response('log/index.html', args)

def submit(request):
    if not(request.POST):
        return HttpResponseRedirect(reverse('log.views.index'))
    form = LogForm(request.POST)
    if form.is_valid():
        log = form.save()
        logger.info('hahdebug group ' + log.group)
        r = HttpResponseRedirect(reverse('log.views.thanks', args=(log.first_name,)))
        r.set_cookie('name', log.first_name)
        if log.group in GroupInfo.group_ids:
            r.set_cookie('group', GroupInfo.group_ids[log.group])
        return r
    else:
        logger.info("An invalid form was submitted - probably missing required fields.")
        return index(request)

def thanks(request, first_name):
    return render_to_response('log/thanks.html', {'first_name': first_name})

def css(request):
    return render_to_response('log/css', mimetype='text/css')
