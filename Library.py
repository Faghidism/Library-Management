import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import datetime


# **
# Connection to the Database
# **

def config():
    global cursor, conn
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=LAPTOP-O16EO7SE\\SQLEXPRESS;"
                          "Database=LibraryManagement;"
                          "Trusted_Connection=yes;")
    cursor = conn.cursor()


###############################################
#     ******                                  #
#              Main                           #
#                      Section                #
#                                ******       #
###############################################

# The main Func for starting the Program
# Set the Main Frame


global S_Username


def main():
    root = tk.Tk()
    root.geometry('400x200')
    root.title('Library Management System')

    # Buttons in the First Window

    button1 = tk.Button(root, text="Log In as Staff", command=staff_l)
    button1.pack(pady=20)

    button2 = tk.Button(root, text="Log In as Member", command=member_l)
    button2.pack(pady=20)

    button3 = tk.Button(root, text="Sign Up as a New Member", command=member_s)
    button3.pack(pady=20)

    root.mainloop()


###############################################
#     ******                                  #
#              Staff                          #
#                      Section                #
#                                ******       #
###############################################


def staff_l():
    root = tk.Tk()
    root.title('LogIn as Staff')

    # Set The Frame Size

    root.geometry('400x200')
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

    # Labels and textbox for Staff LogIn Window
    # Taking UserName and PassWord From Staff

    label_un = tk.Label(frame, text="Username:")
    label_un.grid(row=0, column=0)
    text_box_un = tk.Entry(frame)
    text_box_un.grid(row=0, column=1)

    label_pass = tk.Label(frame, text="Password:")
    label_pass.grid(row=1, column=0)
    text_box_pass = tk.Entry(frame)
    text_box_pass.grid(row=1, column=1)

    # Commit Button

    button = tk.Button(frame, text="Log In", command=lambda: on_button_click())
    button.grid(row=2, column=1)

    # Check that the given Username\Password is Correct

    def on_button_click():

        S_Username = text_box_un.get()
        password = text_box_pass.get()
        config()

        query = "SELECT * FROM Staff WHERE S_IDNO = ? AND S_Pass = ?"
        cursor.execute(query, (S_Username, password))
        user = cursor.fetchone()

        if user:
            staff_menu()
        else:
            messagebox.showinfo("Error", "Invalid Username or Password!")

    # Staff Menu after SignIn
    # Labels Buttons In Staff Menu Window

    def staff_menu():
        root1 = tk.Tk()
        root1.title('Staff Menu')

        # Set the Frame Size

        root1.geometry('400x200')

        # Buttons in Staff Menu Window

        button1 = tk.Button(root1, text="Manage Books", command=book_manager)
        button1.pack(pady=20)

        button2 = tk.Button(root1, text="Manage Members", command=member_manager)
        button2.pack(pady=20)

        button3 = tk.Button(root1, text="Borrowed Books", command=borrowed)
        button3.pack(pady=20)

    def book_manager():
        window = tk.Tk()
        window.title("Book Managing")

        # Create a multi-column list in the middle of the Staff-BookManager window

        treeview = ttk.Treeview(window,
                                columns=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"),
                                show="headings")
        treeview.heading("Column1", text="Title")
        treeview.heading("Column2", text="ISBN")
        treeview.heading("Column3", text="Edition")
        treeview.heading("Column4", text="Genre")
        treeview.heading("Column5", text="Availability")
        treeview.heading("Column6", text="Publisher")
        treeview.heading("Column7", text="Author")

        cursor.execute("SELECT * FROM Book")
        rows = cursor.fetchall()
        for row in rows:
            treeview.insert("", "end", values=row)
        treeview.pack(pady=20)

        # Buttons at the bottom of the window

        button_frame = tk.Frame(window)
        button_frame.pack(side=tk.BOTTOM, pady=10)

        button1 = tk.Button(button_frame, text="Add New Entry", width=15, command=AddEntry)
        button1.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(button_frame, text="Remove Entry", width=15, command=RemoveEntry)
        button2.pack(side=tk.RIGHT, padx=10)

        window.mainloop()

    def AddEntry():

        root1 = tk.Tk()
        root1.title('Add Book')
        root1.geometry('400x200')

        frame1 = tk.Frame(root1)
        frame1.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

        label1 = tk.Label(frame1, text="Title:")
        label1.grid(row=0, column=0)
        text_box1 = tk.Entry(frame1)
        text_box1.grid(row=0, column=1)

        label2 = tk.Label(frame1, text="ISBN:")
        label2.grid(row=1, column=0)
        text_box2 = tk.Entry(frame1)
        text_box2.grid(row=1, column=1)

        label3 = tk.Label(frame1, text="Edition:")
        label3.grid(row=2, column=0)
        text_box3 = tk.Entry(frame1)
        text_box3.grid(row=2, column=1)

        label4 = tk.Label(frame1, text="Genre:")
        label4.grid(row=3, column=0)
        text_box4 = tk.Entry(frame1)
        text_box4.grid(row=3, column=1)

        label5 = tk.Label(frame1, text="Available:")
        label5.grid(row=4, column=0)
        text_box5 = tk.Entry(frame1)
        text_box5.grid(row=4, column=1)

        label6 = tk.Label(frame1, text="Publisher:")
        label6.grid(row=5, column=0)
        text_box6 = tk.Entry(frame1)
        text_box6.grid(row=5, column=1)

        label7 = tk.Label(frame1, text="Author:")
        label7.grid(row=6, column=0)
        text_box7 = tk.Entry(frame1)
        text_box7.grid(row=6, column=1)

        button1 = tk.Button(frame1, text="ADD", command=lambda: click())
        button1.grid(row=7, column=1)

        def click():
            title = text_box1.get()
            isbn = text_box2.get()
            edition = text_box3.get()
            genre = text_box4.get()
            available = text_box5.get()
            publisher = text_box6.get()
            author = text_box7.get()

            config()

            query = "INSERT INTO Book (Title, ISBN, Edition, Genre, Available, Publisher, Author) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (title, isbn, edition, genre, available, publisher, author))
            conn.commit()

    def RemoveEntry():
        root1 = tk.Tk()
        root1.title('Remove Book')
        root1.geometry('400x200')

        frame1 = tk.Frame(root1)
        frame1.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

        label1 = tk.Label(frame1, text="ISBN:")
        label1.grid(row=0, column=0)
        text_box1 = tk.Entry(frame1)
        text_box1.grid(row=0, column=1)

        button1 = tk.Button(frame1, text="Delete", command=lambda: click())
        button1.grid(row=1, column=1)

        def click():
            isbn = text_box1.get()
            config()
            query = "DELETE FROM Book WHERE ISBN = ?"
            cursor.execute(query, (isbn))
            conn.commit()
            messagebox.showinfo("Success", "Successfully Done")

    def member_manager():
        window = tk.Tk()
        window.title("Member Managing")

        # Create a multi-column list in the middle of the window

        treeview = ttk.Treeview(window, columns=("Column1", "Column2", "Column4", "Column5"), show="headings")
        treeview.heading("Column1", text="Name")
        treeview.heading("Column2", text="ID")

        # treeview.heading("Column3", text="Membership Date")

        treeview.heading("Column4", text="E-mail")
        treeview.heading("Column5", text="Phone Number")
        cursor.execute('SELECT M_Name, M_IDNO, M_Email, M_PhoneNumber FROM Member')

        # query = pd.read_sql_query('SELECT * FROM Member')
        # query['MembershipDate'] = pd.to_datetime(query['MembershipDate'] ,format='%Y-%m-%d')

        rows = cursor.fetchall()
        for row in rows:
            treeview.insert("", "end", values=row)
        treeview.pack(pady=20)

        # Create two buttons at the bottom of the window

        button_frame = tk.Frame(window)
        button_frame.pack(side=tk.BOTTOM, pady=10)

        button2 = tk.Button(button_frame, text="Remove Member", width=15, command=lambda: remove_mem())
        button2.pack(padx=10)

        def remove_mem():
            root1 = tk.Tk()
            root1.title('Remove Member')
            root1.geometry('400x200')

            frame1 = tk.Frame(root1)
            frame1.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

            label1 = tk.Label(frame1, text="Member ID:")
            label1.grid(row=0, column=0)
            text_box1 = tk.Entry(frame1)
            text_box1.grid(row=0, column=1)

            button1 = tk.Button(frame1, text="Delete", command=lambda: click())
            button1.grid(row=1, column=1)

            def click():
                mid = text_box1.get()
                config()
                query = "DELETE FROM Member WHERE M_IDNO = ?"
                cursor.execute(query, (mid))
                conn.commit()
                messagebox.showinfo("Success", "Successfully Done")

        window.mainloop()

    def borrowed():
        window = tk.Tk()
        window.title("Borrowed Books")

        # Create a multi-column list in the middle of the window

        treeview = ttk.Treeview(window, columns=("Column1", "Column2"),
                                show="headings")
        treeview.heading("Column1", text="Member_ID")
        treeview.heading("Column2", text="ISBN")

        # treeview.heading("Column3", text="Borrow_Date")
        # treeview.heading("Column4", text="Due_Date")

        cursor.execute('SELECT * FROM Borrow')
        rows = cursor.fetchall()
        for row in rows:
            treeview.insert("", "end", values=row)
        treeview.pack(pady=20)

        window.mainloop()


