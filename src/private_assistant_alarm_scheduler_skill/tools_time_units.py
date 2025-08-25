from datetime import datetime

SINGLE_DIGIT_MINUTE_THRESHOLD = 10


def format_time_for_tts(time: datetime, with_date: bool = False) -> str:
    hour = time.hour
    minute = time.minute

    if minute == 0:
        time_str = f"{hour} o'clock"
    elif minute < SINGLE_DIGIT_MINUTE_THRESHOLD:
        time_str = f"{minute} past {hour}"
    else:
        time_str = f"{minute} past {hour}"

    if with_date:
        date_str = time.strftime("%A, %B %d")
        return f"{date_str} at {time_str}"
    return time_str
