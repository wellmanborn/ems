from django import forms


class HumidityForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور رطوبت",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور رطوبت را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block رطوبت را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    very_high = forms.IntegerField(label="حداکثر مقدار بالای رطوبت",
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "حداکثر مقدار بالای رطوبت را وارد نمایید",
                                           "class": "form-control",
                                           "value": 90,
                                           "type": "number"
                                       }
                                   ))
    high = forms.IntegerField(label="مقدار بالای رطوبت",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای رطوبت را وارد نمایید",
                                      "class": "form-control",
                                      "value": 70,
                                      "type": "number"
                                  }
                              ))
    low = forms.IntegerField(label="مقدار پایین رطوبت",
                             required=False,
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "مقدار پایین رطوبت را وارد نمایید",
                                     "class": "form-control",
                                     "value": 10,
                                     "type": "number"
                                 }
                             ))
    very_low = forms.IntegerField(label="حداکثر مقدار پایین رطوبت",
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "حداکثر مقدار پایین رطوبت را وارد نمایید",
                                          "class": "form-control",
                                          "value": 5,
                                          "type": "number"
                                      }
                                  ))
    offset = forms.IntegerField(label="offset رطوبت",
                                required=False,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "offset رطوبت را وارد نمایید",
                                        "class": "form-control",
                                        "value": 0,
                                        "type": "number"
                                    }
                                ))