###############################################
#     ******                                  #
#              Member                         #
#                      Section                #
#                                ******       #
###############################################


def member_l():
    root = tk.Tk()
    root.title('LogIn as Member')

    # Set the Frame Size

    root.geometry('400x200')
    frame = tk.Frame(root)

    # Place frame in the center

    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Labels and textbox for Member LogIn Window
    # Taking UserName and PassWord From Member

    label1 = tk.Label(frame, text="Username:")
    label1.grid(row=0, column=0)
    text_box1 = tk.Entry(frame)
    text_box1.grid(row=0, column=1)

    # username = text_box1.get()

    label2 = tk.Label(frame, text="Password:")
    label2.grid(row=1, column=0)
    text_box2 = tk.Entry(frame)
    text_box2.grid(row=1, column=1)

    # password = text_box2.get()

    # Commit Button

    button = tk.Button(frame, text="Log In", command=lambda: on_button_click())
    button.grid(row=2, column=1)

    # Check that the given Username\Password is Correct

    def on_button_click():
        M_Username= text_box1.get()
        password = text_box2.get()
        config()

        query = "SELECT * FROM Member WHERE M_IDNO = ? AND M_Pass = ?"
        cursor.execute(query, (M_Username, password))
        user = cursor.fetchone()

        if user:
            member_menu()

        else:
            messagebox.showinfo("Error", "Invalid username or password!")

    def member_menu():
        root1 = tk.Tk()
        root1.title('Member Menu')
        root1.geometry('400x200')

      #  button1 = tk.Button(root1, text="Profile", command=lambda: ProfileView())
       # button1.pack(pady=20)

        button2 = tk.Button(root1, text="View books", command=lambda: viewbooks())
        button2.pack(pady=20)

        button3 = tk.Button(root1, text="Return Books", command=lambda: returnbooks())
        button3.pack(pady=20)

        #def ProfileView():
            #root2 = tk.Tk()
            #root2.title('My Profile')

            # Set The Frame Size
            #root.geometry('400x200')
            #frame = tk.Frame(root2)
            #frame.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

           # config()
          #  query = "Select M_name FROM Member WHERE M_IDNO = ? "
           # cursor.execute(query, (username))
           # name = cursor.fetchall()
          #  labelname1 = tk.Label(frame, text="Name: ")
          #  labelname1.grid(row=0, column=0)
           # labelname2 = tk.Entry(frame)
          #  labelname2.grid(row=0, column=1)

         #   labelname2 = tk.Label(frame, text="Username:")
           # labelname2.grid(row=0, column=0)
          #  text_box_un = tk.Entry(frame)
           # text_box_un.grid(row=0, column=1)

           # labelname3 = tk.Label(frame, text="Username:")
           # labelname3.grid(row=0, column=0)
          #  text_box_un = tk.Entry(frame)
          #  text_box_un.grid(row=0, column=1)

          #  labelname4 = tk.Label(frame, text="Username:")
         #   labelname4.grid(row=0, column=0)
         ##  text_box_un = tk.Entry(frame)
          #  text_box_un.grid(row=0, column=1)

            #window.mainloop()

        def viewbooks():
            window = tk.Tk()
            window.title("View Available Books")

            # Create a multi-column list in the middle of the window

            treeview = ttk.Treeview(window,
                                    columns=(
                                        "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"),
                                    show="headings")
            treeview.heading("Column1", text="Title")
            treeview.heading("Column2", text="ISBN")
            treeview.heading("Column3", text="Edition")
            treeview.heading("Column4", text="Genre")
            treeview.heading("Column5", text="Availability")
            treeview.heading("Column6", text="Publisher")
            treeview.heading("Column7", text="Author")

            query = f"SELECT * FROM Book WHERE Available='true'"
            rows = cursor.execute(query).fetchall()

            for row in rows:
                treeview.insert("", "end", values=row)
            treeview.pack(pady=20)

            # Create buttons at the bottom of the window

            button_frame = tk.Frame(window)
            button_frame.pack(side=tk.BOTTOM, pady=10)

            button1 = tk.Button(button_frame, text="Borrow", width=15, command=lambda: borrowbooks())
            button1.pack(side=tk.LEFT, padx=10)

            window.mainloop()
        
        def borrowbooks():
            root1 = tk.Tk()
            root1.title('Borrow Book')
            root1.geometry('400x200')

            frame1 = tk.Frame(root1)
            frame1.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

            label1 = tk.Label(frame1, text="ISBN:")
            label1.grid(row=0, column=0)
            text_box1 = tk.Entry(frame1)
            text_box1.grid(row=0, column=1)

            label2 = tk.Label(frame1, text="ID no.:")
            label2.grid(row=1, column=0)
            text_box2 = tk.Entry(frame1)
            text_box2.grid(row=1, column=1)

            button1 = tk.Button(frame1, text="Borrow", command=lambda: click())
            button1.grid(row=2, column=1)

            def click():
                config()
                isbn = text_box1.get()
                mid = text_box2.get()
                today = date.today()
                end_date = today + datetime.timedelta(days=10)
                
                query = "UPDATE Book SET Available = 0 WHERE ISBN = ?"
                cursor.execute(query, (isbn))
                conn.commit()
                query1 = "INSERT INTO Borrow(M_IDNO, ISBN, BorrowDate, DueDate) VALUES(?, ?, ?, ?)"
                cursor.execute(query1, (mid, isbn, today, end_date))
                messagebox.showinfo("Success", "Book Borrowd!")


        def returnbooks():
            window = tk.Tk()
            window.title("Return My Books")

            # Create a multi-column list in the middle of the window

            treeview = ttk.Treeview(window,
                                    columns=(
                                        "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"),
                                    show="headings")
            treeview.heading("Column1", text="Title")
            treeview.heading("Column2", text="ISBN")
            treeview.heading("Column3", text="Edition")
            treeview.heading("Column4", text="Genre")
            treeview.heading("Column5", text="Availability")
            treeview.heading("Column6", text="Publisher")
            treeview.heading("Column7", text="Author")

            query = f"SELECT * FROM Book WHERE Available='false'"
            rows = cursor.execute(query).fetchall()

            for row in rows:
                treeview.insert("", "end", values=row)
            treeview.pack(pady=20)

            # Create buttons at the bottom of the window

            button_frame = tk.Frame(window)
            button_frame.pack(side=tk.BOTTOM, pady=10)

            button1 = tk.Button(button_frame, text="Return", width=15, command=lambda: returnb())
            button1.pack(side=tk.LEFT, padx=10)

            def returnb():
                root1 = tk.Tk()
                root1.title('Return Book')
                root1.geometry('400x200')

                frame1 = tk.Frame(root1)
                frame1.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center

                label1 = tk.Label(frame1, text="ISBN:")
                label1.grid(row=0, column=0)
                text_box1 = tk.Entry(frame1)
                text_box1.grid(row=0, column=1)

                button1 = tk.Button(frame1, text="Return", command=lambda: click())
                button1.grid(row=1, column=1)

                def click():
                    config()
                    isbn = text_box1.get()
                    query = "UPDATE Book SET Available = 1 WHERE ISBN = ?"
                    cursor.execute(query, (isbn))
                    conn.commit()
                    query1 = "DELETE FROM Borrow WHERE ISBN = ?"
                    cursor.execute(query1, (isbn))
                    messagebox.showinfo("Success", "Book Returned!")

            window.mainloop()




