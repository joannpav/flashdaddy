from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from flashdaddy.models import Question
from flashdaddyproj import settings
from pytesser import *
from forms import UploadFileForm
from models import UploadFile

# here's a good example of a usecase: http://www.slideshare.net/albertspijkers/lean-analytics-and-practical-facts
# slide preso download disabled, but you want to take notes
# Other usecase is https://read.amazon.com/
# Can't copy snippets from amazon reader to take notes. Yes, you can highlight them but then they go
# to amazon's kindle page where you have to go find them then copy them again

def home(request):
	#if request.method == 'POST':
	form = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
		#UploadFile(file = request.FILES['file'])
		textFile = save_file(request.FILES['file'])
		request.session['textFile']=textFile

		return HttpResponseRedirect(reverse('home'), locals())
	#else:
	#	form = UploadFileForm()

	#data = {'form': form}
	data = ""
	return render_to_response('index.html', data, context_instance=RequestContext(request))


def save_file(file, path=''):
	''' Little helper to save a file
	'''
	filename = file._get_name()
	fd = open('%s/%s' % (settings.MEDIA_ROOT, str(path) + str(filename)), 'wb')
	for chunk in file.chunks():
		fd.write(chunk)
	fd.close()
	result = ocrTest(fd)
	return result


def ocr(request):
	textFile = request.session['textFile']
	return render_to_response('ocr.html', locals())


def ocrTest(fd):
	fp = open(fd.name)
	ms = Image.open(fp)
	textFile = image_to_string(ms)
	return textFile

@csrf_exempt
def createCard(request):
	a = request.POST['answerText']
	q = request.POST['questionText']

	qa = Question(question=q, answer=a)
	qa.save()

	return render_to_response('savedCard.html', locals(), RequestContext(request))


def viewCardList(request):
	print "in viewCardList"
	questions = Question.objects.all()
	return render_to_response('cardBox.html', locals(), RequestContext(request))


def takeQuiz(request):
	print "in takeQuiz"


# things to talk to niki about:
# is there more than one card deck?
# do you want logins?
# can card decks be private and shared?