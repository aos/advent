# Day 4 - Puzzle 2


from datetime import datetime
from part_1 import sort_input, create_calendar, DATETIME_FORMAT


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
    sorted_input = sort_input(f)
    real_cal = create_calendar(sorted_input)
    return find_total(real_cal)


print(solve('./day04-input.txt'))

# Tests
test_input = sort_input('./day04-example.txt')
test_cal = create_calendar(test_input)
test_total = find_total(test_cal)
assert(test_input[0] ==
       (datetime.strptime('1518-11-01 00:00', DATETIME_FORMAT),
        'Guard #10 begins shift'))
assert(test_input[-1] ==
       (datetime.strptime('1518-11-05 00:55', DATETIME_FORMAT),
        'wakes up'))
assert(test_total == 4455)
print('All tests passed!')
