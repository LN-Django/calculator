from django.core.exceptions import ValidationError

def validate_num(s):
    
    try:
        float(s)
        if (float(s)<=0):
            return False
        return True
    except ValueError:
        return False