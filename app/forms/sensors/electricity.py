from django import forms

class PowerForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور برق",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور برق را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block برق را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 1,
                                      "type": "number"
                                  }
                              ))
    start_value = forms.IntegerField(label="مقدار نرمال (0 یا 1 وارد گردد)",
                                     required=False,
                                     widget=forms.TextInput(
                                         attrs={
                                             "placeholder": "مقدار نرمال را وارد نمایید",
                                             "class": "form-control",
                                             "value": 1,
                                             "type": "number"
                                         }
                                     ))
