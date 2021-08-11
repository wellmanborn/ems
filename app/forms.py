import re

from django import forms

AIR_CONDITIONER_CHOICES = (
    (1, 'یک'),
    (2, 'دو'),
    (3, 'سه'),
    (4, 'چهار')
)
PERMISSIONS_CHOICES = (
    (1, 'ادمین'),
    (0, 'مشاهده')
)
STATUS_CHOICES = (
    (1, 'فعال'),
    (0, 'غیرفعال')
)
AIRCONDITIONER_MANUAL_CHOICES=[(1,'تنظیمات دستی'),
                               (0,'اتوماتیک')]

AIRCONDITIONER_STATUS_CHOICES=[(1,'روشن'),
                               (0,'خاموش')]


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


class PowerForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور برق",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور برق را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block برق را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 1,
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


class WaterleakageForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور نشت آب",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور نشت آب را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block نشت آب را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 1,
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


class SmokeForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور دود",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور دود را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
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


class AirconditionerForm(forms.Form):
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
    airconditioner_count = forms.ChoiceField(label='تعداد ari conditioner',
                                             choices=AIR_CONDITIONER_CHOICES,
                                             widget=forms.Select(
                                                 attrs={
                                                     'class': "form-control"
                                                 }
                                             ),
                                             required=True)


class AirconditionerSettingForm(forms.Form):
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


class SmsForm(forms.Form):
    url = forms.CharField(label="آدرس url",
                          required=True,
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "آدرس url را وارد نمایید",
                                  "class": "form-control text-left",
                                   "dir": "ltr"
                              }
                          ))
    username = forms.CharField(label="نام کاربری",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "نام کاربری را وارد نمایید",
                                       "class": "form-control text-left",
                                       "dir": "ltr"
                                   }
                               ))
    password = forms.CharField(label="رمزعبور",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "رمز عبور را وارد نمایید",
                                       "class": "form-control text-left",
                                       "dir": "ltr"
                                   }
                               ))
    originator = forms.CharField(label="شماره ارسال",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره ارسال را وارد نمایید",
                                       "class": "form-control text-left",
                                       "dir": "ltr"
                                   }
                               ))


class EmailForm(forms.Form):
    url = forms.CharField(label="آدرس url",
                          required=True,
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "آدرس url را وارد نمایید",
                                  "class": "form-control"
                              }
                          ))
    username = forms.CharField(label="username",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "username را وارد نمایید",
                                       "class": "form-control"
                                   }
                               ))
    password = forms.CharField(label="password",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "password را وارد نمایید",
                                       "class": "form-control"
                                   }
                               ))
    port = forms.CharField(label="شماره port",
                           required=True,
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "port را وارد نمایید",
                                   "class": "form-control"
                               }
                           ))


class AirconditionerEditForm(forms.Form):
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

class CreateUserForm(forms.Form):
    first_name = forms.CharField(label="نام",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "نام را وارد نمایید",
                                    "class": "form-control",
                                    "minlength": "2",
                                    "maxlength": "32"
                                }
                            ))
    last_name = forms.CharField(label="نام خانوادگی",
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "نام خانوادگی را وارد نمایید",
                                         "class": "form-control",
                                         "minlength": "3",
                                         "maxlength": "32"
                                     }
                                 ))
    username = forms.CharField(label="نام کاربری",
                                required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "نام کاربری را وارد نمایید",
                                        "class": "form-control",
                                        "data-parsley-type": "alphanum",
                                        "minlength": "3",
                                        "maxlength": "20"

                                    }
                                ))
    email = forms.CharField(label="آدرس ایمیل",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "آدرس ایمیل را وارد نمایید",
                                       "class": "form-control",
                                        "data-parsley-type": "email",
                                   }
                               ))
    mobile = forms.CharField(label="شماره موبایل",
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "شماره موبایل را وارد نمایید، مانند : 09123456789",
                                     "class": "form-control",
                                     "data-parsley-type": "digits",
                                     "minlength": "11",
                                     "maxlength": "11",
                                 }
                             ),
                             required=True)
    job_title = forms.CharField(label='سمت در سازمان',
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "سمت در سازمان وارد نمایید",
                                        "class": "form-control"
                                    }
                                ),
                                required=False)
    password = forms.CharField(
                            widget=forms.PasswordInput(
                                attrs={
                                    "placeholder": "رمز عبور را وارد نمایید",
                                    "class": "form-control",
                                    "autocomplete": "off",
                                    "minlength": "8",
                                    "maxlength": "32",
                                    "id": "password"
                                }
                            ), label="رمز عبور", required=True)
    repeat_password = forms.CharField(
                            widget=forms.PasswordInput(
                                attrs={
                                    "placeholder": "رمز عبور را مجددا وارد نمایید",
                                    "class": "form-control",
                                    "autocomplete": "off",
                                    "minlength": "8",
                                    "maxlength": "32",
                                    "data-parsley-equalto": "#password"
                                }
                            ), label="تکرار رمز عبور", required=True)
    permissions = forms.ChoiceField(label='نوع دسترسی',
                                             choices=PERMISSIONS_CHOICES,
                                             widget=forms.Select(
                                                 attrs={
                                                     'class': "form-control"
                                                 }
                                             ),
                                             required=True)

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")

        return password

    def clean_repeat_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if repeat_password != password:
            raise forms.ValidationError("تکرار رمز عبور صحیح نیست")
        else:
            return repeat_password

    def clean_mobile(self, *args, **kwargs):
        mobile = self.cleaned_data.get("mobile")
        mobile = mobile.replace("-", "")
        x = re.compile('^(09)[0-9]{9}$')
        if(len(mobile) != 11 or x.match(mobile) == None):
            raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست")
        else:
            return mobile

