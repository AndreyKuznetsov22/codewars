def case_sensitive(s):
    lowers = [x for x in s if not x.islower()]
    return [False, lowers] if len(lowers) > 0 else [True, []] 