from django.shortcuts import render_to_response
import json,requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
import simplejson

def home(request):
	r =  requests.get('http://localhost:8080/rest/course/doc1')
        courses=r.json()
	print(r.json())
	return render_to_response('courselist.html',{'courses': courses})

def search_form(request):
    return render(request, 'search_form.html')

def frontpage(request):
    return render_to_response('frontpage.html')

def search(request):
    if 'id' in request.GET:
	r =  requests.get('http://localhost:8080/rest/course/%s' % request.GET['id'])
	print(r.json())
	courses=r.json()
        return render_to_response('courselist.html',{'courses': courses})
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def addcourse(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('title', ''):
            errors.append('Enter the Title')
        if not request.POST.get('section', ''):
            errors.append('Enter the Section.')
	if not request.POST.get('department', ''):
            errors.append('Enter the Department.')
	if not request.POST.get('teachername', ''):
            errors.append('Enter the Teacher Name')
	if not request.POST.get('teacherid', ''):
            errors.append('Enter the Teacher id')

        if not errors:
	    term= request.POST['term']
	    title= request.POST['title']
	    section = request.POST['section']
	    department = request.POST['department']
   	    name= request.POST['teachername']
	    tid = request.POST['teacherid']
	    days = request.POST['days']
	    time = request.POST['time1']
            addstr = {"term": term,"title": title,"section": section ,"department":department,"teacher": [name,tid],"days": days,"time": time}
	    coursejson=simplejson.dumps(addstr)
	    
	    print(coursejson)
	return HttpResponse('added')
    return render(request, 'add-course.html',{'errors': errors},context_instance=RequestContext(request))



# BAD!
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)
