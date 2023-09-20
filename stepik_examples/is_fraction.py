def is_fraction(string: str) -> bool:
    res = string.split('/')
    try:
        return True if int(res[0]) and int(res[1]) > 0 else False
    except ValueError:
        return False
    except IndexError:
        return False



