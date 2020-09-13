from django.shortcuts import render

# Create your views here.
def hello(request):
    tags = [
				'2020-09-17 พร้อมใช้งาน'
			]
    return render(request, '../templates/index.html',
		{
            'tags':tags,
        })
def page1(request):
	return render(request, '../templates/page1.html')