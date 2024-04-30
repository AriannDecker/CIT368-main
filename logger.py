import valid
import setup
import os

def log(s):
    if not valid.log(s):
        return
    
    if not setup.LOGGING:
        return
    
    try:
        append = 'a' if os.path.getsize(setup.LOG_FILE) < 1000000 else 'w'
        
        with open(setup.LOG_FILE, append) as f:
            f.writelines(s + '\n')
    except:
        return