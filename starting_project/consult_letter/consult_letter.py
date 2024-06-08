"""
Your task is to implement `create_consult_letter` function to generate a consult letter based on the SOAP note.

The input parameters are:
- user_info: a dictionary contains the bio of the doctor, such as
    {
        "name": "Dr. John Doe", # the name of the doctor
        "email": "drjohndoe@clinic.com", # the email of the doctor
    }
- specialty: a string represents the specialty of the doctor, such as "Obstetrics and Gynecology"
- note_content: a dictionary contains the content of the SOAP note, where the key is the section name and the value is the content of the section, such as
    {
        "Chief Complaint": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        "History of Present Illness": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        ...
    }
- note_date: a string represents the date of the SOAP note, such as "2022-01-01"
"""

import json
from typing import Optional

from openai_chat import chat_content


def create_consult_letter(
    user_info: dict, specialty: str, note_content: dict[str, Optional[str]], note_date: str
) -> str:
    
    # The task given and the instructions for accuracy. 
    
    prompt = f"""
    Your task is to create a consult letter based on the following SOAP note and doctor information:
    Do not alter the note content since the data is crucial for the email and accuracy is paramount and do not leave out any data. 

    Doctor Information:
    Name: {user_info["name"]}
    Email: {user_info["email"]}
    Specialty: {specialty}

    Note Date: {note_date}

    SOAP Note:

    """
    # Ensures that each bullet in the note content is added into the prompt

    for section, content in note_content.items():
        prompt += f"\n{section}: {content}\n"

    # The provided instruction outlines the format for the consultation letter, ensuring that the generated email
    # maintains a consistent structure across each iteration. It emphasizes the incorporation of data from the SOAP
    # notes and includes conventional email formatting guidelines.

    prompt += """
    Subject: Consultation Report for [Patient Name]
    Dear Dr. [Referring Doctor's Name],

    Thank you for referring [Patient Name] for an [Doctor Specialty]. He was examined on [Note Date in this format: 2022/01/01]

    [Patient Name, age, gender] presented with a chief complaint of [Chief of Complaint]. [All PATIENT PAST HISTORY, ex: Past Medical History, Medications, Allergies, Family and Social History]

    [If there is a Physical Examination state Upon examination [list them] else state There were no examination, [list of all the specific items] recorded in the notes]

    The assessment suggests a likely diagnosis of [Diagnosis], considering his symptoms and medical history. The treatment plan [Treatment Plan and recommendations]

    If you have any further questions or require additional information, please do not hesitate to contact me [Doctor Email]

    Sincerely,
    [Doctor Name]
    [Doctor Specialty]
    [Doctor Email]
    
    """


    # Calling the chat_content function in the openat_chat.py to call the GPT API to retrieve the message
    response = chat_content(
        messages=[{"role": "system", "content": prompt}],

        # Temperature range between 0 - 2, 0.7 is the normal default to produce coherent but not overly repetitive responses
        temperature=0.7,

        # Max_tokens set to a higher number to ensure that there is enough space to generate the message
        max_tokens=1500
    )
    
    return response