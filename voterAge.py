import datetime
"""Write a small python program that:
take date of birth as DD/MM/YYYY argument and
print based on birthdate if Voter is eligible to vote or if Voter is not eligible to vote.
Send the code in plain text replying to this email.
Add a small video (3-5 min) explaining you solution."""

def main(): 
    input_date = input("Put in date with the format DD/MM/YYYY: \n")
    incorrectDate = True
    dob = None
    #loop until correct date format is typed
    while (incorrectDate):

        try:
            input_date = input_date.split("/")
            day = int(input_date[0])
            month = int(input_date[1])
            year = int(input_date[2])
            dob = datetime.datetime(year, month, day)
            incorrectDate = False
        except:
            input_date = input("Invalid date. Please insert date with the format DD/MM/YYYY \n")

    #calculate age
    currentDate = datetime.date.today()
    age = currentDate.year - dob.year - ((currentDate.month, currentDate.day) < (dob.month, dob.day))

    #write out whether person is eligible to vote based on age
    if age >= 18:
        print("This person is eligible to vote based on their date of birth.")
    else:
        print("This person is not eligible to vote based on their date of birth.")



if __name__ == '__main__':
    main()
    '''
    ask if registered
        yes
            label: enter date 
            check age eligible
                yes
                    ask name 
                    check database w/ date = enter date
                no 
                    enter date or leave


            

        no 
            register?
                yes
                    label: enter date 
                no
                    leave
    enter date

    '''
