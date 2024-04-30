import re

def zipcode(zipcode):
    if not zipcode:
        return False
    
    return re.match(r'^\d{5}$', zipcode)

def weather(dict):
    if not dict:
        return False
    
    try:
        int(dict['dt'])
        float(dict['main']['temp'])
        str(dict['weather'][0]['description'])
    except:
        return False
    
    return re.match(r'^[A-Za-z \']{3,50}$', dict['weather'][0]['description'])

def log(log):
    if not log or log.strip() == '':
        return False
    
    return re.match(r'[A-Za-z0-9 \'():]{3,150}', log)