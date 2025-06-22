def add_time(start, duration, day=''):
    print('start:', start)
    print('duration:', duration)
    print()

    strp = start.split(':')
    shours = int(strp[0])
    sminutes = int(start[-5:-3])

    dhours = int(duration[:-3])
    dminutes = int(duration[-2:])
    
    add_min = sminutes + dminutes
    add_hours = shours + dhours
    ampm = start[-2:]

    if add_min >= 60:
        add_hours += 1
        add_min -= 60
    if add_min < 10:
        add_min = '0' + str(add_min)

    ndays = (add_hours // 24)

    if add_hours >= 12:
        # print()
        # print('add_hours:', add_hours)
        htwelves = (add_hours // 12)
        add_hours = add_hours - (12 * htwelves)

        if add_hours == 0:
            add_hours = 12
        
        if htwelves % 2 != 0:
            # print('htwelves:', htwelves)
            # print()
            if ampm == 'AM':
                ampm = 'PM'
            elif ampm == 'PM':
                ampm = 'AM'
                ndays += 1
    
    add_hours = str(add_hours)
    add_min = str(add_min)

    if day:
        day = day.lower().capitalize()
        week = [
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
        ]
        index = week.index(day)
        new_day = week[(index + ndays) % 7]
        
    if ndays == 1:
        daystr = '(next day)'
    elif ndays > 1:
        daystr = f'({ndays} days later)'
    else:
        daystr = ''
    
    new_time = f'{add_hours}:{add_min} {ampm}'

    if day:
        new_time += f', {new_day}'
    if daystr:
        new_time += f' {daystr}'

    print(new_time, '\n')
    return new_time
    

#add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

#add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

#add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

#add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

#add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

#add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)

print(add_time('11:59 PM', '24:05', 'Wednesday'))
