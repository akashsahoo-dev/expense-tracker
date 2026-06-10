import csv

expenses_record = []

def read_csv():
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["Amount"] = int(row["Amount"])
                expenses_record.append(row)
            print("Previous data updated")
    except FileNotFoundError :
        print("No Previous saved file found")




def add_expenses():
    expenses = {}
    date = input("Enter Dater(dd-mm-yy): ")
    category = input("where you spend: ")        
    amount = int(input("Enter the amount: "))
    note = input("Enter Note: ")
    expenses["Date"] = date 
    expenses["Category"] = category
    expenses["Amount"] = amount
    expenses["Note"] = note
    expenses_record.append(expenses)

def view_expenses():
    if not expenses_record :
        print("No data found")
        return
    else :        
        for index,  expenses in enumerate(expenses_record, start=1) :
            print(index, expenses)

def monthly_total():
    month = input("Enter the month you want the total (1-12): ")
    total = 0
    for expenses in expenses_record :
        expense_month = expenses["Date"].split("-")[1]
        if expense_month == month :
            total += expenses["Amount"]
            print(expenses)
    print(f"Monthly Total: {total}")
    return total

def save_csv():
    with open("expenses.csv", "w", newline="") as f:
        fieldnames = ["Date", "Category", "Amount", "Note"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for expenses in expenses_record :
            writer.writerow(expenses)
        print("Data Saved Succesfully.")

def delete_expenses():
    view_expenses()
    if not expenses_record :
        return
    del_row = int(input("Enter the Sl. no you want to delete: "))
    if 1 <= del_row <= len(expenses_record) :
        deleted = expenses_record.pop(del_row-1)
        print("Row Deleted succesfully", deleted)
    else:
        print("Enter a valid row")


read_csv()

while True :
    print ('''1. Add expenses
2. View all expenses
3. Calcualte monthly total
4. Save to CSV
5. Delete expenses
6. Exit''' )



    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
       print("Please enter a valid number")
       continue 
    
    if choice == 1 :
        add_expenses()
    elif choice == 2 :
        view_expenses()
    elif choice == 3 :
        monthly_total()
    elif choice == 4 :
        save_csv()    
    elif choice == 5 :
        delete_expenses()    
    elif choice == 6 :
        save_csv()
        break
    else:
        print("Enter a valid input from the option")

