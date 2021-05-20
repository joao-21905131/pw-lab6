from django.shortcuts import render
import datetime
# Create your views here.
def home_page_view(request):
    context = {
        'time': datetime.datetime.now(),
    }
    return render(request, 'website/home.html', context)

def page_one_view(request):
    return render(request, 'website/page1.html')

def page_two_view(request):
    return render(request, 'website/page2.html')
