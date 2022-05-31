def add_time(init, add, showD=False):
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
    scfinal = int(endhr) + int(endadd)
    if scfinal >= 60:
        scfinal = scfinal - 60
        stfinal = int(stfinal) + 1
    som = str(stfinal) + '.' + str(scfinal)
    if timed == 'PM' and (12 - float(som)) <= 0:
        timed = 'AM'
    elif timed == 'AM' and (12 - float(som)) <= 0:
        timed = 'PM' 


    return f'{som}'