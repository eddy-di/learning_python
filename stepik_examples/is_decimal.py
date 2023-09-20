def is_decimal(s):
    try:
        res = float(s) or int(s)
        if res:
            return True
    except ValueError:
        return False
    

print(is_decimal('100'))