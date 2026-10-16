from datetime import datetime, timezone, timedelta, time

date = datetime(2026, 10, 16, 8, 58, 13, tzinfo=timezone.utc)
print(date.isoformat())
set_date = date + timedelta(minutes=60)
print(set_date.isoformat())
print()
aware_date = datetime.now(timezone.utc)
print(aware_date.isoformat())
aware_date = aware_date + timedelta(minutes=60)
print(aware_date.isoformat())
new_date = set_date - aware_date
print(new_date)
print()
naive_date = datetime(2026, 10, 16, 14, 58, 13, tzinfo=timezone.utc)
print(naive_date.isoformat())
naive_date = naive_date + timedelta(minutes=60)
print(naive_date.isoformat())
# new_date = set_date - naive_date
# print(new_date)


def sla(create_date, duration, now=None):
    if now is None:
        now = datetime.now(timezone.utc)
    deadline = create_date + timedelta(minutes=duration)
    if deadline < now:
        return "Over due"
    elif deadline == now:
        return "Due"
    else:
        return "Not due yet."
    
print(sla(date, 60, naive_date))
print(sla(date, 1))
