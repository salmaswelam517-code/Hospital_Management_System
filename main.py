import customtkinter as ctk
from tkinter import messagebox
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
from database import load_data, save_data, validate_patient
from patient import Patient
from hospital import Hospital
from appointments import book_appointment, cancel_appointment
class HospitalGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.hospital_system=Hospital()
        self.hospital_system.patients = load_data()
        self.title("Hospital Management System")
        self.geometry("850x500")
        self.minsize(750, 450)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_sidebar()
        self.create_frames()
        self.show_frame(self.frame_patients)
        
    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        logo = ctk.CTkLabel(self.sidebar, text="Hospital Menu", font=ctk.CTkFont(size=16, weight="bold"))
        logo.pack(pady=30, padx=15)
        ctk.CTkButton(self.sidebar, text="Patients", command=lambda: self.show_frame(self.frame_patients)).pack(pady=10, padx=15, fill="x")
        ctk.CTkButton(self.sidebar, text="Appointments", command=lambda: self.show_frame(self.frame_appointments)).pack(pady=10, padx=15, fill="x")
        ctk.CTkButton(self.sidebar, text="Search & View", command=lambda: self.show_frame(self.frame_search)).pack(pady=10, padx=15, fill="x")
    def create_frames(self):
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.frame_patients = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frame_appointments = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frame_search = ctk.CTkFrame(self.container, fg_color="transparent")

        for frame in (self.frame_patients, self.frame_appointments, self.frame_search):
            frame.grid(row=0, column=0, sticky="nsew")

        self.setup_patients_ui()
        self.setup_appointments_ui()
        self.setup_search_ui()
    def show_frame(self, frame):
        frame.tkraise()
    def setup_patients_ui(self):
        lbl = ctk.CTkLabel(self.frame_patients, text="Patient Operations", font=ctk.CTkFont(size=15, weight="bold"))
        lbl.pack(pady=10)
        self.e_id = ctk.CTkEntry(self.frame_patients, placeholder_text="Patient ID")
        self.e_id.pack(pady=5, fill="x", padx=30)
        self.e_name = ctk.CTkEntry(self.frame_patients, placeholder_text="Patient Name")
        self.e_name.pack(pady=5, fill="x", padx=30)
        self.e_age = ctk.CTkEntry(self.frame_patients, placeholder_text="Age")
        self.e_age.pack(pady=5, fill="x", padx=30)
        self.e_disease = ctk.CTkEntry(self.frame_patients, placeholder_text="Disease")
        self.e_disease.pack(pady=5, fill="x", padx=30)
        self.e_doctor = ctk.CTkEntry(self.frame_patients, placeholder_text="Doctor Name")
        self.e_doctor.pack(pady=5, fill="x", padx=30)
        btns_frame = ctk.CTkFrame(self.frame_patients, fg_color="transparent")
        btns_frame.pack(pady=15)
        ctk.CTkButton(btns_frame, text="Add", fg_color="green", width=90, command=self.on_add).pack(side="left", padx=5)
        ctk.CTkButton(btns_frame, text="Update", fg_color="green", width=90, command=self.on_update).pack(side="left", padx=5)
        ctk.CTkButton(btns_frame, text="Delete", fg_color="green", width=90, command=self.on_delete).pack(side="left", padx=5)
        ctk.CTkButton(btns_frame, text="+ Visit", fg_color="green", width=90, command=self.on_visit).pack(side="left", padx=5)
    def setup_appointments_ui(self):
        lbl = ctk.CTkLabel(self.frame_appointments, text="Appointments Management", font=ctk.CTkFont(size=15, weight="bold"))
        lbl.pack(pady=10)
        self.app_id = ctk.CTkEntry(self.frame_appointments, placeholder_text="Patient ID")
        self.app_id.pack(pady=10, fill="x", padx=30)
        self.app_doctor = ctk.CTkEntry(self.frame_appointments, placeholder_text="Doctor Name")
        self.app_doctor.pack(pady=10, fill="x", padx=30)
        ctk.CTkButton(self.frame_appointments, text="Book Appointment", command=self.on_book).pack(pady=10)
        ctk.CTkButton(self.frame_appointments, text="Cancel Appointment", fg_color="red", command=self.on_cancel).pack(pady=5)
    def setup_search_ui(self):
        lbl = ctk.CTkLabel(self.frame_search, text="Search & View Patients", font=ctk.CTkFont(size=15, weight="bold"))
        lbl.pack(pady=10)
        self.search_entry = ctk.CTkEntry(self.frame_search, placeholder_text="Search by Name or ID")
        self.search_entry.pack(pady=5, fill="x", padx=30)
        ctk.CTkButton(self.frame_search, text="Search", command=self.on_search).pack(pady=10)
        self.result_box = ctk.CTkTextbox(self.frame_search, width=450, height=200)
        self.result_box.pack(pady=10)
    def on_add(self):
        p_id = self.e_id.get().strip()
        name = self.e_name.get().strip()
        age = self.e_age.get().strip()
        disease = self.e_disease.get().strip()
        doctor = self.e_doctor.get().strip()

        if validate_patient(p_id, name, age, doctor, disease, self.hospital_system.patients):
            self.hospital_system.add_patient(p_id, name, int(age), disease, doctor)
            save_data(self.hospital_system.patients)
            messagebox.showinfo("Success", f"Patient '{name}' added successfully!")
        else:
            messagebox.showerror("Error", "Invalid inputs or Patient ID already exists!")
    def on_update(self):
        p_id = self.e_id.get().strip()
        if p_id in self.hospital_system.patients:
            name = self.e_name.get().strip() or self.hospital_system.patients[p_id]['name']
            age_str = self.e_age.get().strip()
            age = int(age_str) if age_str.isdigit() else self.hospital_system.patients[p_id]['age']
            disease = self.e_disease.get().strip() or self.hospital_system.patients[p_id]['disease']
            doctor = self.e_doctor.get().strip() or self.hospital_system.patients[p_id]['doctor']
            self.hospital_system.update_patient(p_id, name, age, disease, doctor)
            save_data(self.hospital_system.patients)
            messagebox.showinfo("Success", f"Patient ID {p_id} updated successfully!")
        else:
            messagebox.showerror("Error", "Patient ID not found!")
    def on_delete(self):
        p_id = self.e_id.get().strip()
        if p_id in self.hospital_system.patients:
            self.hospital_system.delete_patient(p_id)
            save_data(self.hospital_system.patients)
            messagebox.showinfo("Success", f"Patient ID {p_id} deleted successfully!")
        else:
            messagebox.showerror("Error", "Patient ID not found!")
    def on_visit(self):
        p_id = self.e_id.get().strip()
        if p_id in self.hospital_system.patients:
            self.hospital_system.add_visit(p_id)
            save_data(self.hospital_system.patients)
            total_visits = self.hospital_system.patients[p_id]['visits']
            messagebox.showinfo("Success", f"Visit added! Total visits: {total_visits}")
        else:
            messagebox.showerror("Error", "Patient ID not found!")
    def on_book(self):
        p_id = self.app_id.get().strip()
        doctor = self.app_doctor.get().strip()
        if p_id in self.hospital_system.patients:
            messagebox.showinfo("Success", f"Appointment booked for Patient ID {p_id} with Dr. {doctor}!")
        else:
            messagebox.showerror("Error", "Patient ID not found!")
    def on_cancel(self):
        p_id = self.app_id.get().strip()
        if p_id in self.hospital_system.patients:
            messagebox.showinfo("Success", f"Appointment cancelled for Patient ID {p_id}!")
        else:
            messagebox.showerror("Error", "Patient ID not found!")
    def on_search(self):
        query = self.search_entry.get().strip()
        self.result_box.delete("1.0", "end")

        found = False
        for pid, data in self.hospital_system.patients.items():
            if not query or query == pid or query.lower() in data['name'].lower():
                output = (
                    f"ID: {pid} | Name: {data['name']} | Age: {data['age']} | "
                    f"Disease: {data['disease']} | Doctor: {data['doctor']} | Visits: {data['visits']}\n"
                )
                self.result_box.insert("end", output)
                found = True
        if not found:
            self.result_box.insert("end", "No matching patient records found.")

if __name__ == "__main__":
    app = HospitalGUI()
    app.mainloop()