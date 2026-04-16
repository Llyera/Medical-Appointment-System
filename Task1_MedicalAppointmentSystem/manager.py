from models import Patient, Doctor, Appointment, MedicalRecord

class ClinicManager:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, pid: str, name: str, phone: str, dob: str) -> bool:
        if pid in self.patients:
            print("Error: Patient ID already exists!")
            return False
        self.patients[pid] = Patient(pid, name, phone, dob)
        return True

    def add_doctor(self, pid: str, name: str, phone: str, specialty: str) -> bool:
        if pid in self.doctors:
            print("Error: Doctor ID already exists!")
            return False
        self.doctors[pid] = Doctor(pid, name, phone, specialty)
        return True

    def book_appointment(self, aid: str, pid: str, did: str, datetime_str: str) -> bool:
        if pid not in self.patients:
            print("Error: Patient not found!")
            return False
        if did not in self.doctors:
            print("Error: Doctor not found!")
            return False
        if aid in self.appointments:
            print("Error: Appointment ID already exists!")
            return False

        patient = self.patients[pid]
        doctor = self.doctors[did]
        self.appointments[aid] = Appointment(aid, patient, doctor, datetime_str)
        return True

    def get_patient_records(self, pid: str):
        if pid not in self.patients:
            print("Error: Patient not found!")
            return None
        return self.patients[pid].medical_records

    def add_medical_record(self, pid: str, date: str, diagnosis: str, prescription: str, notes: str = ""):
        if pid not in self.patients:
            print("Error: Patient not found!")
            return False
        record = MedicalRecord(date, diagnosis, prescription, notes)
        self.patients[pid].add_record(record)
        print(f"Medical record added for patient {pid}")
        return True

    def view_all_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        for app in self.appointments.values():
            print(app)
