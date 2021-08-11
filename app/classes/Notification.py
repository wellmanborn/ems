import http.client
from urllib. parse import urlparse
from app.models import Profile as ProfileModel, Notification as NotificationModel, Setting

# this is for sending message certification error
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def send_sms(destination, content, user_id):
    sms_setting = Setting.objects.filter(key="sms")[0]
    content = str(content.encode('utf-8')).replace('\\x', '%').replace("b\'", "").replace("\'", "").replace(" ",
                                                                                                            "%20")
    url = (f"{sms_setting.config['url']}?username={sms_setting.config['username']}"
           f"&originator={sms_setting.config['originator']}&password={sms_setting.config['password']}&"
           f"destination={destination}&content={content}")
    conn = http.client.HTTPSConnection(urlparse(sms_setting.config['url']).netloc)
    payload = ''
    headers = {}
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    result = data.replace('\n', '').split(" : ")
    if result[0] == "error":
        notification = NotificationModel(type="error", message="خطا در ارسال sms کد خطا : " + result[1], user_id=user_id)
        notification.save()
    else:
        result = data.replace('\n', '').split("</br>")
        notification = NotificationModel(type="success", message="کد پیگیری ارسال sms " + result[2], user_id=user_id)
        notification.save()


def get_users_for_notification():
    profiles = ProfileModel.objects.filter(send_sms=True)
    list_users = []
    for profile in profiles:
        if(profile.user.is_active):
            list_users.append(profile)
    return list_users


def send_notification(notification_type, content):
    profiles = get_users_for_notification()

    # sms_setting = Setting.objects.filter(key="sms")
    # if sms_setting.count() == 1:
    #     if 'url' in sms_setting[0].config:
    #         for profile in profiles:
    #             send_sms(profile.mobile, content, profile.user.id)

    for profile in profiles:
        notification = NotificationModel(type=notification_type, message=content, user_id=profile.user.id)
        notification.save()
