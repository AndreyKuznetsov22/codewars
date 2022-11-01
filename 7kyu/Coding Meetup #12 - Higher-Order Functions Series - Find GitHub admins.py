def find_admin(lst, lang): 
    return [x for x in lst if x['githubAdmin'] == 'yes' and x['language'] == lang]