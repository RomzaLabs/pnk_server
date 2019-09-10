from django.contrib import admin
from .models import User
from .forms import UserAdminForm
from .choices import USER_TYPES


class UserTypeFilter(admin.SimpleListFilter):
    title = 'User Type'
    parameter_name = 'User Type'

    def lookups(self, request, model_admin):
        return USER_TYPES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user_type__exact=self.value())
        else:
            return queryset


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    search_fields = ('username', 'first_name', 'last_name', 'email', 'user_type',)
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type',)
    list_filter = (UserTypeFilter,)

    class Meta:
        model = User

