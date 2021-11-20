from django.shortcuts import redirect, render
from portal.models import Interviewer, Candidate, Interview
from django.contrib import messages
# Create your views here.
def home(request):
    # messages.success(request,"hello")
    return render(request,'home.html')

def schedule(request):
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
            interview = Interview(interviewer=interviewer, Candidate=candidate, date=schedule_date, startTime = startTimer,endTime = endTimer)

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
    print(interview)
    for i in interview:
        print(i)
    context={"interviews":interview}
    print(context)
    return render(request, 'upcoming.html', context)

def edit(request):
    pass

def delete(request):
    pass