# მომხმარებელს მიერ შემოტანილი რიცხვის შემოწმება
try:
    # მომხმარებელს შემოატანინეთ რიცხვი
    number = int(input("20"))

    # შეამოწმეთ, არის თუ არა რიცხვი ლუწი თუ კენტი
     if number % 2 == 0:
       print(f"(number)" არის ლუწი რიცხვი)
     else:
         print(f"(number)" არის კენტი რიცხვი)
    expect ValueError:
    print("გთხოვთ, შეიტანოთ ვალიდიური რიცხვი")