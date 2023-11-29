
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from .user_transaction import get_some_user_info

def get_some_info(request):
    if not request.user.is_authenticated:
        return HttpResponse('unauthorized', status=401)

    transactions_past_30_days, time_spents_as_minutes_past_30_days = get_some_user_info(request.user.id)

    transactions_past_30_days = serializers.serialize('python', transactions_past_30_days)
    
    transactions_past_30_days = [t['fields'] for t in transactions_past_30_days]

    return JsonResponse({
        'transactions_past_30_days': transactions_past_30_days,
        'time_spents_as_minutes_past_30_days': time_spents_as_minutes_past_30_days })
