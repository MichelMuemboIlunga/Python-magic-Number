MagicNumber = []
confirmation = "Confirm"
Cancel = "Cancel"

for n in range(5):
    # prompting user to enter the magic number
    try:
        user = int(input("Please Enter your Magic number: "))

        # add user number to the list
        MagicNumber.append(user)

        # user confirmation to continue or cancel the process
        if True:
            print(f"The value you enter was : {user}")
            UserConfirm = input(" Enter Confirm to Continue or cancel to Cancel: ")
            if UserConfirm == confirmation:
                continue
            elif UserConfirm == Cancel:
                break

            # in case the user enter a wrong confirmation keyword instead of confirm or Cancel
            else:
                print("------------------------------------------")
                print("Not a correct input, Please try  again!!!")
                print("------------------------------------------")
                if True:
                    print("The Number you enter was : ", user)
                    UserConfirm = input(" Enter Confirm to Continue or cancel to Cancel: ")
                    if UserConfirm == confirmation:
                        continue
                    elif UserConfirm == Cancel:
                        break
    # if user enter a wrong type of number (ex:string or float) instead of throwing an error
    # user receive a message
    except ValueError:
        print("wrong type of number, Prefer integer")

print("Your Magic Number are: ", MagicNumber)

if __name__ == '__main__':
    print('All done by Michel Muembo Ilunga 💻')

