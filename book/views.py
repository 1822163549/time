from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime#注意datetime一定要导入


def baidu(request):
	text='www.baidu.com'
	return HttpResponse(text)

def index(request):
	context={
		'value1':'我是第一个啦！',
		'value': datetime(year=2019, month=11,
			day=8,hour=17,minute=59,second=0)
	}
	return render(request, '1.html', context=context)