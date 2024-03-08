import pymysql
from tkinter import *
from tkinter import messagebox

def insertData():
    conn, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

    conn = pymysql.connect(host='127.0.0.1', user='root', password='98765432!', db='studentdb', charset='utf8')
    cur = conn.cursor()

    data1 = edt1.get() 
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()

    try: 
        # Use placeholders to avoid SQL injection
        sql = "INSERT INTO userTable VALUES(%s, %s, %s, %s)"
        cur.execute(sql, (data1, data2, data3, data4))
        conn.commit()
        messagebox.showinfo("Success", "Successfully inserted the data")
    except Exception as e:
        messagebox.showerror("Error", f"Data Input Error: {e}")
    finally:
        conn.close()

def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='98765432!', db='studentdb', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userTable")

    rows = cur.fetchall()  

    for row in rows:
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])

    listData1.delete(0, END)
    listData2.delete(0, END)
    listData3.delete(0, END)
    listData4.delete(0, END)

    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)

    conn.close()

def deleteData():
    conn, cur = None, None
    user_id = edt1.get()  # Get the User ID from the entry widget

    if user_id:
        try:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='98765432!', db='studentdb', charset='utf8')
            cur = conn.cursor()

            cur.execute("SELECT * FROM userTable WHERE id = %s", (user_id,))
            existing_records = cur.fetchall()

            if existing_records:
                sql = "DELETE FROM userTable WHERE id = %s"
                cur.execute(sql, (user_id,))
                conn.commit()
                messagebox.showinfo("Success", f"Successfully deleted all records with User ID: {user_id}")
            else:
                messagebox.showinfo("Error", f"No records found with User ID: {user_id}")
        except Exception as e:
            messagebox.showerror("Error", f"Data Deletion Error: {e}")
        finally:
            if conn:
                conn.close()
            selectData()  
    else:
        messagebox.showinfo("Error", "Please enter a User ID")


# GUI setup
window = Tk()
window.geometry("800x300")
window.title("Insert and Search Data")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

# Labels
Label(edtFrame, text="Student ID").grid(row=0, column=0, padx=5, pady=5)
Label(edtFrame, text="First Name").grid(row=0, column=1, padx=5, pady=5)
Label(edtFrame, text="Last Name").grid(row=0, column=2, padx=5, pady=5)
Label(edtFrame, text="Age").grid(row=0, column=3, padx=5, pady=5)

# Entry widgets
edt1 = Entry(edtFrame, width=10)
edt1.grid(row=1, column=0, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10)
edt2.grid(row=1, column=1, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10)
edt3.grid(row=1, column=2, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10)
edt4.grid(row=1, column=3, padx=10, pady=10)

# Buttons
btnInsert = Button(edtFrame, text="Insert", command=insertData)
btnInsert.grid(row=2, column=0, padx=10, pady=10)
btnSearch = Button(edtFrame, text="Search", command=selectData)
btnSearch.grid(row=2, column=1, padx=10, pady=10)
btnDelete = Button(edtFrame, text="Delete", command=deleteData)
btnDelete.grid(row=2, column=2, padx=10, pady=10)

# Listboxes
listData1 = Listbox(listFrame, bg="yellow")
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg="yellow")
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg="yellow")
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg="yellow")
listData4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
