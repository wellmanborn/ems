from django import forms

class AlarmForm(forms.Form):
    snooze_time = forms.IntegerField(label="زمان Snooze (به دقبقه وارد نمایید)",
                                     required=False,
                                     widget=forms.TextInput(
                                         attrs={
                                             "placeholder": "زمان Snooze (به دقبقه وارد نمایید)",
                                             "class": "form-control",
                                             "type": "number"
                                         }
                                     ))

    time_for_siren_on_day = forms.IntegerField(label="زمان روشن بودن آژیر خطر در روز (به ثانیه وارد نمایید)",
                                               required=False,
                                               widget=forms.TextInput(
                                                   attrs={
                                                       "placeholder": "مدت زمان روشن بودن آژیر خطر در روز (به ثانیه وارد نمایید)",
                                                       "class": "form-control",
                                                       "type": "number"
                                                   }
                                               ))

    time_for_siren_off_day = forms.IntegerField(label="زمان خاموش بودن آژیر خطر در روز (به دقیقه وارد نمایید)",
                                                required=False,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "placeholder": "مدت زمان روشن بودن آژیر خطر در روز (به دقیقه وارد نمایید)",
                                                        "class": "form-control",
                                                        "type": "number"
                                                    }
                                                ))

    time_for_siren_on_night = forms.IntegerField(label="زمان روشن بودن آژیر خطر در شب (به ثانیه وارد نمایید)",
                                                 required=False,
                                                 widget=forms.TextInput(
                                                     attrs={
                                                         "placeholder": "مدت زمان روشن بودن آژیر خطر در شب (به ثانیه وارد نمایید)",
                                                         "class": "form-control",
                                                         "type": "number"
                                                     }
                                                 ))

    time_for_siren_off_night = forms.IntegerField(label="زمان خاموش بودن آژیر خطر در شب (به دقیقه وارد نمایید)",
                                                  required=False,
                                                  widget=forms.TextInput(
                                                      attrs={
                                                          "placeholder": "مدت زمان خاموش بودن آژیر خطر در شب (به دقیقه وارد نمایید)",
                                                          "class": "form-control",
                                                          "type": "number"
                                                      }
                                                  ))

    start_work_time = forms.IntegerField(label="زمان شروع به کار (به ساعت وارد نمایید)",
                                         required=False,
                                         widget=forms.TextInput(
                                             attrs={
                                                 "placeholder": "زمان شروع به کار (به ساعت وارد نمایید)",
                                                 "class": "form-control",
                                                 "type": "number"
                                             }
                                         ))

    end_work_time = forms.IntegerField(label="زمان پایان ساعت کاری (به ساعت وارد نمایید)",
                                       required=False,
                                       widget=forms.TextInput(
                                           attrs={
                                               "placeholder": "زمان پایان ساعت کاری (به ساعت وارد نمایید)",
                                               "class": "form-control",
                                               "type": "number"
                                           }
                                       ))

    total_sms = forms.IntegerField(label="تعداد پیام ها",
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "تعداد پیام ها",
                                           "class": "form-control",
                                           "type": "number"
                                       }
                                   ))

    time_for_repeat_send_sms = forms.IntegerField(label="زمان تکرار پیام (به دقیقه وارد نمایید)",
                                                  required=False,
                                                  widget=forms.TextInput(
                                                      attrs={
                                                          "placeholder": "زمان تکرار پیام (به دقیقه وارد نمایید)",
                                                          "class": "form-control",
                                                          "type": "number"
                                                      }
                                                  ))