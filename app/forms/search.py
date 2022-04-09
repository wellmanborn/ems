from django import forms
SENSOR_TYPES = (
    ("", 'انتخاب کنید ...'),
    ("temperature", 'دما'),
    ("humidity", 'رطوبت'),
    ("current", 'جریان'),
    ("powerthree", 'برق سه فاز'),
    ("powerone", 'برق تک فاز'),
    ("power", 'برق'),
    ("waterleakage", 'نشت آب'),
    ("door", 'درب'),
    ("smoke", 'دود'),
    ("fuse", 'فیوز'),

)
SENSOR_DIGITAL_TYPES = (
    ("", 'انتخاب کنید ...'),
    ("temperature", 'دما'),
    ("humidity", 'رطوبت'),
    ("current", 'جریان'),
    ("powerthree", 'برق سه فاز'),
    ("powerone", 'برق تک فاز')
)
FAILIURE_CHOICES = (
    ("", 'انتخاب کنید ...'),
    (0, 'بدون خطا'),
    (1, 'کم'),
    (2, 'متوسط'),
    (3, 'زیاد'),
    (4, 'حیاتی')
)

class SearchLogDataForm(forms.Form):
    sensor_type = forms.ChoiceField(label='نوع سنسور',
                                    choices=SENSOR_TYPES,
                                    initial='',
                                    widget=forms.Select(
                                        attrs={
                                            'class': "form-control"
                                        }
                                    ),
                                    required=False)

    sensor_digital_type = forms.ChoiceField(label='نوع سنسور',
                                            choices=SENSOR_DIGITAL_TYPES,
                                            initial='',
                                            widget=forms.Select(
                                                attrs={
                                                    'class': "form-control"
                                                }
                                            ),
                                            required=False)

    sensor_id = forms.ChoiceField(label='عنوان سنسور',
                                  widget=forms.Select(
                                      attrs={
                                          'class': "form-control"
                                      }
                                  ),
                                  required=False)
    sensor_alarm = forms.ChoiceField(label='خطای سنسور',
                                     choices=FAILIURE_CHOICES,
                                     initial='',
                                     widget=forms.Select(
                                         attrs={
                                             'class': "form-control"
                                         }
                                     ),
                                     required=False)
    from_date = forms.CharField(label="از تاریخ",
                                required=False,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "از تاریخ",
                                        "class": "form-control form-datetime-picker",
                                        "data-enabletimepicker": "true",
                                        "dir":"ltr",
                                        "data-mddatetimepicker": "true",
                                        "data-placement": "right",
                                        "data-value": ""
                                    }
                                ))
    from_date_value = forms.CharField(widget=forms.HiddenInput(), initial="")

    to_date = forms.CharField(label="تا تاریخ",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "تا تاریخ",
                                      "class": "form-control form-datetime-picker",
                                      "data-enabletimepicker": "true",
                                      "dir": "ltr",
                                      "data-mddatetimepicker": "true",
                                      "data-placement": "right",
                                      "data-value": ""
                                  }
                              ))
    to_date_value = forms.CharField(widget=forms.HiddenInput(), initial="")
