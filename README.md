# resettabletimer
[![Build Status](https://travis-ci.org/kangasta/resettabletimer.svg?branch=master)](https://travis-ci.org/kangasta/resettabletimer)

Wrapper for `threading.Timer` to provide a resettable Timer implementation. Also provides fake timer for testing.

## Usage

### ResettableTimer

```python
# If using python 2, import print function
from __future__ import print_function

from resettabletimer import ResettableTimer

delay = 5 # seconds
function = print

# Create resettable timer
t = ResettableTimer(delay, function, ["Hello"], {"end":" timer!\n"})

# Starting and canceling work similarly than with threading.Timer
t.start()

# Wait 1-5 seconds

# Reset the timer
t.reset()

# Hello should be printed after five seconds

```

### FakeTimer

```python
# If using python 2, import print function
from __future__ import print_function

from resettabletimer import FakeTimer

t = FakeTimer(2, print, ["Hello"], {"end":" timer!\n"})

# Starting and canceling work similarly than with threading.Timer
t.start()

# Wait >2 seconds
# Nothing happens

# Time passage is controlled with pass_time
t.pass_time(2)

# Hello should be printed

```

## Testing

Run unit tests with command:

```bash
cd resettabletimer

python3 -m unittest discover -s tst/
```

Get test coverage with commands:
```bash
cd resettabletimer

coverage run -m unittest discover -s tst/
coverage report -m
```
