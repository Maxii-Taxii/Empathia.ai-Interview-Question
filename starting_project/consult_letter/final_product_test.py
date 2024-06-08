from consult_letter import create_consult_letter
from openai_chat import chat_content


def test_create_consult_letter():

    # This was the given example.  Please note that when running the code this example will not be used unless selected.
    consult_letter = create_consult_letter(
        user_info={"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"},
        specialty="Obstetrics & Gynecology (ObGyn)",
        note_date="2022/01/01",
        note_content={
            "Patient Name": "Jane",
            "Patient Age": None,
            "Gender": "female",
            "Chief Complaint": "OB consultation for pregnancy management with planned repeat cesarean section.",
            "History of Present Illness": None,
            "Past Medical History": "The patient had COVID-19 in 2021, after which she experienced heart pain, but subsequent evaluations by her family doctor and hospital visits confirmed that everything was okay.",
            "Past Surgical History": "The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.",
            "Family History": None,
            "Social History": "Jane is employed part-time as a banker, working two to three days per week. She and her spouse reside in a non-specified location without nearby family support. However, they have a local friend network. Postpartum, Jane's mother will assist, and they intend to employ a babysitter for two months.",
            "Obstetric History": "The patient is currently pregnant with her third child. She has had one previous live birth via cesarean section and one abortion due to fetal health issues. Her first child was born slightly premature at approximately 37 weeks, weighing 2.5 kilograms.",
            "The Review of Systems": "The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.",
            "Current Medications": None,
            "Allergies": "The patient is allergic to minocycline.",
            "Vital Signs": None,
            "Physical Examination": None,
            "Investigations": None,
            "Problem": "1. Previous cesarean section (654.21)",
            "Differential Diagnosis": None,
            "Plan": "• Scheduled repeat cesarean section at 39 weeks gestation\n• Instructed patient to present to City Medical Center for emergency cesarean section if labor begins prior to scheduled date\n• Advised patient to walk daily for 20 to 30 minutes to improve blood pressure and baby's health\n• Arranged follow-up appointment in three weeks, with subsequent visits every two weeks, then weekly as due date nears",
            "Surgery Discussion": "• Purpose of the Surgery: The purpose of the repeat cesarean section is to safely deliver the baby, given the patient's previous cesarean delivery and her choice for a planned cesarean this time.\n• Risks and Complications: The risks of cesarean section include bleeding, infection, or injury to the bladder or bowel. These risks are small but not zero.\n• Anesthesia: Spinal anesthesia will be used during the procedure, which will prevent pain but allow the patient to be awake.\n• Alternatives: N/A",
        }
    )

    # My own example I created.
    consult_letter_created = create_consult_letter(
        user_info={"name": "Dr. Emily Smith", "email": "dremilysmith@hospital.com"},
        specialty="Cardiology",
        note_date="2023/05/15",
        note_content={
            "Patient Name": "Michael",
            "Patient Age": 45,
            "Gender": "male",
            "Chief Complaint": "Consultation for chest pain and shortness of breath.",
            "History of Present Illness": "Michael has been experiencing chest pain and shortness of breath for the past two weeks, especially after physical exertion.",
            "Past Medical History": "The patient has a history of hypertension and was diagnosed with type 2 diabetes in 2018. He had a mild heart attack in 2020.",
            "Past Surgical History": "The patient underwent angioplasty in 2020 after the heart attack.",
            "Family History": "The patient's father had a history of heart disease and passed away from a heart attack at age 60.",
            "Social History": "Michael is a software engineer who works from home. He lives with his wife and two children. He smokes a pack of cigarettes per day and occasionally drinks alcohol.",
            "The Review of Systems": "The patient reports no fever, chills, or night sweats. He has occasional headaches but no dizziness or fainting spells.",
            "Current Medications": "Metformin, Lisinopril, Aspirin.",
            "Allergies": "The patient is allergic to penicillin.",
            "Vital Signs": "Blood pressure: 150/90 mmHg, Heart rate: 85 bpm.",
            "Physical Examination": "Mild wheezing heard in the lungs, no edema in the lower extremities.",
            "Investigations": "ECG shows signs of previous myocardial infarction. Blood tests reveal elevated cholesterol levels.",
            "Problem": "1. Chest pain (786.50)\n2. Shortness of breath (786.05)\n3. Hypertension (401.9)\n4. Type 2 diabetes (250.00)",
            "Differential Diagnosis": "1. Angina pectoris\n2. Coronary artery disease",
            "Plan": "• Schedule a stress test to evaluate the heart's function during physical activity\n• Adjust hypertension medication to better control blood pressure\n• Recommend smoking cessation program\n• Follow-up appointment in one month to review test results and adjust treatment plan as necessary",
            "Surgery Discussion": "N/A",
        }
    )



    # Writes the output to a txt file and by default it will create the txt file if it doesn't exist already
    with open('output.txt', 'w') as file:
        file.write(consult_letter_created)

    # Prints response so we can see it in the terminal
    print(consult_letter_created)
    return consult_letter_created
