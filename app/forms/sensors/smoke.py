from django import forms

SMOKE_DATA_BLOCK_TYPE_CHOICES = [('boolean', 'Boolean'), ('word', 'Word')]


class SmokeForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور دود",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور دود را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    setting__data_block_type = forms.ChoiceField(label="نوع دیتا بلاک",
                                                 choices=SMOKE_DATA_BLOCK_TYPE_CHOICES,
                                                 initial='boolean',
                                                 widget=forms.Select(
                                                     attrs={
                                                         'class': "form-control"
                                                     }
                                                 ),
                                                 required=True)

    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block دود را وارد نمایید",
                                       "class": "form-control",
                                       "value": 60,
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
