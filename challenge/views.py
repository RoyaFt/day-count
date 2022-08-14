from multiprocessing import context
from pydoc import render_doc
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse




my_week = {
    'saturday' : 'i love it',
    'sunday' : 'its my lucky day',
    'monday' : 'im so bussy',
    'tuesdat' : 'i wanna go trip',
    'wednesday' : 'i have some work to do',
    'tursday' : 'its my off',
    'friday' : None ,
}



def index2(request,day):
    data = my_week.get(day)
    context = {
        "day" : day,
        "day_data" : data,
        }
        #return HttpResponse(f'day is: {day} and my data is: {data}')
    return render(request,'challenge/challenge.html',context)



def index3(request,day):
    if day <= 7:
        my_list = list(my_week.keys())
        user_choose = my_list[day-1]
        my_reverse = reverse('day-of-week', args = [user_choose])
        return HttpResponseRedirect (my_reverse)
    return HttpResponseNotFound()

def index4(request):
    my_list = list(my_week.keys())
    context = {
        'days_list' : my_list
    }
    return render(request,'challenge/index.html',context)


    


    