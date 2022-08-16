def is_leap(year):
    leap = False

    # Write your logic here
    if 1900<=year<=100000:
        if year%400 == 0:
            leap = True

        elif year%4 == 0 and year%100 != 0:
            leap = True

        else:
            leap = False
        
    else:
        leap = False
            
    return leap

year = int(input())
print(is_leap(year))