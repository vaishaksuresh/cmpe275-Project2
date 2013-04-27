from django.shortcuts import render_to_response
import json,requests

def home(request):
	r = requests.get('https://www.coursera.org/maestro/api/topic/list?full=1')
	#r = requests.get('https://www.coursera.org/maestro/api/university/list')
	#data = json.dumps(r.json())
	return render_to_response('index.html',{'courses': r.json()})

