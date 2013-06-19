# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from project.models import Student_info
from project.forms import *
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from project.models import Certificate, Student_info, Student_infoForm, CertificateForm
#from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate, login
def fdata(request):
	if request.method == 'POST':
		form = Student_infoForm(request.POST)
		if form.is_valid():
			p=form.save()
			return HttpResponseRedirect('project.views.fill')
			#return HttpResponseRedirect(reverse('project.views.form',args=('1')))
	else:
		form = Student_infoForm()
	return render_to_response('project/form1.html', {'form': form}, context_instance=RequestContext(request))
def cerdata(request):
	if request.method == 'POST':
		form = CertificateForm(request.POST)
		if form.is_valid():
			p=form.save()
			return HttpResponseRedirect('project.views.fill')
	else:
		form = CertificateForm()
	return render_to_response('project/form2.html', {'form': form}, context_instance=RequestContext(request))
def fill(request):
	return render_to_response('project/fill.html', context_instance=RequestContext(request))	
def done(request):
	return render_to_response('project/done.html', context_instance=RequestContext(request))
def info(request):
	data_list= Student_info.objects.all().order_by('Roll_Number')[:1000]
	#data_list= Student_info.objects.filter(Branch='IT')
	#data_list= Student_info.objects.filter(Branch='CSE')
	#data_list= Student_info.objects.all().order_by('student_info_id')[:100]
	return render_to_response('project/info.html',{'data_list':data_list})
	
def degree(request, Roll_Number):
#def degree(request, student_info_id):
	p=get_object_or_404(Student_info, pk=Roll_Number )
	#p=get_object_or_404(Student_info, pk=student_info_id)
	#p=Student_info.objects.filter(pk=Roll_Number)
	cer_detail=Certificate.objects.filter(student_info_id=Roll_Number)
	#b=Student_info.objects.filter(Branch='IT')
	#c=Student_info.objects.filter(Branch="CSE")
	
	#cer_detail=get_object_or_404(Certificate, pk=Roll_Number)
	#cer_detail=get_object_or_404(Certificate, pk=student_info_id)
	return render_to_response('project/degree.html', {'data_list':p, 'cer_detail':cer_detail}, context_instance=RequestContext(request))
#def form(request):
	#return rendor_to_response('data/form.html'
	

def search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			Roll_Number=cd['search']
			#data_list=Student_info.objects.filter(pk=Roll_Number)
			p=get_object_or_404(Student_info, pk=Roll_Number)
			cer_detail=Certificate.objects.filter(student_info_id=Roll_Number)
			#return HttpResponseRedirect(reverse('data.views.degree', args=('106005')))
			return render_to_response('project/degree.html',{'data_list':p, 'cer_detail':cer_detail}, context_instance=RequestContext(request))
	else:
		form = SearchForm()
	return render_to_response('project/index.html', {'form': form}, context_instance=RequestContext(request))

def filter(request):
	if request.method == 'POST':
		form = FilterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			branch=cd['department']
			data_list= Student_info.objects.filter(Branch=branch).order_by('Roll_Number')[:100]
			
			#return HttpResponseRedirect(reverse('data.views.degree', args=('106005')))
			return render_to_response('project/info.html',{'data_list':data_list}, context_instance=RequestContext(request))
	#else:
		#form = FilterForm()
	#return render_to_response('data/index.html', {'form': form}, context_instance=RequestContext(request))
def new(request):
    return render_to_response('project/new.html', context_instance=RequestContext(request))
#def batch(request):
	#return render_to_response('data/batch.html')
#def login_user(request):
    #state = "Please log in below..."
    #username = password = ''
    #if request.POST:
        #username = request.POST.get('username')
        #password = request.POST.get('password')

        #user = authenticate(username=username, password=password)
        #if user is not None:
            #if user.is_active:
                #login(request, user)
                #state = "You're successfully logged in!"
		#return render_to_response('data/index.html')
		
            #else:
                #state = "Your account is not active, please contact the site admin."
        #else:
            #state = "Your username and/or password were incorrect."
	#return render_to_response('auth.html',{'state':state, 'username': username})	
	
	
	#def fdata(request):
	#if request.method == 'POST':
		#if 'one' in request.POST:
		#	oneform= Student_infoForm(request.POST)
		#	if oneform.is_valid():
		#		one.save()
		#	twoform=CertificateForm()
		#elif 'two' in request.POST:
		#	twoform=CertificateForm(request.POST)
		#	if twoform.is_valid():
		#		two.save()
		
	#else:
	#	oneform = Student_infoForm()
	#	twoform=CertificateForm()
	#return render_to_response('project/form.html', {'oneform':oneform, 'twoform':oneform}, context_instance=RequestContext(request))	
	
