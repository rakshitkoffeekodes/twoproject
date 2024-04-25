from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from.models import *


def accept_reject_form(request):
    print('====>>>>>')
    if request.method == 'POST':
        option = request.POST.get('option')
        name = request.POST.get('name')
        print(option, name)
        return render(request, 'admin/change_list.html')

    else:
        return render(request, 'admin/change_list.html')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


class SubCategoryAdmin(admin.ModelAdmin):
    def Popup(self, obj):
        form_url = reverse('from', args=[obj.pk], )
        return format_html("""
            <button type="button" class="button">
                <a href="{}">Action</a>
            </button>
        """, form_url)

    Popup.short_description = "Action"

    list_display = ["sub_category_id", "sub_category_name", "description", "category_id", "reason", "accept", "Popup"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
