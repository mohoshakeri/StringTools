from jdatetime import datetime as jdatetime
from datetime import datetime as dt
from datetime import date

months = {
    1 : 'فروردین',
    2 : 'اردیبهشت',
    3 : 'خرداد',
    4 : 'تیر',
    5 : 'مرداد',
    6 : 'شهریور',
    7 : 'مهر',
    8 : 'آبان',
    9 : 'آذر',
    10 : 'دی',
    11 : 'بهمن',
    12 : 'اسفند',
}

en_months = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December',
}

def to_text_format(datetime:dt,time_check=True,year_check=True,lang='Persian'):
    if datetime:
        if isinstance(datetime, date) and not isinstance(datetime, dt):
            datetime = dt.combine(datetime,dt.min.time())
        if lang == 'Persian':
            jalali = jdatetime.fromgregorian(datetime=datetime)
            year = str(jalali.year)
            month = months[jalali.month]
            day = str(jalali.day)
            hour = str(jalali.hour)
            min = str(jalali.minute)
            if int(min) < 10 : min = '0' + min
            if int(hour) < 10 : hour = '0' + hour
            
            if isinstance(datetime, date) and not isinstance(datetime, dt) and year_check:
                result = day + ' ' + month + ' ' + year
            elif isinstance(datetime, date) and not isinstance(datetime, dt):
                result = day + ' ' + month
            elif time_check and year_check:
                result = day + ' ' + month + ' ' + year + ' - ' + 'ساعت ' + hour + ':' + min
            elif year_check:
                result = day + ' ' + month + ' ' + year
            elif time_check:
                result = day + ' ' + month  + ' - ' + 'ساعت ' + hour + ':' + min
            else:
                result = day + ' ' + month
        else:
            year = str(datetime.year)
            month = en_months[datetime.month]
            day = str(datetime.day)
            hour = str(datetime.hour)
            min = str(datetime.minute)
            if int(min) < 10 : min = '0' + min
            if int(hour) < 10 : hour = '0' + hour
            
            if isinstance(datetime, date) and not isinstance(datetime, dt) and year_check:
                result = month + ' ' + day + ', ' + year
            elif isinstance(datetime, date) and not isinstance(datetime, dt):
                result = month + ' ' + day
            elif time_check and year_check:
                result = month + ' ' + day + ', ' + year + ' at ' + hour + ':' + min
            elif year_check:
                result = month + ' ' + day + ', ' + year
            elif time_check:
                result = month + ' ' + day + ' at ' + hour + ':' + hour
            else:
                result = month + ' ' + day
        return result