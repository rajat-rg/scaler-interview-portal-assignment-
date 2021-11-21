from django.shortcuts import redirect, render
from portal.models import Interviewer, Candidate, Interview
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def schedule(request,slug=""):
    print(slug)
    if request.method == 'POST':
        interviewerEmail = request.POST.get('interviewerEmail')
        candidateEmail = request.POST.get('candidateEmail')
        schedule_date = request.POST.get('date')
        startTimer = request.POST.get('startTime')
        endTimer = request.POST.get('endTime')
        try:
            interviewer = Interviewer.objects.get(email=interviewerEmail)
        except:
            messages.error(request, "Interviewer not found")
        
        try:
            candidate = Candidate.objects.get(email=candidateEmail)
        except:
            messages.error(request, "Candidate not found")
        i1 = Interview.objects.filter(interviewer = interviewer, date = schedule_date, startTime= startTimer)
        i2 = Interview.objects.filter(Candidate = candidate, date = schedule_date, startTime= startTimer)
        if len(i1)==0 and len(i2)==0:
            if slug == "":
                interview = Interview(interviewer=interviewer, Candidate=candidate, date=schedule_date, startTime = startTimer,endTime = endTimer)
            else:
                interview = Interview.objects.get(sno=slug)
                interview.interviewer = interviewer
                interview.candidate = candidate
                interview.date = schedule_date
                interview.startTime = startTimer
                interview.endTime = endTimer
            interview.save()
            msg= "interview scheduled for "+candidate.name+" X "+interviewer.name+" \n on "+schedule_date + " at "+ startTimer
            messages.success(request, msg)

        if(len(i1) != 0):
            msg = interviewer.name, 'has a interview scheduled at', schedule_date, '', startTimer
            messages.error(request, msg)
        if(len(i2) != 0):
            msg = candidate.name, 'has a interview scheduled at', schedule_date, " ", startTimer
            messages.error(request, msg)
    return redirect('home')
    
def upcoming(request):
    interview = Interview.objects.all()
    context={"interviews":interview}
    return render(request, 'upcoming.html', context)

def edit(request,slug):
    inter = Interview.objects.get(sno=slug)
    context = {'interview':inter}
    return render(request, 'edit.html',context)

def confirmEdit(request,slug):
    slug = str(slug)
    schedule(request, slug)
    return redirect("home")


def delete(request, slug):
    inter = Interview.objects.get(sno=slug)
    inter.delete()
    msg = "interview id "+slug+"deleted successfully."
    messages.success(request, msg)
    return redirect("home")