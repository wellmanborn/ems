from django import forms

class DoorForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور درب",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور درب را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block درب را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    start_hour = forms.IntegerField(label="ساعت شروع (به عدد)",
                                    required=False,
                                    widget=forms.TextInput(
                                        attrs={
                                            "placeholder": "ساعت شروع (به عدد وارد نمایید)",
                                            "class": "form-control",
                                            "value": 8,
                                            "type": "number"
                                        }
                                    ))
    start_min = forms.IntegerField(label="دقیقه شروع (به عدد)",
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "دقیقه شروع (به عدد وارد نمایید)",
                                           "class": "form-control",
                                           "value": 30,
                                           "type": "number"
                                       }
                                   ))
    end_hour = forms.IntegerField(label="ساعت پایان (به عدد)",
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "ساعت پایان (به عدد وارد نمایید)",
                                          "class": "form-control",
                                          "value": 17,
                                          "type": "number"
                                      }
                                  ))
    end_min = forms.IntegerField(label="دقیقه پایان (به عدد)",
                                 required=False,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "دقیقه پایان (به عدد وارد نمایید)",
                                         "class": "form-control",
                                         "value": 30,
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
