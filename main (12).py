# 2.Write a program that determines whether a year entered by the user is a leap year or not using if elif-else statements.



year = int(input("Enter Year To Be Checked : "))

 

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:

            print("The Year Is A Leap Year!")

        else:

            print("The Year Is Not A Leap Year!")

    else:

        print("The Year Is A Leap Year!")

else:

    print("The Year Is Not A Leap Year!")