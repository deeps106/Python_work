"""
Write code for user to input patient details, operation details, postop management with signature and GMCnumber at the end.
Transfer inputs to a text file and aim to construct the page with tabs
Date of the surgery is needed so datetime module needs importing
"""
from datetime import datetime
now = datetime.now()

from pynput.keyboard import Key, Listener

file_name = input("Enter the name of the file and add .txt at the end\n")

today_date = now.strftime("%d-%b-%Y")
current_time = now.strftime("%H:%M")
# print(today_date)
# print(current_time)

theatre = input("In which theatre did you do the operation?\n")
theatre = theatre.title()

name = input("What is the patient's name?\n")
name = name.title()

dob = input("What is the patient's date of birth?e.g 11/02/78\n")

gender = input("What is the patient's gender\n")
gender = gender.title()

hospital_number = input("What is the patient's hospital number?\n")

nhs_no = input("What is the patient's NHS number?\n")

first_surgeon = input("What is the name of the first surgeon\n")
first_surgeon = first_surgeon.title()

second_surgeon = input("What is the name of the second surgeon?\n")
second_surgeon = second_surgeon.title()

assistant = input("What is the name of the assistant?\n")
assistant = assistant.title()

anaesthetist = input("What is the name of the anaesthetist\n")
anaesthetist = anaesthetist.title()


with open(file_name, "w") as textfile:
    textfile.write(f"DATE: {today_date}\t\tTIME: {current_time}\n\n")
    textfile.write(f"THEATRE: {theatre}\n\n")
    textfile.write(f"PATIENT DETAILS:\nNAME: {name}\tDATE OF BIRTH: {dob}\tGENDER: {gender}\n")
    textfile.write(f"MRN: {hospital_number}\tNHS NO: {nhs_no}\n\n")
    textfile.write(f"FIRST SURGEON: {first_surgeon}\nSECOND SURGEON: {second_surgeon}\n")
    textfile.write(f"ASSISTANT: {assistant}\n")
    textfile.write(f"ANAESTHETIST: {anaesthetist}\n\n")   
# # anaesthetic type   
    while True:
        anaesthetic = input('''What type of anaesthetic was used? Choose one from the following options:
                    1. GA
                    2. GA with Spinal
                    3. LA
                    4. Spinal/Epidural
                    5. Sedation and LA\n''')
        anaesthetic = int(anaesthetic)
        if anaesthetic == 1:
            textfile.write(f"ANAESTHETIC:\nGA\n\n")
            break
        elif anaesthetic == 2:
            textfile.write(f"ANAESTHETIC:\nGA with Spinal\n\n")
            break
        elif anaesthetic == 3:
            textfile.write(f"ANAESTHETIC:\nLA\n")
            break
        elif anaesthetic == 4:
            textfile.write(f"ANAESTHETIC:\nSpinal/Epdidural\n\n")
            break
        elif anaesthetic == 5:
            textfile.write(f"ANAESTHETIC:\nSedation and LA\n\n")
            break
        else:
            print("Shucks! You must've entered text or the wrong number!!. Please try again!")
# title of operation
    operation_title = input("What is the operation?\n")
    operation_title = operation_title.title()
    textfile.write(f"OPERATION:\n{operation_title}\n\n")
# #findings
    findings = input("What were the operative findings?")
    findings = findings.capitalize()
    textfile.write(f"FINDINGS:\n{findings}\n\n")
# operation steps
    operation_steps = input("What were the steps of the operation?")
    operation_steps = operation_steps.capitalize()
    textfile.write(f"PROCEDURE:\n{operation_steps}\n\n")
# writing the post op plan
    print("Please write the  post operative plan. Press 'enter' to continue")
    textfile.write(f"POSTOPERATIVE PLAN:\n")
    postop_plan_type = input("How do you want to write your plan? Type 'f' for free-text or 'b' for bullet points.")
    postop_plan_type = postop_plan_type.lower()
    if postop_plan_type !="b":
        postop_plan_freetxt = input("What is your postoperative plan?\n")
        postop_plan_freetxt = postop_plan_freetxt.capitalize()
        textfile.write(f"{postop_plan_freetxt}")
        print("Thank you for using the app. Goodbye!")            
    else:
        for item in range(10):
            postop_plan_bulletpoint = input(f"{item+1}: ")
            postop_plan_bulletpoint.capitalize()
            textfile.write(f"{item+1}: {postop_plan_bulletpoint} \n")
            if item >= 2:
                plan_continue = input("Do you want to continue? Press 'Y' to continue or 'N' to exit.\n")
                plan_continue = plan_continue.lower()
                if plan_continue != 'n':
                    continue
            else:
                print("Thank you for using the app. Goodbye!")
            break

        

    

    
          
            
        
        
         
        
            
              
          
         
               

            
            
            
        
        

