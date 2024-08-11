from datetime import date



def set_attrs(object_, keywords, values):
    for kw, val in zip(keywords, values):
        setattr(object_, kw, val)
    

def get_date(date_: str):
    D = date_.split("-")
    y, m, d = int(D[0]), int(D[1]), int(D[2])
    return date(y, m, d)

def days_difference(end, start):
    delta = end - start
    return delta.days


def get_next_day(date_: str):
    date_ = get_date(date_=date_)
    day = date_.day
    mon = date_.month
    yaer = date_.year
    if day == 30 and mon == 12:
        day = 1
        mon = 1
        yaer += 1
    elif day == 30:
        day = 1
        mon += 1
        yaer = yaer
    else:
        day += 1
    next_day = date(year=yaer, month=mon, day=day)
    return next_day.isoformat()

def get_priv_day(date_: str):
    date_ = get_date(date_=date_)
    day = date_.day
    mon = date_.month
    yaer = date_.year
    if day == 1 and mon == 1:
        day = 30
        mon = 12
        yaer -= 1
    elif day == 1:
        day = 30
        mon -= 1
    else:
        day -= 1
    next_day = date(year=yaer, month=mon, day=day)
    return next_day.isoformat()

