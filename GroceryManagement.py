from tkinter import *
from tkinter import messagebox
import mysql.connector

# Connecting to the database and creating tables
db = mysql.connector.connect(host="localhost", user="root", passwd="bhanderchod08")
my_cursor = db.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS GroceryShop")
db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
my_cursor = db.cursor()

# Creating tables if not exists
query_products = "CREATE TABLE IF NOT EXISTS products (date VARCHAR(10), custName VARCHAR(20), address VARCHAR(100))"
my_cursor.execute(query_products)

query_sale = "CREATE TABLE IF NOT EXISTS sale (custName VARCHAR(20), date VARCHAR(10), prodName VARCHAR(30), qty INTEGER, price INTEGER)"
my_cursor.execute(query_sale)

# Function to add customer details to the products table
def prodtoTable():
    dt = date.get()
    cust_name = custName.get()
    address = prodAddress.get()

    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()

    query = "INSERT INTO products(date, custName, address) VALUES(%s, %s, %s)"
    details = (dt, cust_name, address)

    try:
        cursor.execute(query, details)
        db.commit()
        messagebox.showinfo('Success', "Customer added successfully")
    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Error", "Trouble adding data into Database")

    wn.destroy()


def addProd():
    global prodAddress, date, custName, Canvas1, wn

    wn = Tk()
    wn.title("Grocery Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='LightBlue1', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add a Customer Detail", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lable1 = Label(labelFrame, text="Date : ", fg='black')
    lable1.place(relx=0.05, rely=0.3, relheight=0.08)

    date = Entry(labelFrame)
    date.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    lable2 = Label(labelFrame, text="Customer Name : ", fg='black')
    lable2.place(relx=0.05, rely=0.45, relheight=0.08)

    custName = Entry(labelFrame)
    custName.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.08)

    lable3 = Label(labelFrame, text="Customer Address : ", fg='black')
    lable3.place(relx=0.05, rely=0.6, relheight=0.08)

    prodAddress = Entry(labelFrame)
    prodAddress.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.08)

    Btn = Button(wn, text="ADD", bg='#d1ccc0', fg='black', command=prodtoTable)
    Btn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

    wn.mainloop()



# Function to add the product to the database
def prodtoTable():
    # Getting the user inputs of product details from the user
    dt = date.get()
    cust_name = custName.get()
    address = prodAddress.get()

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()

    # Query to add the product details to the table
    query = "INSERT INTO products(date, custName, address) VALUES(%s, %s, %s)"
    details = (dt, cust_name, address)

    # Executing the query and showing the pop-up message
    try:
        cursor.execute(query, details)
        db.commit()
        messagebox.showinfo('Success', "Customer added successfully")
    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Error", "Trouble adding data into Database")

    wn.destroy()


# Function to remove the product from the database
def removeProd():
    # Getting the customer name from the user to be removed
    cust_name = custName.get()
    cust_name = cust_name.lower()

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()

    # Query to delete the respective customer from the database
    query = "DELETE from products where LOWER(custName) = '" + cust_name + "'"
    # Executing the query and showing the message box
    try:
        cursor.execute(query)
        db.commit()
        messagebox.showinfo('Success', "Customer Record Deleted Successfully")

    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Please check Customer Name")

    wn.destroy()


