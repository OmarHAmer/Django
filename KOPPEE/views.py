from django.shortcuts import render
from .models import Job
from .forms import ApplyForms
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    formjobfilter = JobFilter(request.GET, queryset=job_list)
    jobfilter = formjobfilter.qs

    paginator = Paginator(jobfilter, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : formjobfilter
    }
    return render(request,'job/job_list.html',context)
    
@login_required
def job_detail(request, slug):
    job_detail = Job.objects.get(slug = slug)

    if request.method == 'POST' :
        form = ApplyForms(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid() :
            myform = form.save(commit=False)
            # myform = myform.cleaned_data()
            print(myform)
            myform.job = job_detail
            myform.save()
            

    else :
        form = ApplyForms()
        
    print (job_detail)
    context = {
        'job' : job_detail,
        'form' : form
    }
    return render(request,'job/job_detail.html',context)