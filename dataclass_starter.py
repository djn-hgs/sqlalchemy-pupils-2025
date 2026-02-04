from dataclasses import dataclass
import datetime


@dataclass
class Pupil:
    first_name: str
    second_name: str
    date_of_birth: datetime.date
    house: 'House'

@dataclass
class House:
    house_name: str

mg = House('Midgate')

rb = Pupil('Rosalia', 'Bialek', datetime.date(2009,5,13), mg)
hme = Pupil('Henry', 'Miller Evans', datetime.date(2009,4,14), House('Eastgate'))

print(rb)
print(hme)

