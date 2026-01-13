class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def new_patient(self, name: str, age: str):
        if age.isdigit():
            self.age = int(age)
        else:
            raise ValueError("Yoshni sonda kiritish kerak")
        if name[0].isupper():
            self.name = name
        else:
            raise ValueError("Ismi bosh harifi katta bolishi kerak")
class Doctor:
    def __init__(self, name, specialty, patient_type, experience):
        self.name = name 
        self.specialty = specialty
        self.patient_type = patient_type
        self.experience = experience
    def get_info_doctors(self):
        return f"Shifokor: {self.name}, Yonalishi: {self.specialty}, Kimlarni koradi: {self.patient_type}, Tajribasi: {self.experience}"
    
    def set_name(self, value: str):
        if value.startswith("Dr."):
            self.name = value
        else:
            raise ValueError("Ismning boshida 'Dr.' bolishi shart")
class Appointment:
    def __init__(self, data, patient, chosen_doctor):
        self.data = data
        self.patient = patient
        self.doctor = chosen_doctor
    def show_appointment(self):
        print(f"Sana: {self.data}")
        print(f"Bemor: {self.patient.name}, {self.patient.age} yosh")
        print(f"Shifokor: {self.doctor.name}, {self.doctor.specialty}")

doctor_ear = Doctor("Dr. Valijon", "Quloq salomatligi", "Hamma uchun", "8 yil")
doctor_brain = Doctor("Dr. Alijon", "Miyya salomatligi", "Hamma uchun", "12 yil")
doctor_heart =  Doctor("Dr. Nozimjon", "Yurak salomatligi", "Hamma uchun", "7 yil")
doctor_children = Doctor("Dr. Avazbek", "Stamatolog", "Bolalar shifokori", "4 yil")
doctor_adults = Doctor("Dr. Rustamjon", "Stamatolog", "Kattalar shifokori", "6 yil")
doctors = [doctor_adults, doctor_brain, doctor_children, doctor_ear, doctor_heart]  

patients = []
def add_patient(name, age):
    patient = Patient(name, age)
    patients.append(patient)
    print(f"Yangi bemor qoshildi: {patient.name}, {patient.age} yosh")
    return patient
patient1 = add_patient("Laylo", 8)
patient2 = add_patient("Lobar", 11)
patient3 = add_patient("Malak", 24)

appointments = []
def add_appointment(date, patient, doctor):
    appointment = Appointment(date, patient, doctor)
    appointments.append(appointment)
    print(f"Yangi bemor ochret qoshildi: {patient.name}, Shifokor ismi: {doctor.name}")
    return appointment

doctor_children.set_name("Dr. Rustamjon")
print("Bolalar doktori yangi tayinlandi:", doctor_children.name)
appointment1 = add_appointment("2025-05-23", patient1, doctor_children)
appointment2 = add_appointment("2025-05-24", patient2, doctor_brain)
appointment3 = add_appointment("2025-07-22", patient3, doctor_ear)
appointment1.show_appointment()
print()
appointment2.show_appointment()
print()
appointment3.show_appointment()
print()

print("Shifo xona doktorlar royhati:")
for doc in doctors:
    print(doc.get_info_doctors())

def find_doctor_name(name, doctors):
    for doc in doctors:
        if doc.name == name:
            return doc
        return None
search_name = "Dr. Rustamjon"
doctor_found = find_doctor_name(search_name, doctors)
if doctor_found:
    print("Topilgan shifokor malumoti")
    print(doctor_found.get_info_doctors())
else:
    print(f"{search_name} ismli shifokor topilmadi")
