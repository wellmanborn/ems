from django import forms


FAN_STATUS_CHOICES=[(1,'روشن'),(0,'خاموش')]

class FanForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور فن",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور فن را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block فن را وارد نمایید",
                                       "class": "form-control",
                                       "value": 82,
                                       "type": "number"
                                   }
                               ))
    byte_id = forms.IntegerField(label="شماره Byte",
                                 required=False,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "مقدار شماره Byte را وارد نمایید",
                                         "class": "form-control",
                                         "value": 2,
                                         "type": "number"
                                     }
                                 ))

    bit_id = forms.IntegerField(label="شماره Bit",
                                required=False,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "مقدار شماره Bit را وارد نمایید",
                                        "class": "form-control",
                                        "value": 0,
                                        "type": "number"
                                    }
                                ))

    setting__fan_control_byte_id = forms.IntegerField(label="شماره Byte کنترل",
                                                      required=False,
                                                      widget=forms.TextInput(
                                                          attrs={
                                                              "placeholder": "مقدار شماره Byte کنترل را وارد نمایید",
                                                              "class": "form-control",
                                                              "value": 0,
                                                              "type": "number"
                                                          }
                                                      ))

    setting__fan_control_bit_id = forms.IntegerField(label="شماره Bit کنترل",
                                                     required=False,
                                                     widget=forms.TextInput(
                                                         attrs={
                                                             "placeholder": "مقدار شماره Bit کنترل را وارد نمایید",
                                                             "class": "form-control",
                                                             "value": 0,
                                                             "type": "number"
                                                         }
                                                     ))
    status = forms.ChoiceField(label=" وضعیت ",
                               choices=FAN_STATUS_CHOICES,
                               required=False,
                               widget=forms.RadioSelect())
