from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from timeline_app.models import Timeline, Event

# Create your views here.
def index(request):
    timeline_objects = Timeline.objects.all().order_by('timeline_id')
    dict = {'timelines' : timeline_objects}

    if request.method=="POST":
            timeline_name = request.POST['timeline_name']
            o = Timeline(timeline_name=timeline_name)
            o.save()
            
    return render(request, 'timeline_app/index.html', context=dict)

def timeline(request, pk):
    timeline = Timeline.objects.get(pk=pk)
    event = Event.objects.filter(timeline_id=pk).order_by('date')
    
    dict = {'timeline': timeline,
            'events': event}

    if request.method=="POST":
        title = request.POST['title']
        date = request.POST['date']
        description = request.POST['description']
        o = Event(date=date, title=title, 
                  description=description, timeline_id=timeline)
        o.save()
    return render(request, 'timeline_app/timeline.html', context=dict)

def delete_timeline(request, id):
  member = Timeline.objects.filter(timeline_id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def delete_event(request, id, timelineId):
  member = Event.objects.filter(event_id=id)
  member.delete()
  return HttpResponseRedirect(reverse('timeline'))