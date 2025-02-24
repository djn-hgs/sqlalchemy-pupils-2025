from dataclasses import dataclass


@dataclass
class Pupil:
    name: str
    age: int

hf = Pupil('Holly', 17)

print(hf)
