def is_leap(year):
    """
    Determines whether a given year is a leap year.
    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))



'''son=int(input('son kiriting: '))

if son % 2 == 1:
    print('weird')
elif son%2==0 and 2<=son<=5:
    print('not weird')   
elif son%2==0 and 6<=son<=20:
    print('weird')
elif son%2==0 and son>20:
    print('not weird')  '''
