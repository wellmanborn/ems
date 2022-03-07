from django import forms

AIRCONDITIONER_MANUAL_CHOICES=[(1,'تنظیمات دستی'),(0,'اتوماتیک')]

AIRCONDITIONER_CHOICES = ((1, 'یک'),(2, 'دو'),(3, 'سه'),(4, 'چهار'))

AIRCONDITIONER_STATUS_CHOICES=[(1,'روشن'),(0,'خاموش')]

AIRCONDITIONER_TYPE_CHOICES=[("temponly",'فقط شامل دما'),("full",'کامل (شامل دما و رطوبت)')]


class AirConditionerForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور تهویه هوا",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور تهویه هوا را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block تهویه هوا را وارد نمایید",
                                       "class": "form-control",
                                       "value": 64,
                                       "type": "number"
                                   }
                               ))
    byte_id = forms.IntegerField(label="شماره Byte",
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": " شماره Byte را وارد نمایید",
                                         "class": "form-control",
                                         "value": 42,
                                         "type": "number"
                                     }
                                 ))
    air_conditioner_count = forms.ChoiceField(label='تعداد تهویه هوا',
                                             choices=AIRCONDITIONER_CHOICES,
                                             widget=forms.Select(
                                                 attrs={
                                                     'class': "form-control"
                                                 }
                                             ),
                                             required=True)

    air_conditioner_type = forms.ChoiceField(label='نوع تهویه هوا',
                                             choices=AIRCONDITIONER_TYPE_CHOICES,
                                             initial="full",
                                             widget=forms.Select(
                                                 attrs={
                                                     'class': "form-control"
                                                 }
                                             ),
                                             required=True)


class AirConditionerSettingForm(forms.Form):
    set_point_on = forms.IntegerField(label="ست پوینت روشن",
                                      required=True,
                                      widget=forms.TextInput(
                                          attrs={
                                              "placeholder": "ست پوینت روشن",
                                              "class": "form-control",
                                              "type": "number"
                                          }
                                      ))
    set_point_off = forms.IntegerField(label="ست پوینت خاموش",
                                       required=True,
                                       widget=forms.TextInput(
                                           attrs={
                                               "placeholder": "ست پوینت خاموش",
                                               "class": "form-control",
                                               "type": "number"
                                           }
                                       ))
    set_point_humidity = forms.IntegerField(label="ست پوینت رطوبت",
                                            required=True,
                                            widget=forms.TextInput(
                                                attrs={
                                                    "placeholder": "ست پوینت رطوبت",
                                                    "class": "form-control",
                                                    "type": "number"
                                                }
                                            ))
    time_for_over_range = forms.IntegerField(label="زمان over range",
                                             required=True,
                                             widget=forms.TextInput(
                                                 attrs={
                                                     "placeholder": "زمان over range",
                                                     "class": "form-control",
                                                     "type": "number"
                                                 }
                                             ))
    start_first_hour  = forms.IntegerField(label="اولین ساعت شروع",
                                           required=True,
                                           widget=forms.TextInput(
                                               attrs={
                                                   "placeholder": "اولین ساعت شروع",
                                                   "class": "form-control",
                                                   "type": "number"
                                               }
                                           ))
    start_second_hour = forms.IntegerField(label="دومین ساعت شروع",
                                           required=True,
                                           widget=forms.TextInput(
                                               attrs={
                                                   "placeholder": "دومین ساعت شروع",
                                                   "class": "form-control",
                                                   "type": "number"
                                               }
                                           ))
    start_third_hour = forms.IntegerField(label="سومین ساعت شروع",
                                          required=True,
                                          widget=forms.TextInput(
                                              attrs={
                                                  "placeholder": "سومین ساعت شروع",
                                                  "class": "form-control",
                                                  "type": "number"
                                              }
                                          ))
    control_method = forms.ChoiceField(label=" تنظیمات ",
                                       choices=AIRCONDITIONER_MANUAL_CHOICES,
                                       required=True,
                                       widget=forms.RadioSelect(
                                           attrs={
                                               "placeholder": "تنظیمات"
                                           }
                                       ))


class AirConditionerSettingTempOnlyForm(forms.Form):
    set_point_on = forms.FloatField(label="ست پوینت روشن",
                                   required=True,
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "ست پوینت روشن",
                                           "class": "form-control"
                                       }
                                   ))
    set_point_off = forms.FloatField(label="ست پوینت خاموش",
                                     required=True,
                                     widget=forms.TextInput(
                                         attrs={
                                             "placeholder": "ست پوینت خاموش",
                                             "class": "form-control"
                                         }
                                     ))
    alarm_time = forms.IntegerField(label="زمان alarm",
                                    required=True,
                                    widget=forms.TextInput(
                                        attrs={
                                            "placeholder": "زمان alarm به دقیقه وارد نمایید",
                                            "class": "form-control",
                                            "type": "number"
                                        }
                                    ))
    warning_time = forms.IntegerField(label="زمان warning",
                                      required=True,
                                      widget=forms.TextInput(
                                          attrs={
                                              "placeholder": "زمان warning به دقیقه وارد نمایید",
                                              "class": "form-control",
                                              "type": "number"
                                          }
                                      ))
    control_method = forms.ChoiceField(label=" تنظیمات ",
                                       choices=AIRCONDITIONER_MANUAL_CHOICES,
                                       required=True,
                                       widget=forms.RadioSelect(
                                           attrs={
                                               "placeholder": "تنظیمات"
                                           }
                                       ))
class AirConditionerEditForm(forms.Form):
    title = forms.CharField(label=" شناسه air conditioner",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه air conditioner را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    status = forms.ChoiceField(label=" وضعیت ",
                               choices=AIRCONDITIONER_STATUS_CHOICES,
                               required=False,
                               widget=forms.RadioSelect())