from django.shortcuts import render

# Create your views here.
from jobs.models import Job
from jobs.models import Cities,JobTypes
from django.template import loader
from django.http import HttpResponse
from django.http import Http404


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list':job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request,job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404('Job dose not exist')
    return render(request,'job.html',{'job':job})