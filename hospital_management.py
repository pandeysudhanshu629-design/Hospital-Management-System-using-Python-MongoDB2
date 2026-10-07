from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["hospital_db"]

# Collections
patients = db["patients"]
doctors = db["doctors"]
appointments = db["appointments"]


# ---------- PATIENT FUNCTIONS ----------

# Add Patient
def add_patient():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    city = input("Enter City: ")

    patient = {
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "city": city
    }

    patients.insert_one(patient)

    print("Patient Added Successfully!\n")


# View Patients
def view_patients():
    print("\n===== ALL PATIENTS =====")

    for p in patients.find():
        print("ID:", p["_id"])
        print("Name:", p["name"])
        print("Age:", p["age"])
        print("Gender:", p["gender"])
        print("Disease:", p["disease"])
        print("City:", p["city"])
        print("------------------------")


# Search Patient
def search_patient():
    name = input("Enter Patient Name: ")

    patient = patients.find_one({"name": name})

    if patient:
        print("\nPatient Found")
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Disease:", patient["disease"])
        print("City:", patient["city"])
    else:
        print("Patient Not Found")


# Update Patient
def update_patient():
    name = input("Enter Patient Name: ")
    new_disease = input("Enter New Disease: ")

    result = patients.update_one(
        {"name": name},
        {"$set": {"disease": new_disease}}
    )

    if result.modified_count > 0:
        print("Patient Updated Successfully!")
    else:
        print("Patient Not Found")


# Delete Patient
def delete_patient():
    name = input("Enter Patient Name: ")

    result = patients.delete_one({"name": name})

    if result.deleted_count > 0:
        print("Patient Deleted Successfully!")
    else:
        print("Patient Not Found")


# ---------- DOCTOR FUNCTIONS ----------

# Add Doctor
def add_doctor():
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    experience = int(input("Enter Experience (Years): "))

    doctor = {
        "name": name,
        "specialization": specialization,
        "experience": experience
    }

    doctors.insert_one(doctor)

    print("Doctor Added Successfully!\n")


# View Doctors
def view_doctors():
    print("\n===== ALL DOCTORS =====")

    for d in doctors.find():
        print("Name:", d["name"])
        print("Specialization:", d["specialization"])
        print("Experience:", d["experience"], "Years")
        print("------------------------")


# ---------- APPOINTMENT FUNCTION ----------

def book_appointment():
    patient = input("Enter Patient Name: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date: ")

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date
    }

    appointments.insert_one(appointment)

    print("Appointment Booked Successfully!\n")


# View Appointments
def view_appointments():
    print("\n===== APPOINTMENTS =====")

    for a in appointments.find():
        print("Patient:", a["patient"])
        print("Doctor:", a["doctor"])
        print("Date:", a["date"])
        print("------------------------")


# ---------- MAIN MENU ----------

while True:

    print("\n================================")
    print("   HOSPITAL MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. View Doctors")
    print("8. Book Appointment")
    print("9. View Appointments")
    print("10. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        update_patient()

    elif choice == "5":
        delete_patient()

    elif choice == "6":
        add_doctor()

    elif choice == "7":
        view_doctors()

    elif choice == "8":
        book_appointment()

    elif choice == "9":
        view_appointments()

    elif choice == "10":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")