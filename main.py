from datetime import \
  datetime as dt,\
  timezone as tz,\
  timedelta as td
import logging
import math

from lang.langage import lang_data
from lang.timezone import timezone_data

def get_now(timezone) -> dt:
  return dt.now(timezone)

def elapsed_time(timezone: tz, datetime: dt) -> td:
  return get_now(timezone) - datetime

def approximated_time(datetime: dt, lang:str, timezone:str="", format:str="{} {}{}") -> str:
  """ 
    Returns the approximate time compared to the current time.

    ex. approxmimated_time(<class datetime.datetime>, 'en') 
  """

  # set langage data
  try:
    ld = lang_data[lang]
  except KeyError:
    logging.error(f"\nThe spelling of the language you are specifying is incorrect.\nSupported languages are {', '.join([f'’{i}’' for i in lang_data.keys()])}.")
    return ""

  # set timezone
  tz_data: tz = timezone_data.get(timezone) or ld.timezone

  if datetime.tzinfo is None:
    datetime = datetime.replace(tzinfo=tz_data)

  seconds = (elapsed_time(tz_data, datetime)).total_seconds()
  intervals = {
    'year': 31536000, 
    'month': 2592000, 
    'week': 604800, 
    'day': 86400, 
    'hour': 3600, 
    'minute': 60
  }

  for k, v in intervals.items():
    interval = seconds / v
    if interval > 1:
      return format.format(str(math.floor(interval)), getattr(ld, k), ld.ago)
  return format.format(str(math.floor(seconds)), ld.second, ld.ago)


if __name__ == '__main__':
  print(approximated_time(dt(2021, 10, 10, 12, 38, 39, 32734), 'ja'))