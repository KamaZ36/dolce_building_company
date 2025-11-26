from datetime import datetime, timezone


def get_time_now_remove_tz() -> datetime:
    date = datetime.now(tz=timezone.utc)
    return date.replace(tzinfo=None)
