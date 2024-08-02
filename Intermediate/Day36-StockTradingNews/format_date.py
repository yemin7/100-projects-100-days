import datetime
from datetime import timedelta
from datetime import datetime as dt


class FormatDate:
    def __init__(self):
        self.time_now = dt.now(datetime.UTC)

    def yesterday(self):
        return self.time_now - timedelta(days=1)

    def before_yesterday(self):
        return self.time_now - timedelta(days=2)

    def format_yesterday(self, format_string):
        return dt.strftime(self.yesterday(), format_string)

    def format_before_yesterday(self, format_string):
        return dt.strftime(self.before_yesterday(), format_string)
