from django.shortcuts import render


# Create your views here.
def hello(request):
	per = '100'
	tags = [
				'2020-09-30 หาความสูง QFE พร้อมใช้งาน',
				'2020-09-29 หาความสูง QFE อยู่ระหว่างดำเนินการ ',
				'2020-09-28 หาความสูง QFE อยู่ระหว่างดำเนินการ',
				'2020-09-27 หาความสูง QFE อยู่ระหว่างดำเนินการ',
				'2020-09-24 Pressure From Table 3.12.2 เพิ่มระบบจำค่า input ล่าสุดใน TextBox',
				'2020-09-19 Pressure From Table 3.12.2 แก้ไข นำค่าสัมบูรณ์ออกจาก \u0394\u03A6, ใส่ปุ่มเคลียร์ฝั่งซ้ายและขวา',
				'2020-09-17 Pressure From Table 3.12.2 พร้อมใช้งาน'
			]
	return render(request, '../templates/index.html',
		{
            'tags':tags,
			'per' : per,
        })

def page1(request):
	return render(request, '../templates/page1.html')
	
def qfeH(request):
	return render(request, '../templates/qfeHeight.html')
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