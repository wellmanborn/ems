from django import forms

class CurrentForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور جریان",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور جریان را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block جریان را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    high = forms.IntegerField(label="مقدار بالای جریان",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای جریان را وارد نمایید",
                                      "class": "form-control",
                                      "value": 0,
                                      "type": "number"
                                  }
                              ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 5,
                                      "type": "number"
                                  }
                              ))
