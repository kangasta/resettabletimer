# resettabletimer

[![CI](https://github.com/kangasta/resettabletimer/actions/workflows/ci.yml/badge.svg)](https://github.com/kangasta/resettabletimer/actions/workflows/ci.yml)
[![Release](https://github.com/kangasta/resettabletimer/actions/workflows/release.yml/badge.svg)](https://github.com/kangasta/resettabletimer/actions/workflows/release.yml)

Wrapper for `threading.Timer` to provide a resettable Timer implementation. Also provides fake timer for testing.

## Usage

### ResettableTimer

```python
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

Check and automatically fix formatting with:

```bash
pycodestyle resettabletimer
autopep8 -aaar --in-place resettabletimer
```

Run static analysis with:

```bash
pylint -E --enable=invalid-name,unused-import,useless-object-inheritance resettabletimer
```

Run unit tests:

```bash
# Run unit tests
python3 -m unittest discover -s tst/

# Run unit tests with coverage analysis
coverage run \
    --branch \
    --source resettabletimer/ \
    -m unittest discover -s tst/
coverage report -m
```
