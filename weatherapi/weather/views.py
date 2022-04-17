from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .apifuncs import locationcodes,average,coldest,singletowncheck
@csrf_exempt
def index(request):
    locationcodes()
    if(request.POST):
         city=request.form.get('city')
         towntemp,weather,hmdt=singletowncheck(city)
         data1={"city": city,"towntemp": towntemp,"weather": weather,"hmdt": hmdt}
         citycount,avg=average()
         coldestt=coldest()
    return render(request, 'weather/index.html', data1, citycount, avg, coldestt)
