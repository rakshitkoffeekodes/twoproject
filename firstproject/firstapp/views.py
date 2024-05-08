from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import *
import requests
from .twofactor import user_two_factor_auth_data_create
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView, FormView


# This function is for accept reject form

def accept_reject_form(request, pk):
    print(pk)
    option = request.GET.get('option')
    reason_or_url = request.GET.get('name')
    redirect_url = '/myadmin/firstapp/subcategory/'

    try:
        sub_category_data = SubCategory.objects.get(sub_category_id=pk)

        if option == '0' or reason_or_url == '':
            return redirect(redirect_url)

        # if condition check the option is 1 And if option is 1 then it will send data with url

        if option == '1':
            url = reason_or_url
            data = {'name': sub_category_data.sub_category_name, 'description': sub_category_data.description}
            response = requests.post(url, data=data)
            sub_category_data.accept = True
            sub_category_data.reason = '-'
            sub_category_data.save()

        # elif condition check the option is 2 and elif option is 2 then it will store reason in sub_category_data

        elif option == '2':
            sub_category_data.reason = reason_or_url
            sub_category_data.accept = False
            sub_category_data.save()

    except Exception as e:
        return redirect(redirect_url)

    return redirect(redirect_url)


# This class is for generating OTP and qr_code


class AdminSetupTwoFactorAuthView(TemplateView):
    template_name = "admin/2fa.html"

    def post(self, request):
        context = {}
        user = request.user

        try:
            # is sent to the user in user_two_factor_auth_data_create

            two_factor_auth_data = user_two_factor_auth_data_create(user=user)
            otp_secret = two_factor_auth_data.otp_secret

            # In this function the tax_code and OTP are generated

            context["otp_secret"] = otp_secret
            context["qr_code"] = two_factor_auth_data.generate_qr_code(
                name=user.email,
                username=user.username
            )
        except ValidationError as exc:
            context["form_errors"] = exc.messages

        return self.render_to_response(context)


# This class is for admin confirmation if OTP is correct then will send to index page else will give error


class AdminConfirmTwoFactorAuthView(FormView):
    template_name = "admin/c_2fa.html"
    success_url = reverse_lazy("admin:index")

    class Form(forms.Form):
        otp = forms.CharField(required=True)

        # This function is for OTP to check if OTP is valid or not

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

    # This function returns the form class

    def get_form_class(self):
        return self.Form

    # In this function super() takes the property of the above class and stores request.user in form.user

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.user = self.request.user

        return form

    # This function is of for whether the form is valid or not

    def form_valid(self, form):
        form.two_factor_auth_data.rotate_session_identifier()

        self.request.session['2fa_token'] = str(form.two_factor_auth_data.session_identifier)

        return super().form_valid(form)


# This function is to take you to the login page

def login(request):
    return redirect('myadmin:login')
