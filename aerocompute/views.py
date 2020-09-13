from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, '../templates/index.html', {'name':'ท่องเที่ยวภาคเหนือ'})
