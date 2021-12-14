# Approximate-elapsed-time
Returns the approximate elapsed time by language.

# Usage
Run the sample code
```python
python3 main.py
```

## EN
```python
from main import approximated_time
from datetime import datetime

# now 2021-10-10 13:24:18.427468
input_datetime = datetime(2021, 10, 10, 13, 24, 29, 427468)

approximated_time(input_datetime, 'en')
# 11 seconds ago

#Outputs the approximate time for each elapsed time.
/*
  11 seconds ago
  .
  8 hours ago
  .
  1 days ago
  .
  .
  1　weeks ago
  .
*/
```

## JP - ja
```python
approximated_time(input_datetime, 'ja')
# 11 秒前

#経過時間ごとにおおよその時間を出力します。
/*
  11 秒前
  .
  .
  1 日前
  .
  .
  1　週間前
*/
```

## options
The time zone is automatically set for each language, but you can also set it manually.
```python
approximated_time(input_datetime, 'en', timezone='JST')
```

You can specify the output format. From top to bottom are time, units, and 'ago'.
```python
approximated_time(input_datetime, 'en', format='{}-{}-{}')
# 11-seconds-ago
```
