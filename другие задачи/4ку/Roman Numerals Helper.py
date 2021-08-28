class RomanNumerals:
    dictionary = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000, 'CM': 900,
        'CD': 400, 'XC': 90,
        'XL': 40, 'IX': 9, 'IV': 4,
    }
    dictionary_reverse = {value: key for key, value in dictionary.items()}

    @staticmethod
    def from_roman(roman):
        number = 0
        number_list = [RomanNumerals.dictionary[integer] for integer in roman] + [-1]
        for i in range(0, len(number_list) - 1):
            if number_list[i] < number_list[i + 1]:
                number += (number_list[i + 1] - number_list[i])
                number_list[i + 1] = 1001
            elif number_list[i] != 1001:
                number += number_list[i]
        return number

    @staticmethod
    def decompose_numbers(digit, number_bit_depth):
        if 5 < digit < 9:
            return '5' + '0' * (number_bit_depth - 1) + ',' + ('1' + '0' * (number_bit_depth - 1) + ',') * (digit - 5)
        elif digit < 4:
            return ('1' + '0' * (number_bit_depth - 1) + ',') * digit

        else:
            return f"{digit}" + '0' * (number_bit_depth - 1) + ','

    @staticmethod
    def to_roman(number):

        roman_list = ''.join([RomanNumerals.decompose_numbers(int(str(number)[x]), len(str(number)) - x)
                              for x in range(len(str(number)))]).split(',')[:-1]
        return ''.join([RomanNumerals.dictionary_reverse[int(x)] for x in roman_list])



r = RomanNumerals()
print(RomanNumerals.to_roman(1259))
