from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .apifuncs import locationcodes,average,coldest,singletowncheck
@csrf_exempt
def index(request):
    locationcodes()
    city=request.POST.get('city')
    print(city)
    towntemp, weather, hmdt=singletowncheck(city)
    data1= {"city": city,"towntemp": towntemp,"weather": weather,"hmdt": hmdt}
    citycount, avg=average()
    coldestt=coldest()
    context={"data1": data1, "citycount": citycount, "avg": avg, "coldest":coldestt, }
    return render(request, 'weather/index.html', {"context": context})
