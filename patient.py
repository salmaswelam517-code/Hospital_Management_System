class Patient:
    name: str
    age: int
    disease: str
    doctor: str
    visit_count: int

    def __init__(
        self,
        name: str,
        age: int,
        disease: str,
        doctor: str,
        visit_count: int
    ):
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor = doctor
        self.visit_count = visit_count

    def __repr__(self) -> str:
        return (f"Patient(Name={self.name}, "
                f"Age={self.age}, "
                f"Disease={self.disease}, "
                f"Doctor={self.doctor}, "
                f"Visit Count={self.visit_count})")

p1 = Patient("Ahmed Ali", 25, "Flu", "Dr. Sara", 2)
p2 = Patient("Mona Hassan", 30, "Diabetes", "Dr. Omar", 5)
p3 = Patient("Youssef Adel", 18, "Cold", "Dr. Sara", 1)
p4 = Patient("Nour Mohamed", 40, "Hypertension", "Dr. Ali", 7)
p5 = Patient("Khaled Samy", 35, "Asthma", "Dr. Omar", 3)
p6 = Patient("Walied Tarek", 22, "Migraine", "Dr. Ali", 4)
p7 = Patient("Hana Mostafa", 28, "Anemia", "Dr. Sara", 2)

patients = [p1, p2, p3, p4, p5, p6, p7]

for patient in patients:
    print(patient)