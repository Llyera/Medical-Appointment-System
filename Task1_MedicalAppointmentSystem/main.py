from manager import ClinicManager

def main():
    manager = ClinicManager()
    print("Medical Appointment System (Task 1)")

    while True:
        print("\n" + "="*55)
        print("1. View All Patients")
        print("2. View All Doctors")
        print("3. Add New Patient")
        print("4. Add New Doctor")
        print("5. Book Appointment")
        print("6. Cancel Appointment")
        print("7. View Patient Records")
        print("8. Add Medical Record")
        print("9. View All Appointments")
        print("0. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            if not manager.patients:
                print("No patients yet.")
            for p in manager.patients.values():
                print(p.display_info())

        elif choice == "2":
            if not manager.doctors:
                print("No doctors yet.")
            for d in manager.doctors.values():
                print(d.display_info())

        elif choice == "3":
            pid = input("Patient ID: ").strip()
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            manager.add_patient(pid, name, phone, dob)

        elif choice == "4":
            pid = input("Doctor ID: ").strip()
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            spec = input("Specialty: ").strip()
            manager.add_doctor(pid, name, phone, spec)

        elif choice == "5":
            aid = input("Appointment ID: ").strip()
            pid = input("Patient ID: ").strip()
            did = input("Doctor ID: ").strip()
            dt = input("Date & Time (e.g. 2026-04-20 14:30): ").strip()
            manager.book_appointment(aid, pid, did, dt)

        elif choice == "6":   # 新增 Cancel
            aid = input("Appointment ID to cancel: ").strip()
            manager.cancel_appointment(aid)

        elif choice == "7":
            pid = input("Patient ID: ").strip()
            records = manager.get_patient_records(pid)
            if records:
                print(f"\nMedical Records for {pid}:")
                for r in records:
                    print(r)
            else:
                print("No medical records found.")

        elif choice == "8":
            pid = input("Patient ID: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            diagnosis = input("Diagnosis: ").strip()
            prescription = input("Prescription: ").strip()
            notes = input("Notes (optional): ").strip()
            manager.add_medical_record(pid, date, diagnosis, prescription, notes)

        elif choice == "9":
            manager.view_all_appointments()

        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
