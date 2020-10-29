from random import choice,choices
def Zusatzzahl():
    numbers=[x for x in range(1,11)]
    return choice(numbers)
def lottoSamstag():
    '''6 Aus 49'''
    numbers=[i for i in range(1,50) ]
    zahlen=choices(numbers,k=6)
    return sorted(zahlen),Zusatzzahl()

zahlen=[]
zahlen,zusatz=lottoSamstag()
print(f'Die Zahlen der heutigen Ziehung sind{zahlen}, die Zustatzzahl ist {zusatz}. Allen Gewinnern herzlichen Glückwunsch')