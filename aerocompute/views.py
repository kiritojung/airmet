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
'''
class AjaxHandlerView(View):
	def get(self, request):
		lat1Text = request.GET.get('lat1_text')
		s = float(lat1Text) + 3
		if request.headers.get('x-requested-with') == 'XMLHttpRequest':
			data = {
				'seconds': s,
			}
			return JsonResponse(data)
		return render(request, '../templates/page1.html')
'''