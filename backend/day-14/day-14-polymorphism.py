class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum
    
    def _digits(self, number):
        digit = 0
        while number != 0:
            digit+=1
            number//=10

        return digit
    
    def product(self, numlist):
        _product = 1
        
        for num in numlist:
            if self._digits(num) > 3:
                raise ValueError("Basic Calculator can only handle 3 digits.")
            _product *= num

        return _product

class ComplexCalculator(BasicCalculator):
    def power(base, exponent):
        return base ** exponent

    def abs(number):
        if number >= 0:
            return number
        return -number
    
    def product(self, numlist):
        _product = 1
        
        for num in numlist:
            if self._digits(num) > 8:
                raise ValueError("Complex Calculator can only handle 8 digits.")
            _product *= num

        return _product
    
basic = BasicCalculator()
complex = ComplexCalculator()
