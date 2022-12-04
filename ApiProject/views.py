from django.shortcuts import render
from django.views import View
from .models import OrderStatus
from django.http import JsonResponse
from django.forms.models import model_to_dict

class OrderStatusView(View):
    def get(self,request):
        orderList = OrderStatus.objects.all()
        return JsonResponse(list(orderList.values()),safe=False)

class OrderStatusItemView(View):
    def get(self,request, pk):
        item = OrderStatus.objects.filter(order_number=pk)
        final_status = ''
        order = ''
       
        for i in list(item.values()):
            order = i['order_number']
            if "CANCELLED" in i['status']:
                final_status = i['status']
                break
            elif "PENDING" in i['status']:
                final_status  = i['status']
                break
            else:
                final_status = i['status']
              
        #print (order,final_status)
        #return JsonResponse (list(item.values()),safe=False)
        return JsonResponse(dict(order_number=order,status=final_status))


