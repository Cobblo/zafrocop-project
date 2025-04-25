from datetime import datetime, timedelta
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Order, Payment, OrderProduct
from django.utils import timezone

# Register your models here.
class OrderDateRangeFilter(admin.SimpleListFilter):
    title = _('Filter by Date')
    parameter_name = 'created_at_range'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('yesterday', _('Yesterday')),
            ('last_7_days', _('Last 7 Days')),
            ('this_month', _('This Month')),
            ('last_30_days', _('Last 30 Days')),
        )

    def queryset(self, request, queryset):
        now = timezone.now()  # use timezone-aware datetime
        today = now.date()

        if self.value() == 'today':
            return queryset.filter(created_at__date=today)
    
        elif self.value() == 'yesterday':
            yesterday = today - timedelta(days=1)
            return queryset.filter(created_at__date=yesterday)
    
        elif self.value() == 'last_7_days':
            last_7_days = now - timedelta(days=7)
            return queryset.filter(created_at__gte=last_7_days)
    
        elif self.value() == 'this_month':
            return queryset.filter(created_at__year=now.year, created_at__month=now.month)
    
        elif self.value() == 'last_30_days':
            last_30_days = now - timedelta(days=30)
            return queryset.filter(created_at__gte=last_30_days)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered', OrderDateRangeFilter]
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 25                         



admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)