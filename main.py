class Subject:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit


class Student:
    def __init__(self, name, limit=30):
        self.name = name
        self.limit = limit
        self.subjects = []

    def choose(self, subject):
        if self.total_credits() + subject.credit <= self.limit:
            self.subjects.append(subject)
            print(subject.name, "qo‘shildi")
        else:
            print("Kredit limiti oshib ketdi")

    def total_credits(self):
        return sum(s.credit for s in self.subjects)

    def report(self):
        print(self.name, "| Kredit:", self.total_credits())
        for s in self.subjects:
            print("-", s.name)


math = Subject("Matematika", 6)
python = Subject("Python", 8)

st = Student("Jahongir")
st.choose(math)
st.choose(python)
st.report()
