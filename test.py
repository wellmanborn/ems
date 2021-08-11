from app.classes.Notification import send_notification


def send():
    send_notification("test")


if __name__ == '__main__':
    send()