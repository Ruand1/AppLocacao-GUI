from datetime import datetime


def get_time():
    time = datetime.now().strftime('%H')
    return int(time)
