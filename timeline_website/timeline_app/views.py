from django.shortcuts import render
from django.http import HttpResponse
from timeline_app.models import Timeline, Event

# Create your views here.
def index(request):
    return render(request, 'timeline_app/index.html')

def timeline(request, pk):
    course = Timeline.objects.get(pk=pk)

    if request.method=="POST":
        title = request.add['title']
        date = request.add['date']
        description = request.add['description']
        o = Event(date=date, title=title, 
                  description=description, timeline_id=pk)
        o.save()
    
    dict = {'timeline' : timeline}
    return render(request, 'timeline_app/timeline.html', context=dict)