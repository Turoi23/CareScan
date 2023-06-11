import tkinter as tk
from tkinter import messagebox


def check_heart_rate(heart_rate):
    if heart_rate < 30 or heart_rate > 200:
        return False
    return True

def check_blood_pressure(blood_pressure):
    if blood_pressure < 30 or blood_pressure > 200:
        return False
    return True

def check_body_temperature(temperature):
    if temperature < 28 or temperature > 42:
        return False
    return True

def check_yellow_fever(scanner_result):
    if scanner_result:
        return "Possible yellow fever infection"
    return ""

def check_healthy(symptoms):
    if (
        float(blood_pressure_entry.get()) >= 85
          and float(body_temperature_entry.get()) >= 36.5
          and float(heart_rate_entry.get()) >= 80
          and float(blood_pressure_entry.get()) <= 110
          and float(body_temperature_entry.get()) <=37.5
          and float(heart_rate_entry.get()) <= 100
       ): 
        return "Your condition seems to be stable. However if you still have any complaints, address the issue with your doctor"
    return ""

def check_critical(symptoms):
    if (
        float(blood_pressure_entry.get()) >= 180
          or float(body_temperature_entry.get()) > 40
          or float(heart_rate_entry.get()) >= 140
          or float(blood_pressure_entry.get()) <= 65
          or float(body_temperature_entry.get()) <= 35
          or float(heart_rate_entry.get()) <= 60
       ): 
        return "Your condition seems to be critical. Please stand by, an ambulance will arrive shortly."
    return ""

def check_pneumonia(symptoms):
    if (
        symptoms.get('cough') 
        or symptoms.get('fever') 
        or symptoms.get('shortness_of_breath') 
        or (float(blood_pressure_entry.get()) <= 80
            and float(body_temperature_entry.get()) > 38
            and float(heart_rate_entry.get()) >= 110)
    ): 
        return "Possibly pneumonia, more infos below" #Infos will be added through other means
    return ""

def check_diarrhoea(symptoms):
    if (
        symptoms.get('diarrhoea')
        or symptoms.get('abdominal_pain') 
        or symptoms.get('dehydration') 
        or (float(blood_pressure_entry.get()) <= 80
            and float(body_temperature_entry.get()) > 38
            and float(heart_rate_entry.get()) >= 110)
    ):
        return "Possibly diarrhoea, more infos below" #Infos will be added through other means
    return ""

def check_malaria(symptoms):
    if (
        symptoms.get('fever')
        or symptoms.get('chills') 
        or symptoms.get('muscle_pain') 
        or symptoms.get('headache') 
        or (float(blood_pressure_entry.get()) >= 140
            and float(heart_rate_entry.get()) <= 80)
        or (float(blood_pressure_entry.get()) >= 140
            and float(body_temperature_entry.get()) >= 39)
        or (float(body_temperature_entry.get()) >= 39
            and float(heart_rate_entry.get()) <= 80)
    ):
        return "Possibly malaria, more infos below" #Infos will be added through other means
    return ""

def analyze_symptoms():
    heart_rate = int(heart_rate_entry.get())
    if not check_heart_rate(heart_rate):
        messagebox.showerror("Error", "Invalid heart rate value!")
        return

    blood_pressure = int(blood_pressure_entry.get())
    if not check_blood_pressure(blood_pressure):
        messagebox.showerror("Error", "Invalid blood pressure value!")
        return

    body_temperature = float(body_temperature_entry.get())
    if not check_body_temperature(body_temperature):
        messagebox.showerror("Error", "Invalid body temperature value!")
        return

    scanner_result = yellow_fever_var.get()

    symptoms = {
        'cough': cough_var.get(),
        'fever': fever_var.get(),
        'shortness_of_breath': shortness_of_breath_var.get(),
        'diarrhoea': diarrhoea_var.get(),
        'abdominal_pain': abdominal_pain_var.get(),
        'dehydration': dehydration_var.get(),
        'chills': chills_var.get(),
        'muscle_pain': muscle_pain_var.get(),
        'headache': headache_var.get()
    }

    possible_diseases = []
    if scanner_result:
        possible_diseases.append(check_yellow_fever(scanner_result))
    possible_diseases.append(check_pneumonia(symptoms))
    possible_diseases.append(check_diarrhoea(symptoms))
    possible_diseases.append(check_malaria(symptoms))
    possible_diseases.append(check_critical(symptoms))
    possible_diseases.append(check_healthy(symptoms))

    result_text.delete('1.0', tk.END)
    if possible_diseases:
        for disease in possible_diseases:
            if disease:
                result_text.insert(tk.END, f"{disease}\n")
    else:
        result_text.insert(tk.END, "No specific disease detected.")

# GUI setup
root = tk.Tk()
root.title("Disease Terminal")
root.geometry("600x600")

heart_rate_label = tk.Label(root, text="Heart Rate (bpm):")
heart_rate_label.pack()
heart_rate_entry = tk.Entry(root)
heart_rate_entry.pack()

blood_pressure_label = tk.Label(root, text="Blood Pressure (mmHg):")
blood_pressure_label.pack()
blood_pressure_entry = tk.Entry(root)
blood_pressure_entry.pack()

body_temperature_label = tk.Label(root, text="Body Temperature (°C):")
body_temperature_label.pack()
body_temperature_entry = tk.Entry(root)
body_temperature_entry.pack()

yellow_fever_var = tk.BooleanVar()
yellow_fever_checkbutton = tk.Checkbutton(root, text="Yellow Fever detected", variable=yellow_fever_var)
yellow_fever_checkbutton.pack()

cough_var = tk.BooleanVar()
cough_checkbutton = tk.Checkbutton(root, text="Cough", variable=cough_var)
cough_checkbutton.pack()

fever_var = tk.BooleanVar()
fever_checkbutton = tk.Checkbutton(root, text="Fever", variable=fever_var)
fever_checkbutton.pack()

shortness_of_breath_var = tk.BooleanVar()
shortness_of_breath_checkbutton = tk.Checkbutton(root, text="Shortness of Breath", variable=shortness_of_breath_var)
shortness_of_breath_checkbutton.pack()

diarrhoea_var = tk.BooleanVar()
diarrhoea_checkbutton = tk.Checkbutton(root, text="diarrhoea", variable=diarrhoea_var)
diarrhoea_checkbutton.pack()

abdominal_pain_var = tk.BooleanVar()
abdominal_pain_checkbutton = tk.Checkbutton(root, text="Abdominal Pain", variable=abdominal_pain_var)
abdominal_pain_checkbutton.pack()

dehydration_var = tk.BooleanVar()
dehydration_checkbutton = tk.Checkbutton(root, text="Dehydration", variable=dehydration_var)
dehydration_checkbutton.pack()

chills_var = tk.BooleanVar()
chills_checkbutton = tk.Checkbutton(root, text="Chills", variable=chills_var)
chills_checkbutton.pack()

muscle_pain_var = tk.BooleanVar()
muscle_pain_checkbutton = tk.Checkbutton(root, text="Muscle Pain", variable=muscle_pain_var)
muscle_pain_checkbutton.pack()

headache_var = tk.BooleanVar()
headache_checkbutton = tk.Checkbutton(root, text="Headache", variable=headache_var)
headache_checkbutton.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_symptoms)
analyze_button.pack()

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

root.mainloop()