###############################################
#     ******                                  #
#              SignUP                         #
#                      Section                #
#                                ******       #
###############################################


def member_s():
    root = tk.Tk()
    root.title('Sign Up as Member')
    root.geometry('400x200')
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor='center')  # Place frame in the center
    label1 = tk.Label(frame, text="Name:")
    label1.grid(row=0, column=0)
    text_box1 = tk.Entry(frame)
    text_box1.grid(row=0, column=1)
    # name = text_box1.get()

    label2 = tk.Label(frame, text="ID:")
    label2.grid(row=1, column=0)
    text_box2 = tk.Entry(frame)
    text_box2.grid(row=1, column=1)
    # ID = text_box2.get()

    label3 = tk.Label(frame, text="E-mail:")
    label3.grid(row=2, column=0)
    text_box3 = tk.Entry(frame)
    text_box3.grid(row=2, column=1)
    # email = text_box3.get()

    label4 = tk.Label(frame, text="Phone Number:")
    label4.grid(row=3, column=0)
    text_box4 = tk.Entry(frame)
    text_box4.grid(row=3, column=1)
    # phn = text_box4.get()

    label5 = tk.Label(frame, text="Password:")
    label5.grid(row=4, column=0)
    text_box5 = tk.Entry(frame)
    text_box5.grid(row=4, column=1)
    # password = text_box5.get()

    button = tk.Button(frame, text="Sign Up", command=lambda: on_button_click())
    button.grid(row=5, column=1)

    def on_button_click():
        name = text_box1.get()
        ID = text_box2.get()
        email = text_box3.get()
        phn = text_box4.get()
        password = text_box5.get()
        today = date.today()

        print(name, ID, email, phn, password, today)
        config()

        query = "INSERT INTO Member (M_Name, M_IDNO, MembershipDate, M_Email, M_PhoneNumber, M_Pass) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (name, ID, today, email, phn, password))

        conn.commit()
        messagebox.showinfo("Success", "Signed UP!\n Go back and log in with your credentials!")
    # user = cursor.fetchone()
    # if user:
    #   messagebox.showinfo("Success", "Signed UP!\n Go back and log in with your credentials!")

    #  else:
    #     messagebox.showinfo("Error", "Invalid Entry!")


if __name__ == '__main__':
    main()
