from django.shortcuts import render
import datetime
import random
# Create your views here.
def result_view(request):
    msg_list = [
        'the golden days a head',
        'better to sleep',
        'tomorrow is a good day',
        'tomorrow is a bad day',
    ]
    names_list=['sunny','mallika','kareena','katrina','deepika']
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if h <= 12:
        s = 'good morning'
    elif h < 16:
        s = 'good afternoon'
    elif h < 21:
        s = 'good night'
    else:
        s = 'good'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'date':date,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)
