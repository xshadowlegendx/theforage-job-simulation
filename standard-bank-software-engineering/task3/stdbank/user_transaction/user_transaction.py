
from datetime import datetime, timedelta

from django.db.models import Q

from .models import AppUsage, Transaction

def get_some_user_info(user_id: int):
    now = datetime.now()

    past_30_days = now - timedelta(days=30)

    transactions_of_previous_30_days = Transaction.objects.filter(
        (Q(sender__id=user_id) | Q(recipient__id=user_id)) & (Q(timestamp__lt=now) & Q(timestamp__gt=past_30_days)))

    app_usage_previous_30_days = AppUsage.objects.filter(
        Q(user__id=user_id) & Q(timestamp__lt=now) & Q(timestamp__gt=past_30_days))

    time_spents_as_minutes = 0

    for usage in app_usage_previous_30_days:
        time_spents_as_minutes += (usage.session_end - usage.session_start).seconds / 60

    return transactions_of_previous_30_days, time_spents_as_minutes
