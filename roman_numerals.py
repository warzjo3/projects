# roman numerals converter

example = 'MCMXVII' # 1917

def numerals(numeral = input('enter a roman numeral: ')):
    numerals = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    numbers = []
    for letter in range(len(numeral)) :
        number = (numerals[numeral[letter]])
        numbers.append(number)
        try:
            for i in range(len(numbers)):
                if numbers[i] < numbers[i+1]:
                    numbers[i] = -numbers[i]
        except IndexError:
            pass
        total = sum(numbers)
        
    return total
    
print(numerals())