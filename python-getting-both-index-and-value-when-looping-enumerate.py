## lists the applicant names on the list with
## their assigned number
num_applicants = int(input())

applicant_list = []
for i in range(num_applicants):
    applicant_list.append(input())

for (number, applicant) in enumerate(applicant_list):
    print(f'Name: {applicant}, Number: {number + 1}')

## lists the patient names and what floor
## they are going to based on assigned number
num_data = int(input())

list_patients = []
for i in range(num_data):
    list_patients.append(input())

for (number, name) in enumerate(list_patients):
    if number % 2 != 0:
        print(f'{name} goes to level 1')
    else:
        print(f'{name} goes to level 5')
