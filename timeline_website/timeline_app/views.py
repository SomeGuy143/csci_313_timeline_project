from django.shortcuts import render
from django.http import HttpResponse
from timeline_app.models import Timeline, Event

# Create your views here.
def index(request):
    return render(request, 'timeline_app/index.html')

def timeline(request, pk):
    course = Timeline.objects.get(pk=pk)
    
    #Events.objects.filter(id=id).delete()
    
    if request.method=="POST":
        title = request.POST['title']
        date = request.POST['date']
        description = request.POST['description']
        o = Event(date=date, title=title, 
                  description=description, timeline_id=pk)
        o.save()
    
    dict = {'timeline' : timeline}
    return render(request, 'timeline_app/timeline.html', context=dict)