class EditUserForm(forms.Form):
    first_name = forms.CharField(label="نام",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "نام را وارد نمایید",
                                    "class": "form-control",
                                    "minlength": "2",
                                    "maxlength": "32"
                                }
                            ))
    last_name = forms.CharField(label="نام خانوادگی",
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         "placeholder": "نام خانوادگی را وارد نمایید",
                                         "class": "form-control",
                                         "minlength": "3",
                                         "maxlength": "32"
                                     }
                                 ))
    username = forms.CharField(label="نام کاربری",
                                required=False,
                                disabled=True,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "نام کاربری را وارد نمایید",
                                        "class": "form-control",
                                        "disabled": "disabled"
                                    }
                                ))
    email = forms.CharField(label="آدرس ایمیل",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "آدرس ایمیل را وارد نمایید",
                                       "class": "form-control",
                                        "data-parsley-type": "email",
                                   }
                               ))
    mobile = forms.CharField(label="شماره موبایل",
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "شماره موبایل را وارد نمایید، مانند : 09123456789",
                                     "class": "form-control",
                                     "data-parsley-type": "digits",
                                     "minlength": "11",
                                     "maxlength": "11",
                                 }
                             ),
                             required=True)
    job_title = forms.CharField(label='سمت در سازمان',
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "سمت در سازمان وارد نمایید",
                                        "class": "form-control"
                                    }
                                ),
                                required=False)
    permissions = forms.ChoiceField(label='نوع دسترسی',
                                             choices=PERMISSIONS_CHOICES,
                                             widget=forms.Select(
                                                 attrs={
                                                     'class': "form-control"
                                                 }
                                             ),
                                             required=True)
    is_active = forms.ChoiceField(label='وضعیت',
                                    choices=STATUS_CHOICES,
                                    widget=forms.Select(
                                        attrs={
                                            'class': "form-control"
                                        }
                                    ),
                                    required=True)

    def clean_mobile(self, *args, **kwargs):
        mobile = self.cleaned_data.get("mobile")
        mobile = mobile.replace("-", "")
        x = re.compile('^(09)[0-9]{9}$')
        if(len(mobile) != 11 or x.match(mobile) == None):
            raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست")
        else:
            return mobile


class ChangeUserPasswordForm(forms.Form):
    username = forms.CharField(label="نام کاربری",
                               required=False,
                               disabled=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "نام کاربری را وارد نمایید",
                                       "class": "form-control",
                                       "disabled": "disabled"
                                   }
                               ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور را وارد نمایید",
                "class": "form-control",
                "autocomplete": "off",
                "minlength": "8",
                "maxlength": "32",
                "id": "password"
            }
        ), label="رمز عبور", required=True)
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور را مجددا وارد نمایید",
                "class": "form-control",
                "autocomplete": "off",
                "minlength": "8",
                "maxlength": "32",
                "data-parsley-equalto": "#password"
            }
        ), label="تکرار رمز عبور", required=True)

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")

        return password

    def clean_repeat_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if repeat_password != password:
            raise forms.ValidationError("تکرار رمز عبور صحیح نیست")
        else:
            return repeat_password