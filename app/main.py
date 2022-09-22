
from birthdayRepository import BirthdayRepository
from email_send import *

def main():
    emp_data =BirthdayRepository.CleanData()
    exlc_emp_list=BirthdayRepository.NoBirthdayWishes()
    name_list =BirthdayRepository.getTodayBirthday(emp_data,exlc_emp_list)
    sendMessage(name_list)
    

if __name__ == "__main__":
    main()
