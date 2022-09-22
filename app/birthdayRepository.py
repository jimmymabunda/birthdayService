import requests
from datetime import datetime
from decouple import config


EMP_EXC_ENDPOINT = config('ENDPOINT_EXC_EMP', cast=str)
EMP_ENDPOINT = config('ENDPOINT_EMP', cast=str)

class BirthdayRepository:

    @classmethod
    def CleanData(self):
        emp =requests.get(EMP_ENDPOINT)
        return emp.json()

    @classmethod
    def NoBirthdayWishes(self):
        no_birthday=requests.get(EMP_EXC_ENDPOINT)
        return no_birthday.json()

    @classmethod
    def getTodayBirthday(self,employee_data,exlc_emp_list):
        birthdayListn= []
        unique_list = []
        day=0
        now_month = datetime.now().strftime("%m")
        now_day = datetime.now().strftime("%d")
        date = datetime.now().strftime("%Y-%m-%d")
        for i in range (len(employee_data)):
            for key in employee_data[i]:
                if employee_data[i]['id'] not in exlc_emp_list:
                    if 'dateOfBirth' in employee_data[i]:
                        dob =datetime.strptime(employee_data[i]['dateOfBirth'], '%Y-%m-%dT%H:%M:%S')
                        day =dob.strftime('%d')
                        month = dob.strftime('%m')
                    if 'employmentStartDate' in employee_data[i] and employee_data[i]['employmentStartDate']:
                        start_date =datetime.strptime(employee_data[i]['employmentStartDate'],'%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
                
                    
                    if day == now_day and month == now_month and start_date <= date and employee_data[i]['employmentEndDate'] is None:
                        if employee_data[i]['id']not in unique_list:
                            unique_list.append(employee_data[i]['id'])
                            birthdayListn.append(employee_data[i]['name'])


        return birthdayListn