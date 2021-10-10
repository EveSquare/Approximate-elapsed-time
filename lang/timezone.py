from datetime import \
  timedelta as td,\
  timezone as tz

UTC = tz.utc
JST = tz(td(hours=9), 'JST')

timezone_data = {
  'UTC': UTC,
  'JST': JST,
}