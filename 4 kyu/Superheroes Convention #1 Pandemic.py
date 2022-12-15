#https://www.codewars.com/kata/6202149e89771200306428f0

def is_possible(db: dict) -> bool:
    db  = dict(db)
    stk = list(db)
    day = [0] * len(db)
    
    while stk:
        a = stk.pop()
        if a not in db: continue
        
        lst    = db.pop(a)
        day[a] = day[a] or 1
        oppDay = day[a] ^ 3
        for b in lst: 
            if day[b] and day[b] != oppDay: return False
            day[b] = oppDay
        
        stk.extend(lst)
    return True