def proofread(s):    
    return '. '.join(i.lower().replace('ie', 'ei').capitalize() for i in s.split('. '))
