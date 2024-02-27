def main():
    print("Resturent Check and Tip")
    check=int(input("Please enter Chack Value : "))
    tip=int(input("Please Enter Tip Value : "))
    def expect_tip(check,tip):
        exp_tip=check*tip/100
        return
    def calculate(check,tip,expect_tip):
        if expect_tip<15:
            print("Can you Leve Little bit mor Tip It'll help ")
        else:
            print("Thank You Fore your Genurus Tip We are appriciate it...")
        return
    print(calculate)
main()