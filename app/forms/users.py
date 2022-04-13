from django import forms
import re


PERMISSIONS_CHOICES = ((1, 'ادمین'),(0, 'مشاهده'))
STATUS_CHOICES = ((1, 'فعال'),(0, 'غیرفعال'))


class CreateUserForm(forms.Form):
    first_name = forms.CharField(label="نام",
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "نام را وارد نمایید",
                                         "class": "form-control",
                                         "minlength": "2",
                                         "maxlength": "32"
                                     }
                                 ))
    last_name = forms.CharField(label="نام خانوادگی",
                                required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "نام خانوادگی را وارد نمایید",
                                        "class": "form-control",
                                        "minlength": "3",
                                        "maxlength": "32"
                                    }
                                ))
    username = forms.CharField(label="نام کاربری",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "نام کاربری را وارد نمایید",
                                       "class": "form-control",
                                       "data-parsley-type": "alphanum",
                                       "minlength": "3",
                                       "maxlength": "20"

                                   }
                               ))
    email = forms.CharField(label="آدرس ایمیل",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "آدرس ایمیل را وارد نمایید",
                                    "class": "form-control",
                                    "data-parsley-type": "email",
                                }
                            ))
    mobile = forms.CharField(label="شماره موبایل",
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "شماره موبایل را وارد نمایید، مانند : 09123456789",
                                     "class": "form-control",
                                     "data-parsley-type": "digits",
                                     "minlength": "11",
                                     "maxlength": "11",
                                 }
                             ),
                             required=True)
    job_title = forms.CharField(label='سمت در سازمان',
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "سمت در سازمان وارد نمایید",
                                        "class": "form-control"
                                    }
                                ),
                                required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور را وارد نمایید",
                "class": "form-control",
                "autocomplete": "off",
                "minlength": "8",
                "maxlength": "32",
                "id": "password"
            }
        ), label="رمز عبور", required=True)
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور را مجددا وارد نمایید",
                "class": "form-control",
                "autocomplete": "off",
                "minlength": "8",
                "maxlength": "32",
                "data-parsley-equalto": "#password"
            }
        ), label="تکرار رمز عبور", required=True)
    permissions = forms.ChoiceField(label='نوع دسترسی',
                                    choices=PERMISSIONS_CHOICES,
                                    widget=forms.Select(
                                        attrs={
                                            'class': "form-control"
                                        }
                                    ),
                                    required=True)

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")

        return password

    def clean_repeat_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if repeat_password != password:
            raise forms.ValidationError("تکرار رمز عبور صحیح نیست")
        else:
            return repeat_password

    def clean_mobile(self, *args, **kwargs):
        mobile = self.cleaned_data.get("mobile")
        mobile = mobile.replace("-", "")
        x = re.compile('^(09)[0-9]{9}$')
        if(len(mobile) != 11 or x.match(mobile) == None):
            raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست")
        else:
            return mobile

class EditUserForm(forms.Form):
    first_name = forms.CharField(label="نام",
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "نام را وارد نمایید",
                                         "class": "form-control",
                                         "minlength": "2",
                                         "maxlength": "32"
                                     }
                                 ))
    last_name = forms.CharField(label="نام خانوادگی",
                                required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "نام خانوادگی را وارد نمایید",
                                        "class": "form-control",
                                        "minlength": "3",
                                        "maxlength": "32"
                                    }
                                ))
    username = forms.CharField(label="نام کاربری",
                               required=False,
                               disabled=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "نام کاربری را وارد نمایید",
                                       "class": "form-control",
                                       "disabled": "disabled"
                                   }
                               ))
    email = forms.CharField(label="آدرس ایمیل",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "آدرس ایمیل را وارد نمایید",
                                    "class": "form-control",
                                    "data-parsley-type": "email",
                                }
                            ))
    mobile = forms.CharField(label="شماره موبایل",
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "شماره موبایل را وارد نمایید، مانند : 09123456789",
                                     "class": "form-control",
                                     "data-parsley-type": "digits",
                                     "minlength": "11",
                                     "maxlength": "11",
                                 }
                             ),
                             required=True)
    job_title = forms.CharField(label='سمت در سازمان',
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "سمت در سازمان وارد نمایید",
                                        "class": "form-control"
                                    }
                                ),
                                required=False)
    permissions = forms.ChoiceField(label='نوع دسترسی',
                                    choices=PERMISSIONS_CHOICES,
                                    widget=forms.Select(
                                        attrs={
                                            'class': "form-control"
                                        }
                                    ),
                                    required=True)
    is_active = forms.ChoiceField(label='وضعیت',
                                  choices=STATUS_CHOICES,
                                  widget=forms.Select(
                                      attrs={
                                          'class': "form-control"
                                      }
                                  ),
                                  required=True)

    def clean_mobile(self, *args, **kwargs):
        mobile = self.cleaned_data.get("mobile")
        mobile = mobile.replace("-", "")
        x = re.compile('^(09)[0-9]{9}$')
        if(len(mobile) != 11 or x.match(mobile) == None):
            raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست")
        else:
            return mobile


class ChangeUserPasswordForm(forms.Form):
    username = forms.CharField(label="نام کاربری",
                               required=False,
                               disabled=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "نام کاربری را وارد نمایید",
                                       "class": "form-control",
                                       "disabled": "disabled"
                                   }
                               ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور را وارد نمایید",
                "class": "form-control",
                "autocomplete": "off",
                "minlength": "8",
                "maxlength": "32",
                "id": "password"
            }
        ), label="رمز عبور", required=True)
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور را مجددا وارد نمایید",
                "class": "form-control",
                "autocomplete": "off",
                "minlength": "8",
                "maxlength": "32",
                "data-parsley-equalto": "#password"
            }
        ), label="تکرار رمز عبور", required=True)

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")

        return password

    def clean_repeat_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if repeat_password != password:
            raise forms.ValidationError("تکرار رمز عبور صحیح نیست")
        else:
            return repeat_password
