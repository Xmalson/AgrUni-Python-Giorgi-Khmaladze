from datetime import datetime
s = input()
dt = datetime.fromisoformat(s)

date_part = dt.strftime("%d-%m-%Y %H:%M:%S")

offset = dt.utcoffset()
hours = int(offset.total_seconds() / 3600)

print(f"{date_part} {hours:+d}")