class Hospital:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, disease, doctor):
        if patient_id in self.patients:
            print("This ID already exists")
        else:
            self.patients[patient_id] = {
                "name": name,
                "age": age,
                "disease": disease,
                "doctor": doctor,
                "visits": 1
            }
            print(f"Patient {name} added successfully")

    def search_by_id(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            
            print(f"\n Patient Info for ID: {patient_id} ")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Disease: {patient['disease']}")
            print(f"Doctor: {patient['doctor']}")
            print(f"Visits: {patient['visits']}\n")
        else:
            print("Patient not found")

    def search_by_name(self, name):
        for patient_id in self.patients:
            patient = self.patients[patient_id]
            
            if patient["name"].lower() == name.lower():
                print(f"\nFound Patient (ID: {patient_id})")
                print(f"Name: {patient['name']}")
                print(f"Age: {patient['age']}")
                print(f"Disease: {patient['disease']}")
                print(f"Doctor: {patient['doctor']}")
                print(f"Visits: {patient['visits']}\n")
                break
        
        else:
            print("Patient not found")

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient deleted successfully")
        else:
            print("Patient not found")

    def update_patient(self, patient_id, name, age, disease, doctor):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient["name"] = name
            patient["age"] = age
            patient["disease"] = disease
            patient["doctor"] = doctor
            print("Patient updated successfully")
        else:
            print("Patient not found")

    def add_visit(self, patient_id):
        if patient_id in self.patients:
            self.patients[patient_id]["visits"] += 1
            print(f"Visit added. Total visits now: {self.patients[patient_id]['visits']}")
        else:
            print("Patient not found")