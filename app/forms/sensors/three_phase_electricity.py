from django import forms

class ThreePhaseElectricityForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور برق سه فاز",
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
                                       "placeholder": "شماره Data Block برق سه فاز را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    byte_id = forms.IntegerField(label="شماره Byte",
                                 required=False,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "مقدار شماره Byte را وارد نمایید",
                                         "class": "form-control",
                                         "value": 0,
                                         "type": "number"
                                     }
                                 ))
    high = forms.IntegerField(label="مقدار بالای برق سه فاز ",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای برق سه فاز را وارد نمایید",
                                      "class": "form-control",
                                      "value": 230,
                                      "type": "number"
                                  }
                              ))
    # high_rt = forms.IntegerField(label="مقدار بالای برق سه فاز RT",
    #                              required=False,
    #                              widget=forms.TextInput(
    #                                  attrs={
    #                                      "placeholder": "مقدار بالای برق سه فاز RT را وارد نمایید",
    #                                      "class": "form-control",
    #                                      "value": 230,
    #                                      "type": "number"
    #                                  }
    #                              ))
    # high_st = forms.IntegerField(label="مقدار بالای برق سه فاز ST",
    #                              required=False,
    #                              widget=forms.TextInput(
    #                                  attrs={
    #                                      "placeholder": "مقدار بالای برق سه فاز ST را وارد نمایید",
    #                                      "class": "form-control",
    #                                      "value": 230,
    #                                      "type": "number"
    #                                  }
    #                              ))
    low = forms.IntegerField(label="مقدار پایین برق سه فاز ",
                             required=False,
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "مقدار پایین برق سه فاز را وارد نمایید",
                                     "class": "form-control",
                                     "value": 200,
                                     "type": "number"
                                 }
                             ))
    # low_rt = forms.IntegerField(label="مقدار پایین برق سه فاز RT",
    #                             required=False,
    #                             widget=forms.TextInput(
    #                                 attrs={
    #                                     "placeholder": "مقدار پایین برق سه فاز RT را وارد نمایید",
    #                                     "class": "form-control",
    #                                     "value": 200,
    #                                     "type": "number"
    #                                 }
    #                             ))
    # low_st = forms.IntegerField(label="مقدار پایین برق سه فاز ST",
    #                             required=False,
    #                             widget=forms.TextInput(
    #                                 attrs={
    #                                     "placeholder": "مقدار پایین برق سه فاز ST را وارد نمایید",
    #                                     "class": "form-control",
    #                                     "value": 200,
    #                                     "type": "number"
    #                                 }
    #                             ))
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
