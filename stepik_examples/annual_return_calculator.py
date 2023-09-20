def annual_return(start, percent, years):
    equation_percent = percent / 100
    res = []
    current = start
    for year in range(years):
        res.append(current)
        current = start * equation_percent
    return iter(res)