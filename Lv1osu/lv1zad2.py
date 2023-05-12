def input_number():
    while True:
        try:
            number = float(input("Enter a number between 0 and 1: "))
            if 0 <= number <= 1:
                return(number)
            print("Please try again, it must be a number between 0 and 1")
        except ValueError:
            print("Input must be an integer between 0 and 1.")


x=input_number()

if x>=0.9 :
    print('A')
elif x>=0.8 :
    print('B')
elif x>=0.7 :
    print('C')
elif x>=0.6 :
    print('D')
elif x<0.6 :
    print('F')