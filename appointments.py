patients = []
timetable = []


def add_patient():
    patient_id = int(input("Enter Patient ID: "))

    patient_name = input("Enter Patient Name: ")

    patient_age = int(input("Enter Patient Age: "))

    patient_doctor = input("Enter Doctor Name: ")

    patient_disease = input("Enter Disease: ")

    patient_visits = int(input("Enter Number of Visited: "))

    patient = {
        "id": patient_id,
        "name": patient_name,
        "age": patient_age,
        "doctor": patient_doctor,
        "disease": patient_disease,
        "visits": patient_visits
    }

    patients.append(patient)

    print("Patient Added Successfully!")
def book_appointment():
    patient_id = int(input("Enter Patient ID: "))
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM): ")
    patient_found = False
    for patient in patients:
        if patient["id"] == patient_id:
            patient_found = True

            appointment = {
                "patient_id": patient_id,
                "doctor": patient["doctor"],
                "date": appointment_date,
                "time": appointment_time
            }

            for app in timetable:
                if (app["doctor"] == patient["doctor"]
                    and app["date"] == appointment_date
                    and app["time"] == appointment_time):
                    print("This appointment is already booked!")
                    return
            timetable.append(appointment)

            print("Appointment Booked Successfully!")
            break

    if patient_found == False:
        print("Patient Not Found!")


def display_doctor_patients():
    doctor_name = input("Enter Doctor Name to search for patients: ")

    found_any = False

    print(f"\n--- Patients assigned to Dr. {doctor_name} ---")

    count = 1

    for patient in patients:
        if patient["doctor"].lower() == doctor_name.lower():

            print(f"{count}. ID: {patient['id']} | Name: {patient['name']} | Age: {patient['age']} | Disease: {patient['disease']}")

            found_any = True
            count += 1

    if not found_any:
        print(f"No patients found for Dr. {doctor_name}")


def display_all_patients():
    print("\n--- All Patients ---")

    if len(patients) == 0:
        print("No Patients Found!")
        return

    for index, patient in enumerate(patients, start=1):
        print(f"{index}. ID: {patient['id']} | Name: {patient['name']} | Age: {patient['age']} | Doctor: {patient['doctor']} | Disease: {patient['disease']}")


def cancel_appointment():
    patient_id = int(input("Enter Patient ID: "))
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM): ")

    for appointment in timetable:
        if (appointment["patient_id"] == patient_id
            and appointment["date"] == appointment_date
            and appointment["time"] == appointment_time):

            timetable.remove(appointment)
            print("Appointment Cancelled Successfully!")
            return

    print("Appointment Not Found!")
if __name__ == "__main__":
    while True:
        print("\n--- Clinic Management System ---")
        print("1. Add Patient")
        print("2. Book Appointment")
        print("3. Display Doctor Patients")
        print("4. Display All Patients")
        print("5. Cancel Appointment")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_patient()

        elif choice == 2:
            book_appointment()

        elif choice == 3:
            display_doctor_patients()

        elif choice == 4:
            display_all_patients()

        elif choice == 5:
            cancel_appointment()

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")