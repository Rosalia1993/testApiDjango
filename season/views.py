from django.views import View
from .models import SeasonStatus
from django.http import JsonResponse
from django.forms.models import model_to_dict
from datetime import timedelta, datetime
# Create your views here.

class SeasonListView(View):
    def get(self,request):
        seasonList = SeasonStatus.objects.all()
        spring_ini, spring_fin = datetime.strptime('03-19','%m-%d'), datetime.strptime('6-19','%m-%d')
        summer_ini, summer_fin = datetime.strptime('06-19','%m-%d'), datetime.strptime('09-21','%m-%d')
        fall_ini, fall_fin = datetime.strptime('09-22','%m-%d'), datetime.strptime('12-20','%m-%d')
        winter_ini, winter_fin = datetime.strptime('12-21','%m-%d'), datetime.strptime('03-18','%m-%d')
        result_list = []

        for i in list(seasonList.values()):
            date = i['order_date'][5:]
            fecha = datetime.strptime(date, '%m-%d')
            if winter_ini > winter_fin:
                f = fecha.strftime('%Y-%m-%d')
                winter_f=f[:4].replace('0','1')+'-'+date
                winter_fin = datetime.strptime(winter_f, '%Y-%m-%d')
            #print(fecha,winter_ini,winter_fin)
            
            if fecha >= spring_ini and fecha <= spring_fin:
                result_list.append(dic(order_id=i['order_id'],season='spring'))
                #print(fecha,"spring")
            else:
                if fecha >= summer_ini and fecha <= summer_fin:
                    result_list.append(dic(order_id=i['order_id'],season='summer'))
                    #print(fecha,"summer")
                else:
                    if fecha >= fall_ini and fecha <= fall_fin:
                        result_list.append(dic(order_id=i['order_id'],season='Fall'))
                        #print(fecha,"Fall")
                    else:
                        if fecha > winter_ini and fecha < winter_fin:
                            result_list.append(dic(order_id=i['order_id'],season='winter'))
                            #print(fecha,"winter")
                        else:
                            result_list.append(dic(order_id=i['order_id'],season='winter'))
                            #print(fecha,"winter")
                
        return JsonResponse(dict(result=result_list))