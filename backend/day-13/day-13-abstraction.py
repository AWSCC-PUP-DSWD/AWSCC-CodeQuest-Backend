class Calculator:
    def sum(self, numlist: list):
        _sum = 0
        for num in numlist:
            _sum += num

        return _sum

numlist = [5, 10, 15, 20, 25]
new_calculator = Calculator()
sum = new_calculator.sum(numlist)
print(sum)