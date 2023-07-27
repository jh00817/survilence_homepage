from django.http import HttpResponse
from django.template import loader

def login(request):
	template = loader.get_template('login.html') # templates 폴더에 있는 html 파일 정보를 가져온다.
	return HttpResponse(template.render()) # template을 view에 표현한다.

def main(request):
	template = loader.get_template('main.html') # templates 폴더에 있는 html 파일 정보를 가져온다.
	return HttpResponse(template.render()) # template을 view에 표현한다.

def dev(request):
	template = loader.get_template('dev.html') # templates 폴더에 있는 html 파일 정보를 가져온다.
	return HttpResponse(template.render()) # template을 view에 표현한다.