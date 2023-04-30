from django.shortcuts import render
from django.http import HttpResponse
from timeline_app.models import Timeline

# Create your views here.
def index(request):
    return render(request, 'timeline_app/index.html')

def timeline(request, pk):
    course = Timeline.objects.get(pk=pk)
    dict = {'timeline' : timeline}
    return render(request, 'timeline_app/timeline.html', context=dict)