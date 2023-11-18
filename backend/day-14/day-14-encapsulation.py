from datetime import datetime

class Student:
    def __init__(self, name, birth_yr, birth_mo, birth_day):
        self.name = name
        self._birthdate = self._to_unixtime(birth_yr, birth_mo, birth_day)

    def _to_unixtime(self, yr, mo, d):
        return datetime(yr, mo, d).timestamp()        

    @property
    def birthdate(self):
        return datetime.fromtimestamp(self._birthdate).strftime("%B %d, %Y")

student1 = Student("John", 2002, 10, 5)
print(student1.birthdate)