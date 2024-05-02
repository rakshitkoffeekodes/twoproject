from django import forms
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from .models import *
import requests
from .twofactor import user_two_factor_auth_data_create


# #
# def add_category(request: HttpRequest):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         user_ip = request.META.get('REMOTE_ADDR')
#         print('======>', user_ip)
#         category = Category.objects.create(name=name, description=description)
#         category.save()
#
#         second_project_url = 'http://192.168.1.107:8001/category/'
#         data = {'name': name, 'description': description}
#         response = requests.post(second_project_url, data=data)
#         return redirect('admin:index')
#
#     return render(request, 'admin/change_list.html')

def accept_reject_form(request, pk):
    print('id============>', pk)
    print(request.method)
    print('=======>', request.GET.get('obj_id'))
    print('=======>', request.GET.get('name'))
    option = request.GET.get('option')
    name = request.GET.get('name')
    try:
        sub_category_data = SubCategory.objects.get(sub_category_id=pk)
        print('name', name, 'option', option)
        if option == 0:
            return redirect('admin:index')
        if name == '':
            return redirect('admin:index')
        if option == '1':
            print(name)
            url = name
            data = {'name': sub_category_data.sub_category_name, 'description': sub_category_data.description}
            response = requests.post(url, data=data)
            sub_category_data.accept = True
            sub_category_data.reason = '-'
            sub_category_data.save()
            return redirect('admin:index')

        elif option == '2':
            print(sub_category_data.sub_category_id)
            sub_category_data.reason = name
            sub_category_data.accept = False
            sub_category_data.save()
            return redirect('admin:index')
    except Exception as e:
        return redirect('admin:index')


def logout(request):
    return render(request, 'registration/logged_out.html')


from django.core.exceptions import ValidationError
from django.views.generic import TemplateView, FormView


class AdminSetupTwoFactorAuthView(TemplateView):
    template_name = "admin/2fa.html"

    def post(self, request):
        context = {}
        user = request.user

        try:
            two_factor_auth_data = user_two_factor_auth_data_create(user=user)
            otp_secret = two_factor_auth_data.otp_secret

            context["otp_secret"] = otp_secret
            context["qr_code"] = two_factor_auth_data.generate_qr_code(
                name=user.email,
                username=user.username
            )
        except ValidationError as exc:
            context["form_errors"] = exc.messages

        return self.render_to_response(context)


class AdminConfirmTwoFactorAuthView(FormView):
    template_name = "admin/c_2fa.html"
    success_url = reverse_lazy("admin:index")

    class Form(forms.Form):
        otp = forms.CharField(required=True)

        def clean_otp(self):
            self.two_factor_auth_data = UserTwoFactorAuthData.objects.filter(
                user=self.user
            ).first()

            if self.two_factor_auth_data is None:
                raise ValidationError('2FA not set up.')

            otp = self.cleaned_data.get('otp')

            if not self.two_factor_auth_data.validate_otp(otp):
                raise ValidationError('Invalid 2FA code.')

            return otp

    def get_form_class(self):
        return self.Form

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.user = self.request.user

        return form

    def form_valid(self, form):
        form.two_factor_auth_data.rotate_session_identifier()

        self.request.session['2fa_token'] = str(form.two_factor_auth_data.session_identifier)

        return super().form_valid(form)

