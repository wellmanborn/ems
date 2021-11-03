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

class CurrentForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور جریان",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور جریان را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block جریان را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    high = forms.IntegerField(label="مقدار بالای جریان",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای جریان را وارد نمایید",
                                      "class": "form-control",
                                      "value": 0,
                                      "type": "number"
                                  }
                              ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 5,
                                      "type": "number"
                                  }
                              ))


class PoweroneForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور برق تک فاز",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور برق تک فاز را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block برق تک فاز را وارد نمایید",
                                       "class": "form-control",
                                       "type": "number"
                                   }
                               ))
    high = forms.IntegerField(label="مقدار بالای برق تک فاز",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای برق تک فاز را وارد نمایید",
                                      "class": "form-control",
                                      "value": 230,
                                      "type": "number"
                                  }
                              ))
    low = forms.IntegerField(label="مقدار پایین برق تک فاز",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار پایین برق تک فاز را وارد نمایید",
                                      "class": "form-control",
                                      "value": 200,
                                      "type": "number"
                                  }
                              ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 5,
                                      "type": "number"
                                  }
                              ))


class PowerthreeForm(forms.Form):
    title = forms.CharField(label="شناسه سنسور برق سه فاز",
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "شناسه سنسور برق تک فاز را وارد نمایید",
                                    "class": "form-control"
                                }
                            ))
    db_id = forms.IntegerField(label="شماره Data Block",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "شماره Data Block برق سه فاز را وارد نمایید",
                                       "class": "form-control",
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
    high = forms.IntegerField(label="مقدار بالای برق سه فاز ",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار بالای برق سه فاز را وارد نمایید",
                                      "class": "form-control",
                                      "value": 230,
                                      "type": "number"
                                  }
                              ))
    # high_rt = forms.IntegerField(label="مقدار بالای برق سه فاز RT",
    #                              required=False,
    #                              widget=forms.TextInput(
    #                                  attrs={
    #                                      "placeholder": "مقدار بالای برق سه فاز RT را وارد نمایید",
    #                                      "class": "form-control",
    #                                      "value": 230,
    #                                      "type": "number"
    #                                  }
    #                              ))
    # high_st = forms.IntegerField(label="مقدار بالای برق سه فاز ST",
    #                              required=False,
    #                              widget=forms.TextInput(
    #                                  attrs={
    #                                      "placeholder": "مقدار بالای برق سه فاز ST را وارد نمایید",
    #                                      "class": "form-control",
    #                                      "value": 230,
    #                                      "type": "number"
    #                                  }
    #                              ))
    low = forms.IntegerField(label="مقدار پایین برق سه فاز ",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "مقدار پایین برق سه فاز را وارد نمایید",
                                      "class": "form-control",
                                      "value": 200,
                                      "type": "number"
                                  }
                              ))
    # low_rt = forms.IntegerField(label="مقدار پایین برق سه فاز RT",
    #                             required=False,
    #                             widget=forms.TextInput(
    #                                 attrs={
    #                                     "placeholder": "مقدار پایین برق سه فاز RT را وارد نمایید",
    #                                     "class": "form-control",
    #                                     "value": 200,
    #                                     "type": "number"
    #                                 }
    #                             ))
    # low_st = forms.IntegerField(label="مقدار پایین برق سه فاز ST",
    #                             required=False,
    #                             widget=forms.TextInput(
    #                                 attrs={
    #                                     "placeholder": "مقدار پایین برق سه فاز ST را وارد نمایید",
    #                                     "class": "form-control",
    #                                     "value": 200,
    #                                     "type": "number"
    #                                 }
    #                             ))
    time = forms.IntegerField(label="زمان خطا (به ثانیه وارد نمایید)",
                              required=False,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "زمان خطا را وارد نمایید",
                                      "class": "form-control",
                                      "value": 5,
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
    airconditioner_count = forms.ChoiceField(label='تعداد air conditioner',
                                             choices=AIR_CONDITIONER_CHOICES,
                                             widget=forms.Select(
                                                 attrs={
                                                     'class': "form-control"
                                                 }
                                             ),
                                             required=True)


class AirconditionerSettingForm(forms.Form):
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