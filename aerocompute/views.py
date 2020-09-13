from django.shortcuts import render

# Create your views here.
def hello(request):
    tags = ['น้ำตก', 'ธรรมชาติ', 'หน้าฝน', 'ตากหมอก']
    return render(request, '../templates/index.html',
        {
            'name':'บทความท่องเที่ยว',
            'author':'Mymemo',
            'tags':tags,
			'rating':3
        })
