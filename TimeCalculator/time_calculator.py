def add_time(init, add, showD=False):
    semana = [
        ['monday'],
        ['tuesday'],
        ['wednesday'],
        ['thursday'],
        ['friday'],
        ['saturday'],
        ['sunday'],
    ]
    showD = showD.lower()
    dayS = 0
    for k, c in enumerate(semana):
        if c[0] == showD:
            dayS = k
    restday = 0
    hr = init.split(' ')[0].replace(':','.')
    timed = init.split(' ')[1]
    hr = hr.replace(':','.')
    addhr = add.replace(':','.')
    
    sthr = hr.split('.')[0]
    endhr = hr.split('.')[1]
    
    stadd = addhr.split('.')[0]
    endadd = addhr.split('.')[1]
    
    stfinal = int(sthr) + int(stadd)
    days = 0
    while stfinal >= 24:
        stfinal = stfinal - 24
        days+=1
    dayS = dayS + days
    while dayS > 6:
        dayS -= 7
    dayspassed = ''
    if days == 1:
        dayspassed = '(next day)'
    else:
        dayspassed = f'({days} days later)'
    scfinal = int(endhr) + int(endadd)
    if scfinal >= 60:
        scfinal = scfinal - 60
        stfinal = int(stfinal) + 1
    som = str(stfinal) + '.' + str(scfinal)
    if timed == 'PM' and (12 - float(som)) <= 0:
        timed = 'AM'
    elif timed == 'AM' and (12 - float(som)) <= 0:
        timed = 'PM' 


    return f'{stfinal}:{scfinal} {timed}, {semana[dayS][0]} {dayspassed} {days} {dayS}'