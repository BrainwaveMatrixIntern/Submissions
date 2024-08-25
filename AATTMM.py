import random
print("Welcome to ROSO bank!")

Nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "B", "C", "D", "E"]
def genCardNum(Nums):
    newNum = []
    for item in range(21):
        newNum.append(random.sample(Nums, 10))
    print(newNum)

PinNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def genPINNum(PinNums):
    newPin = []
    for item in range(21):
        newPin.append(random.sample(PinNums, 4))
    print(newPin)

Cards = [genCardNum(Nums)]
CardPin = [genPINNum(PinNums)]
#userAccDetail = {Cards[i] : CardPin[i] for i in range(len(Cards))}
#print(str(userAccDetail))


trial = 3
Balance = random.uniform(0, 10000000)
while trial != 0:
    try:
        userCard = input("Please enter your card details: ")
        userPin = int(input("Please enter your pin: "))
        if (userCard in Cards) and (userPin in CardPin) == False:
            trial -= 1
            print(f"Wrong input, {trial} trys left!")
        
        if trial == 0:
            print("Wrong Input")
            print("Your card has been withheld. Please visit your bank for more details!")
            break

        if trial == "":
            print("Wrong Input")
            print("Your card has been withheld. Please visit your bank for more details!")
            break

        else:
            Choice = int(input("1: Deposit, 2: Withdraw, 3: Balance, 4: Exit: "))
            if Choice == 1:
                deposit = int(input("How much would you like to deposit: "))
                newBalance = Balance + deposit
                Balance = newBalance
                print("Transaction Successful!")
                print(f"Present available balance: ${newBalance}")
            

            elif Choice == 2:
                withdrawal = int(input("How much do you want to withdraw: "))
                if withdrawal > Balance:
                    print("Insufficient Balance!")
                newBalance = Balance - withdrawal
                print("Transaction Successful!")
                print(f"Present available balance: ${newBalance}")

            if Choice == 3:
                print(f"Available balance is ${Balance}.")

            elif Choice == 4:
                print("Thank you for using ROSO bank")
                print("Have a nice day!")
                break
    except:
        print("Wrong Input!")
        print("Thank you for using ROSO bank!")
        print("Have a great day!")
        break
print("Thank you for using ROSO bank!")
print("Have a great day!")