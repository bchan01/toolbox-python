from parse import is_within_range
from datetime import datetime,  timedelta

# Test

today = datetime.now().date()
print(f"TODAY: {today}")
today_str = today.strftime("%Y-%m-%d")
yesterday = (today + timedelta(days=-1)).strftime("%Y-%m-%d")
print(f"YESTRDAY: {yesterday}")
tomorrow = (today + timedelta(days=1)).strftime("%Y-%m-%d")
print(f"TOMORROW: {tomorrow}")

# empty
print(">>>> EMPTY")
s = 'empty'
print(f"{s} => {is_within_range(s, today)}")
s = '(None, None)'
print(f"{s} => {is_within_range(s, today)}")
s = '[None, None]'
print(f"{s} => {is_within_range(s, today)}")
s = '(None, None]'
print(f"{s} => {is_within_range(s, today)}")
s = '[None, None)'
print(f"{s} => {is_within_range(s, today)}")

# start only
print(">>>> START ONLY")
s = f"[{today_str}, ]"
print(f"{s} => {is_within_range(s, today)}")
s = f"({today_str}, ]"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{yesterday}, ]"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{tomorrow}, ]"
print(f"{s} => {is_within_range(s, today)}")

# end only
print(">>>> END ONLY")
s = f"[, {today_str}]"
print(f"{s} => {is_within_range(s, today)}")
s = f"[, {today_str})"
print(f"{s} => {is_within_range(s, today)}")
s = f"[, {yesterday}]"
print(f"{s} => {is_within_range(s, today)}")
s = f"[, {tomorrow})"
print(f"{s} => {is_within_range(s, today)}")
s = f"[, {tomorrow}]"
print(f"{s} => {is_within_range(s, today)}")


# start and end
print(">>>> START AND END")
s = f"[2023-01-01 , {today_str}]"
print(f"{s} => {is_within_range(s, today)}")
s = f"(2023-01-01 , {today_str})"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{today_str} , 2023-12-23)"
print(f"{s} => {is_within_range(s, today)}")
s = f"({today_str} , 2023-01-23)"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{yesterday}, {today_str}]"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{yesterday}, {today_str})"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{yesterday}, {tomorrow}]"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{yesterday}, {tomorrow})"
print(f"{s} => {is_within_range(s, today)}")
s = f"[{tomorrow}, 2023-12-30)"
print(f"{s} => {is_within_range(s, today)}")
