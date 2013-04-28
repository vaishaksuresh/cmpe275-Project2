from django.shortcuts import render_to_response
import json,requests

def home(request):
	r = requests.get('https://www.coursera.org/maestro/api/topic/list?full=1')
	return render_to_response('index.html',{'courses': r.json()})