# Function to get customer details from the user to be deleted
def delProd():
    global custName, Canvas1, wn
    # Creating a window
    wn = Tk()
    wn.title("Grocery Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg="misty rose", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Customer record", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Customer Name to Delete
    lable = Label(labelFrame, text="Customer Name : ", fg='black')
    lable.place(relx=0.05, rely=0.5)

    custName = Entry(labelFrame)
    custName.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Delete Button
    Btn = Button(wn, text="DELETE", bg='#d1ccc0', fg='black', command=removeProd)
    Btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Function to show all the customers in the database
def viewProds():
    global wn
    # Creating the window to show the customer details
    wn = Tk()
    wn.title("Grocery Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='old lace')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='old lace', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Customer Detail", fg='black', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()
    # Query to select all customers from the table
    query = 'SELECT * FROM products'

    Label(labelFrame, text="%-50s%-50s%-50s" % ('Date', 'Customer', 'Address'), font=('calibri', 11, 'bold'),
          fg='black').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",
          fg='black').place(relx=0.05, rely=0.2)
    # Executing the query and showing the customers' details
    try:
        cursor.execute(query)
        res = cursor.fetchall()

        for i in res:
            Label(labelFrame, text="%-50s%-50s%-50s" % (i[0], i[1], i[2]), fg='black').place(relx=0.07, rely=y)
            y += 0.1
    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Failed to fetch files from the database")

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Function to generate the bill
def bill():
    # Creating a window
    wn = Tk()
    wn.title("Grocery Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    headingFrame1 = Frame(wn, bg="lavender blush2", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Generate Bill", fg='black', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn, bg='lavender blush2')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    y = 0.25

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()

    # Query to select all products from the sale table
    query = 'SELECT * FROM sale'
    try:
        cursor.execute(query)
        res = cursor.fetchall()

        # Displaying the product details in the window
        for i in res:
            Label(labelFrame, text="%-30s%-30s%-20s%-20s" % (i[0], i[1], i[2], i[3]), fg='black').place(relx=0.07, rely=y)
            y += 0.1

    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Failed to fetch files from the database")

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Function to generate the bill
def sell():
    global wn, Canvas1
    # Creating a window
    wn = Tk()
    wn.title("Grocery Management System")
    wn.configure(bg='orange2')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='orange2')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='orange2', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Sell", fg='black', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.45)

    # Product Name
    lable = Label(labelFrame, text="Product Name : ", fg='black')
    lable.place(relx=0.05, rely=0.1)

    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.1, relwidth=0.62)

    # Quantity
    lable = Label(labelFrame, text="Quantity : ", fg='black')
    lable.place(relx=0.05, rely=0.3)

    qty = Entry(labelFrame)
    qty.place(relx=0.3, rely=0.3, relwidth=0.62)

    # Price
    lable = Label(labelFrame, text="Price : ", fg='black')
    lable.place(relx=0.05, rely=0.5)

    price = Entry(labelFrame)
    price.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Date
    lable = Label(labelFrame, text="Date : ", fg='black')
    lable.place(relx=0.05, rely=0.7)

    date = Entry(labelFrame)
    date.place(relx=0.3, rely=0.7, relwidth=0.62)

    # Sell Button
    Btn = Button(wn, text="SELL", bg='#d1ccc0', fg='black', command=addSale)
    Btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Quit Button
    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Function to add the sale details to the sale table
def addSale():
    # Getting the user inputs for sale details
    global custName, prodName, qty, price, date 
    cust_name = custName.get()
    prod_name = prodName.get()
    qty_val = qty.get()
    price_val = price.get()
    date_val = date.get()

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()

    # Query to add sale details to the sale table
    query = "INSERT INTO sale(custName, date, prodName, qty, price) VALUES(%s, %s, %s, %s, %s)"
    details = (cust_name, date_val, prod_name, qty_val, price_val)

    # Executing the query and showing the pop-up message
    try:
        cursor.execute(query, details)
        db.commit()
        messagebox.showinfo('Success', "Product sold successfully")
    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Error", "Trouble adding data into Database")

    wn.destroy()


# Function to view sales details
def viewSales():
    global wn
    # Creating the window to show the sales details
    wn = Tk()
    wn.title("Grocery Management System")
    wn.configure(bg='misty rose')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='misty rose')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='misty rose', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Sales Detail", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="bhanderchod08", host="localhost", database='GroceryShop')
    cursor = db.cursor()

    # Query to select all sales from the sale table
    query = 'SELECT * FROM sale'

    Label(labelFrame, text="%-20s%-20s%-20s%-20s%-20s" % ('Customer', 'Date', 'Product', 'Quantity', 'Price'),
          font=('calibri', 11, 'bold'), fg='black').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",
          fg='black').place(relx=0.05, rely=0.2)

    # Executing the query and showing the sales details
    try:
        cursor.execute(query)
        res = cursor.fetchall()

        for i in res:
            Label(labelFrame, text="%-20s%-20s%-20s%-20s%-20s" % (i[0], i[1], i[2], i[3], i[4]), fg='black').place(relx=0.07, rely=y)
            y += 0.1

    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Failed to fetch data from the database")

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Main function
def main():
    # Creating the main window
    root = Tk()
    root.title("Grocery Management System")
    root.configure(bg='mint cream')
    root.minsize(width=500, height=500)
    root.geometry("700x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg='misty rose')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg='misty rose', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Welcome to Grocery Management System", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Button to add a new customer
    btn = Button(root, text="Add Customer", bg='#d1ccc0', fg='black', command=addProd)
    btn.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    # Button to delete a customer
    btn = Button(root, text="Delete Customer", bg='#d1ccc0', fg='black', command=delProd)
    btn.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)

    # Button to view all customers
    btn = Button(root, text="View Customers", bg='#d1ccc0', fg='black', command=viewProds)
    btn.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    # Button to sell a product
    btn = Button(root, text="Sell Product", bg='#d1ccc0', fg='black', command=sell)
    btn.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)

    # Button to view sales
    btn = Button(root, text="View Sales", bg='#d1ccc0', fg='black', command=viewSales)
    btn.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)

    root.mainloop()


if __name__ == "__main__":
    main()

