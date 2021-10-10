from datetime import timezone as tz,\
  timedelta as td
# from collections import namedtuple
from typing import NamedTuple

from lang.timezone import *

# https://publib.boulder.ibm.com/tividd/td/TWS/SC32-1274-02/ja_JA/HTML/SRF_mst269.htm

class LangData(NamedTuple):
  second: str
  minute: str
  hour: str
  month: str
  day: str
  week: str
  year: str
  ago: str
  timezone: tz

# LangageData = namedtuple('langdata', [
#   'second',
#   'minute',
#   'hour',
#   'month',
#   'day',
#   'week',
#   'year',
#   'ago',
#   'timezone',
# ])

en = LangData(
  'seconds',
  'minutes',
  'hour',
  'month',
  'day',
  'week',
  'year',
  'ago',
  UTC,
)

ja = LangData(
  '秒',
  '分',
  '時間',
  'か月',
  '日',
  '週間',
  '年',
  '前',
  JST,
)

lang_data = {
  'en': en,
  'ja': ja,
}