from django import forms


class FuseForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور فیوز",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور فیوز را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block فیوز را وارد نمایید",
                                       "class": "form-control",
                                       "value": 75,
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
