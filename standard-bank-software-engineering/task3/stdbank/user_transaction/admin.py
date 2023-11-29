from django.contrib import admin

from .models import User, AppUsage, Transaction

admin.site.register(User)
admin.site.register(AppUsage)
admin.site.register(Transaction)
