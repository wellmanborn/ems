from django import forms


class SmsForm(forms.Form):
    url = forms.CharField(label="آدرس url",
                          required=True,
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "آدرس url را وارد نمایید",
                                  "class": "form-control text-left",
                                  "dir": "ltr"
                              }
                          ))
    username = forms.CharField(label="نام کاربری",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "نام کاربری را وارد نمایید",
                                       "class": "form-control text-left",
                                       "dir": "ltr"
                                   }
                               ))
    password = forms.CharField(label="رمزعبور",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "رمز عبور را وارد نمایید",
                                       "class": "form-control text-left",
                                       "dir": "ltr"
                                   }
                               ))
    originator = forms.CharField(label="شماره ارسال",
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "شماره ارسال را وارد نمایید",
                                         "class": "form-control text-left",
                                         "dir": "ltr"
                                     }
                                 ))
