from django.contrib import admin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User, Group
from django.urls import reverse, path
from django.utils.html import format_html
from .models import *
import pyotp
from django.core.exceptions import ValidationError

from .views import AdminSetupTwoFactorAuthView
from .views import AdminConfirmTwoFactorAuthView


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


class SubCategoryAdmin(admin.ModelAdmin):
    def Popup(self, obj):

        form_url = reverse('accept_reject_form', args=[obj.pk])
        print(form_url)
        return format_html("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
                  integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w=="
                  crossorigin="anonymous" referrerpolicy="no-referrer"/>
        </head>
        <body>
                <style>
                    .popup {{
                        position: fixed;
                        top: 0;
                        right: 0;
                        left: 0;
                        bottom: 0;
                        width: 100vw;
                        height: 100vh;
                        background-color: rgba(0, 0, 0, 0.5);
                        z-index: 10000;
                    }}

                    .form-data {{
                        position: fixed;
                        background-color: #f4f6f9;
                        border-radius: 5px;
                        width: 25%;
                        height: 55%;
                        left: 40vw;
                        top: 25vh;
                    }}

                    .cancel-icon{{
                        position: absolute;
                        font-size: 10px;
                        right: 8px;
                        top: 8px;
                        color: #f4f6f9;
                        background: #343a40;
                        padding: 5px 6px;
                        border-radius: 100%;
                    }}

                    .first-container {{
                        width: 100%;
                        height: 5%;
                    }}

                    .second-container {{
                        padding-left: 20px;
                        padding-top: 10px;
                        font-family: "Garamond", Times, serif;
                        font-weight: bold;
                        color: #343a40;
                    }}

                    .third-container {{
                        width: 100%;
                        height: 25%;
                        color: #343a40;
                    }}

                    .four-container {{
                        width: 100%;
                        height: 25%;
                        color: #343a40;

                    }}

                    .five-container {{
                        width: 100%;
                        height: 30%;
                    }}

                    .required {{
                        color:red;
                    }}

                    .select-label{{
                        font-family: "Times New Roman", Times, serif;
                        padding-left: 20px;
                        padding-top: 10px;
                        font-size: 15px;
                    }}

                    .dropdown {{
                        width:88%;
                        height: 45%;
                        margin-left:20px;
                        outline: none;
                        border-radius: 5px;
                        font-family: "Times New Roman", Times, serif;
                        padding-left: 10px;
                        padding-right: 10px;
                    }}

                    .enter-label{{
                        font-family: "Times New Roman", Times, serif;
                        padding-left: 20px;
                        padding-top: 15px;
                        font-size: 15px;
                    }}

                    .input-text {{
                        width:88%;
                        margin-left:20px;
                        border-radius: 5px;
                        font-family: "Times New Roman", Times, serif;
                        outline: none;
                    }}

                    .save-btn {{
                        margin-top:10%;
                        margin-left:20px;
                        width: 88%;
                        border-radius: 5px;
                        color: white;
                        cursor: pointer;
                    }}

                </style>
                <button type="button" onclick="popupFn(obj.pk)" id="button" class="btn btn-primary">
                    Action
                </button>
                <div id="form" class="popup" style="display:none;">
                     <div class="form-data" id="form-data">
                        <form action="/accept_reject_form/" method="post" id="myForm" >
                            <div class="first-container">
                                <i class="fa fa-times cancel-icon" aria-hidden="true" id="cancel"></i>
                            </div>
                            <div class="second-container">
                                <h5>Action Form</h5>
                            </div>
                            <div class="third-container">
                                <p class="p-header-2 font-family select-label">Status <span class="required">*</span> :</p>
                                <select class="dropdown" name="option" id="dropdown" style="border-color: black;">
                                    <option name="option" value="0">--------</option>
                                    <option name="option" value="1">Accept</option>
                                    <option name="option" value="2">Reject</option>
                                </select>
                            </div>
                            <div class="four-container">
                                <p class="p-header-2 font-family enter-label">Enter URL / Reason <span class="required">*</span>&nbsp;:</p>
                                <input type="text" id="input" name="name" placeholder="Enter..." class="input-text" style="border-color: black; border-radius: 5px;">
                            </div>
                            <div class="five-container">
                                <button type="button" onclick="getFormData('{}', {})" class="btn btn-success save-btn ">save</button>
                            </div>
                        </form>
                     </div>
                </div>
                <script>
                     function popupFn(objId) {{ 
                        var form = document.getElementById("form");
                        var dropdown = document.getElementById("dropdown");
                        var input = document.querySelector(".input-text");
                        var cancel = document.getElementById("cancel");

                        form.style.display = "block";

                        dropdown.addEventListener("change", function() {{
                            if (this.value === "1")
                                input.placeholder = "Enter a URL";
                            else if (this.value === "2")
                                input.placeholder = "Enter a Reason";
                            else if (this.value === "0")
                                input.placeholder = "Enter..";
                        }});

                    }}

                    function getFormData(formUrl, objId) {{
                        var option = document.getElementById("dropdown").value;
                        var name = document.getElementById("input").value;
                        var url = formUrl + '?option=' + option + '&name=' + name + '&obj_id=' + objId;;
                        window.location.href = url;
                    }}  

                    document.getElementById("cancel").addEventListener("click", function()
                    {{
                        document.getElementById("form").style.display = "none";
                    }});

                </script>
            </body>
        </html>
        """, form_url, obj.pk)

    Popup.short_description = "Action"

    list_display = ["sub_category_id", "sub_category_name", "description", "category_id", "reason", "accept", "Popup"]


class MyAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"
    default_site = 'my_custom_admin_site'

    def get_urls(self):
        base_urlpatterns = super().get_urls()

        extra_urlpatterns = [
            path(
                "setup-2fa/",
                self.admin_view(AdminSetupTwoFactorAuthView.as_view()),
                name="setup-2fa"
            ),
            path(
                "confirm-2fa/",
                self.admin_view(AdminConfirmTwoFactorAuthView.as_view()),
                name="confirm-2fa"
            )
        ]

        return extra_urlpatterns + base_urlpatterns

    def login(self, request, *args, **kwargs):
        if request.method != 'POST':
            return super().login(request, *args, **kwargs)

        username = request.POST.get('username')

        two_factor_auth_data = UserTwoFactorAuthData.objects.filter(
            user__username=username
        ).first()
        request.POST._mutable = True
        request.POST[REDIRECT_FIELD_NAME] = reverse('admin:confirm-2fa')

        if two_factor_auth_data is None:
            request.POST[REDIRECT_FIELD_NAME] = reverse("admin:setup-2fa")
        else:
            request.POST[REDIRECT_FIELD_NAME] = reverse('admin:confirm-2fa')
        request.POST._mutable = False

        return super().login(request, *args, **kwargs)

    def has_permission(self, request):
        has_perm = super().has_permission(request)

        if not has_perm:
            return has_perm

        two_factor_auth_data = UserTwoFactorAuthData.objects.filter(user=request.user).first()

        allowed_paths = [
            reverse("admin:confirm-2fa"),
            reverse("admin:setup-2fa")
        ]

        if request.path in allowed_paths:
            return True

        if two_factor_auth_data is not None:
            two_factor_auth_token = request.session.get("2fa_token")

            return str(two_factor_auth_data.session_identifier) == two_factor_auth_token

        return False


admin_site = MyAdminSite(name="myadmin")
admin_site.register(UserTwoFactorAuthData)
admin_site.register(Category, CategoryAdmin)
admin_site.register(SubCategory, SubCategoryAdmin)

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']

    def save_model(self, request, obj, form, change):
        if obj.password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)


admin_site.register(User, CustomUserAdmin)
admin_site.register(Group)
