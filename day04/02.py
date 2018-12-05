# Day 4 - Puzzle 2


from datetime import datetime
import re
DATETIME_FORMAT = '%Y-%m-%d %H:%M'


def _sort_input(file):
    s = []
    with open(file) as f:
        for line in f:
            dt, action = re.match(r'^\[(.+)]\s(.*)', line.strip()).groups()
            dt = datetime.strptime(dt, DATETIME_FORMAT)
            s.append((dt, action))

    s.sort(key=lambda i: i[0])
    return s


def _create_calendar(inp):
    table = {}
    current_guard = None
    time_slept = None

    for dt, action in inp:
        # Guard begins shift, let's grab the ID
        if '#' in action:
            i = re.search(r'(#\d+)', action).group(1)
            current_guard = i
            if i not in table:
                table[i] = [0 for i in range(60)]
            continue

        # Guard falls asleep, keep track of when they did
        if 'falls asleep' in action:
            time_slept = dt
            continue

        # Guard wakes up, add up the minutes they slept
        if 'wakes up' in action:
            start_time = time_slept.minute
            end_time = dt.minute
            for i in range(start_time, end_time):
                table[current_guard][i] += 1
            continue

    return table


def find_total(cal):
    minute = 0
    guard = ''
    max_slept = 0

    for guard_id, times in cal.items():
        slept = max(times)
        if slept > max_slept:
            minute = times.index(slept)
            max_slept = slept
            guard = guard_id

    return int(guard.replace('#', '')) * minute


def solve(f):
    sorted_input = _sort_input(f)
    real_cal = _create_calendar(sorted_input)
    return find_total(real_cal)


print(solve('./day04-input.txt'))

# Tests
test_input = _sort_input('./day04-example.txt')
test_cal = _create_calendar(test_input)
test_total = find_total(test_cal)
assert(test_input[0] ==
       (datetime.strptime('1518-11-01 00:00', DATETIME_FORMAT),
        'Guard #10 begins shift'))
assert(test_input[-1] ==
       (datetime.strptime('1518-11-05 00:55', DATETIME_FORMAT),
        'wakes up'))
assert(test_total == 4455)
print('All tests passed!')
