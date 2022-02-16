from django import forms


class OnePhaseElectricityForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور برق تک فاز",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور برق تک فاز را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block برق تک فاز را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    high = forms.IntegerField(label="مقدار بالای برق تک فاز",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای برق تک فاز را وارد نمایید",
                                      "class": "form-control",
                                      "value": 230,
                                      "type": "number"
                                  }
                              ))
    low = forms.IntegerField(label="مقدار پایین برق تک فاز",
                             required=False,
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "مقدار پایین برق تک فاز را وارد نمایید",
                                     "class": "form-control",
                                     "value": 200,
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
