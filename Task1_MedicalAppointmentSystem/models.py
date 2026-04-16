from abc import ABC, abstractmethod
from datetime import datetime

class Person(ABC):
    def __init__(self, pid: str, name: str, phone: str):
        self._pid = pid
        self.name = name
        self.phone = phone
        
    def display_info(self) -> str:
        pass

class Patient(Person):
    def __init__(self, pid: str, name: str, phone: str, dob: str):
        super().__init__(pid, name, phone)
        self.dob = dob
        self.medical_records = []

    def add_record(self, record: 'MedicalRecord'):
        self.medical_records.append(record)

    def display_info(self) -> str:
        return f"Patient [{self._pid}] {self.name} | Phone: {self.phone} | DOB: {self.dob}"

class Doctor(Person):
    def __init__(self, pid: str, name: str, phone: str, specialty: str):
        super().__init__(pid, name, phone)
        self.specialty = specialty

    def display_info(self) -> str:
        return f"Doctor [{self._pid}] Dr. {self.name} | Specialty: {self.specialty}"

class MedicalRecord:
    def __init__(self, date: str, diagnosis: str, prescription: str, notes: str = ""):
        self.date = date
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.notes = notes

    def __str__(self):
        return f"{self.date} | Diagnosis: {self.diagnosis} | Prescription: {self.prescription}"

class Appointment:
    def __init__(self, app_id: str, patient: Patient, doctor: Doctor, datetime_str: str):
        self.app_id = app_id
        self.patient = patient
        self.doctor = doctor
        self.datetime = datetime_str
        self.status = "Booked"
        
    def __str__(self):
        return (f"Appointment[{self.app_id}] {self.datetime} | "
                f"{self.patient.name} → Dr.{self.doctor.name} ({self.doctor.specialty}) | Status: {self.status}")
