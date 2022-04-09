from django import forms

class TemperatureForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور دما",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور دما را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block دما را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    very_high = forms.IntegerField(label="حداکثر مقدار بالای دما",
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "حداکثر مقدار بالای دما را وارد نمایید",
                                           "class": "form-control",
                                           "value": 30,
                                           "type": "number"
                                       }
                                   ))
    high = forms.IntegerField(label="مقدار بالای دما",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای دما را وارد نمایید",
                                      "class": "form-control",
                                      "value": 27,
                                      "type": "number"
                                  }
                              ))
    low = forms.IntegerField(label="مقدار پایین دما",
                             required=False,
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "مقدار پایین دما را وارد نمایید",
                                     "class": "form-control",
                                     "value": 12,
                                     "type": "number"
                                 }
                             ))
    very_low = forms.IntegerField(label="حداکثر مقدار پایین دما",
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "حداکثر مقدار پایین دما را وارد نمایید",
                                          "class": "form-control",
                                          "value": 10,
                                          "type": "number"
                                      }
                                  ))
    offset = forms.IntegerField(label="offset دما",
                                required=False,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "offset دما",
                                        "class": "form-control",
                                        "value": 0,
                                        "type": "number"
                                    }
                                ))