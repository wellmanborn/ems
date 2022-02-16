from django import forms


class EmailForm(forms.Form):
    url = forms.CharField(label="آدرس url",
                          required=True,
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "آدرس url را وارد نمایید",
                                  "class": "form-control"
                              }
                          ))
    username = forms.CharField(label="username",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "username را وارد نمایید",
                                       "class": "form-control"
                                   }
                               ))
    password = forms.CharField(label="password",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "password را وارد نمایید",
                                       "class": "form-control"
                                   }
                               ))
    port = forms.CharField(label="شماره port",
                           required=True,
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "port را وارد نمایید",
                                   "class": "form-control"
                               }
                           ))
