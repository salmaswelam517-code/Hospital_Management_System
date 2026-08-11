import json

FILE_NAME = "patients.json"

def load_data():

    try:
        with open(FILE_NAME, "r") as file:
            patients = json.load(file)

            if isinstance(patients, dict):
                return patients
            else:
                return {}

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("JSON file is empty or corrupted.")
        return {}

    except Exception as error:
        print("Loading Error:", error)
        return {}

    finally:
        print("Load operation completed.")

def save_data(patients):

    try:

        with open(FILE_NAME, "w") as file:
            json.dump(patients, file, indent=4)

        print("Data saved successfully.")

    except Exception as error:
        print("Saving Error:", error)

    finally:
        print("Save operation completed.")

def validate_patient(patient_id, name, age, doctor, disease, patients):

    if patient_id.strip() == "":
        print("Patient ID cannot be empty.")
        return False

    if patient_id in patients:
        print("Patient ID already exists.")
        return False

    if name.strip() == "":
        print("Name cannot be empty.")
        return False

    if doctor.strip() == "":
        print("Doctor name cannot be empty.")
        return False

    if disease.strip() == "":
        print("Disease cannot be empty.")
        return False

    if age.strip() == "":
        print("Age cannot be empty.")
        return False

    if not age.isdigit():
        print("Age must be a number.")
        return False

    age = int(age)

    if age <= 0:
        print("Age must be greater than zero.")
        return False

    return True

def add_patient():

    patients = load_data()

    try:

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        doctor = input("Enter Doctor Name: ")
        disease = input("Enter Disease: ")

        if validate_patient(patient_id, name, age, doctor, disease, patients):

            patients[patient_id] = {

                "name": name,
                "age": int(age),
                "doctor": doctor,
                "disease": disease,
                "visits": 0

            }

            save_data(patients)

            print("Patient added successfully.")

    except ValueError:
        print("Invalid input.")

    except KeyboardInterrupt:
        print("\nOperation cancelled.")

    except Exception as error:
        print("Unexpected Error:", error)

    finally:
        print("Program finished.")

if __name__ == "__main__":
    add_patient()