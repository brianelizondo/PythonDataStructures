def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_freq = { number: str(num1).count(number) for number in "1234567890"}
    num2_freq = { number: str(num2).count(number) for number in "1234567890"}
    return num1_freq == num2_freq