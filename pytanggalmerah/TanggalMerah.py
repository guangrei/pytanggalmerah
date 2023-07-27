# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone
from .myrequests import MyRequests
import json


in_cache_path = os.path.abspath(os.path.dirname(__file__)) + "/cache/"
class TanggalMerah:
    def __init__(self, cache_path = None, cache_time = 600):
        self.event = set([])
        self.date = datetime.now(timezone("Asia/Jakarta"))
        req = MyRequests("https://raw.githubusercontent.com/guangrei/APIHariLibur_V2/main/holidays.json", cache_path = in_cache_path, cache_time = cache_time)  
        self.data = json.loads(req.response)

    # end __init_()

    def set_timezone(self, tz):
        self.date = datetime.now(timezone(tz))
        return self.date

    # end set_timezone()

    def check(self):
        check = (self.is_sunday(), self.is_holiday())
        return True in check
    # end check()

    def is_sunday(self):
        now = self.date
        day = now.strftime("%A")
        if day == "Sunday":
            self.event.add("sunday")
            return True
        else:
            return False

    # end is_sunday()

    def is_holiday(self):
        d = self.date.strftime("%Y-%m-%d")
        if d in self.data:
            self.event.add(self.data[d]['summary'])
            return True
        else:
            return False

    # end is_holiday()

    def set_date(self, y, m, d):
        self.date = datetime(int(y), int(m), int(d), 0, 0)
        return self.date

    # end set_date()

    def get_event(self):
        return list(self.event)

    # end get_event()
# end class TanggalMerah


if __name__ == "__main__":
    pass
