# Day 4 - Puzzle 1
# What is the ID of the guard you chose multiplied by the minute you chose?


from datetime import datetime
import re
DATETIME_FORMAT = '%Y-%m-%d %H:%M'


def sort_input(file):
    s = []
    with open(file) as f:
        for line in f:
            dt, action = re.match(r'^\[(.+)]\s(.*)', line.strip()).groups()
            dt = datetime.strptime(dt, DATETIME_FORMAT)
            s.append((dt, action))

    s.sort(key=lambda i: i[0])
    return s


def create_calendar(inp):
    table = {}
    current_guard = None
    time_slept = None

    for dt, action in inp:
        # Guard begins shift, let's grab the ID
        if '#' in action:
            current_guard = re.search(r'(#\d+)', action).group(1)
            if current_guard not in table:
                table[current_guard] = [0 for i in range(60)]
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


def _find_guard(cal):
    t = {}
    largest = 0
    g = ''
    for guard, times in cal.items():
        if guard not in t:
            t[guard] = 0

        t[guard] = sum(times)

    for guard, hours in t.items():
        if hours > largest:
            g = guard
            largest = hours

    return g


def _find_total(guard_id, guard_cal):
    m = 0
    i = 0

    for index, value in enumerate(guard_cal):
        if value > m:
            m = value
            i = index

    return i * int(guard_id.replace('#', ''))


if __name__ == '__main__':
    def solve(f):
        sorted_input = sort_input(f)
        real_cal = create_calendar(sorted_input)
        real_guard = _find_guard(real_cal)
        return _find_total(real_guard, real_cal[real_guard])

    print(solve('./day04-input.txt'))

    # Tests
    test_input = sort_input('./day04-example.txt')
    cal = create_calendar(test_input)
    guard_id = _find_guard(cal)
    total = _find_total(guard_id, cal[guard_id])
    assert(test_input[0] ==
           (datetime.strptime('1518-11-01 00:00', DATETIME_FORMAT),
            'Guard #10 begins shift'))
    assert(test_input[-1] ==
           (datetime.strptime('1518-11-05 00:55', DATETIME_FORMAT),
            'wakes up'))
    assert(guard_id == '#10')
    assert(total == 240)
    print('All tests passed!')
