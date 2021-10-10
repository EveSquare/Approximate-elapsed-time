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
now = datetime.now()

approximated_time(now, 'en')
# 11 seconds ago

#Outputs the approximate time for each elapsed time.
/*
  11 seconds ago
  .
  8 hour ago
  .
  1 day ago
  .
  .
  1　week ago
  .
*/

```

## JP - ja
```python
approximated_time(now, 'ja')
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