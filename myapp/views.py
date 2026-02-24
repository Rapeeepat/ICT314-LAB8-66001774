# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# ต้องชื่อ 'form' เท่านั้นเพื่อให้ตรงกับที่ urls.py เรียกหา
def form(request):
    return render(request, "form.html")