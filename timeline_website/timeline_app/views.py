from django.shortcuts import render
from django.http import HttpResponse
from timeline_app.models import Timeline, Event

# Create your views here.
def index(request):
    return render(request, 'timeline_app/master.html')

def timeline(request, pk):
    timeline = Timeline.objects.get(pk=pk)
    event = Event.objects.filter(timeline_id=pk)
    
    dict = {'timeline': timeline,
            'events': event}

    if request.method=="POST":
        title = request.POST['title']
        date = request.POST['date']
        description = request.POST['description']
        o = Event(date=date, title=title, 
                  description=description, timeline_id=pk)
        o.save()
    return render(request, 'timeline_app/timeline.html', context=dict)