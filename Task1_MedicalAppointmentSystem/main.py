from manager import ClinicManager

def main():
    manager = ClinicManager()
    print("Medical Appointment System")

    while True:
        print("\n" + "="*40)
        print("1. View All Patients")
        print("2. View All Doctors")
        print("3. Add New Patient")
        print("4. Add New Doctor")
        print("5. Book Appointment")
        print("6. View Patient Records")
        print("7. View All Appointments")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for p in manager.patients.values():
                print(p.display_info())
        elif choice == "2":
            for d in manager.doctors.values():
                print(d.display_info())
        elif choice == "3":
            pid = input("Patient ID: ")
            name = input("Name: ")
            phone = input("Phone: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            manager.add_patient(pid, name, phone, dob)
            print("Patient added successfully!")
        elif choice == "4":
            pid = input("Doctor ID: ")
            name = input("Name: ")
            phone = input("Phone: ")
            spec = input("Specialty: ")
            manager.add_doctor(pid, name, phone, spec)
            print("Doctor added successfully!")
        elif choice == "5":
            aid = input("Appointment ID: ")
            pid = input("Patient ID: ")
            did = input("Doctor ID: ")
            dt = input("Date & Time (YYYY-MM-DD HH:MM): ")
            if manager.book_appointment(aid, pid, did, dt):
                print("Appointment booked successfully!")
            else:
                print("Invalid Patient or Doctor ID")
        elif choice == "6":
            pid = input("Patient ID: ")
            records = manager.get_patient_records(pid)
            if records:
                for r in records:
                    print(r)
            else:
                print("No records found")
        elif choice == "7":
            for app in manager.appointments.values():
                print(app)
        elif choice == "0":
            print("Thank you for using the system!")
            break

if __name__ == "__main__":
    main()
  
