import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

# Function to run the second script

# Function to run the first script (same as the first one in this example)
def run_script_1():
    try:
        subprocess.run(['python', 'inputemployeedateExcel.py'], check=True)
    #    messagebox.showinfo("Success", "Script 4 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 4: {e}")

# Function to run the Second script
def run_script_2():
    try:
        subprocess.run(['python', 'DailyAttendanceByLastEmployee02.py'], check=True)
    #    messagebox.showinfo("Success", "Script 1 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 1: {e}")

# Function to run the Third script
def run_script_3():
    try:
        subprocess.run(['python', 'DailyAttendanceByLastEmployee03.py'], check=True)
    #    messagebox.showinfo("Success", "Script 2 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 2: {e}")

# Function to run the Forth script
def run_script_4():
    try:
        subprocess.run(['python', 'inputemployeedate.py'], check=True)
    #    messagebox.showinfo("Success", "Script 2 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 2: {e}")
# Function to run the Fifth script
def run_script_5():
    try:
        subprocess.run(['python', 'SendTextFile.py'], check=True)
    #    messagebox.showinfo("Success", "Script 3 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 3: {e}")
        
# Function to quit the application

# Function to run the Sixth script
def run_script_6():
    try:
        subprocess.run(['python', 'InputEmployeeDatePdf.py'], check=True)
    #    messagebox.showinfo("Success", "Script 3 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 3: {e}")

# Function to run the Seventh script
def run_script_7():
    try:
        subprocess.run(['python', 'InputEmployeeDatePdfA1.py'], check=True)
    #    messagebox.showinfo("Success", "Script 3 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 3: {e}")
        
# Function to run the Eigth script
def run_script_8():
    try:
        subprocess.run(['python', 'InputEmployeeDatePdfA2.py'], check=True)
    #    messagebox.showinfo("Success", "Script 3 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 3: {e}")

def run_script_9():
    try:
        # Daily Attendance - Summary
        subprocess.run(['python', 'DailyAttendanceByLastEmployee04S.py'], check=True)
    #    messagebox.showinfo("Success", "Script 3 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 3: {e}")

def run_script_10():
    try:
        # Daily Attendance - Details
        subprocess.run(['python', 'DailyAttendanceByLastEmployee04.py'], check=True)
    #    messagebox.showinfo("Success", "Script 3 ran successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error running Script 3: {e}")

# Function to quit the application
def quit_app():
    root.quit()

# Main Tkinter window
root = tk.Tk()
root.title("Employee Attendance")

# Set window size and center it
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Create the notebook for tabs
notebook = ttk.Notebook(root)

# Create the first tab frame
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Master')

# Create the second tab frame
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Transactions')

# Create the Third tab frame
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='PDF Options')

# Create the Forth tab frame
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Quit Options')


# Add buttons for scripts in Tab 1
btn1_tab1 = tk.Button(tab1, text=" Basic Attendance ", command=run_script_1)
btn1_tab1.pack(pady=10)

btn1_tab3 = tk.Button(tab1, text="Daily Attendance Summary", command=run_script_9)
btn1_tab3.pack(pady=10)

# btn1_tab3 = tk.Button(tab1, text="Daily Attendance Details", command=run_script_10)
# btn1_tab3.pack(pady=10)

# To Quit 
btn2_tab1 = tk.Button(tab1, text=" Quit Application ", command=quit_app)
btn2_tab1.pack(pady=10)

# Add buttons for scripts in Tab 2
btn1_tab2 = tk.Button(tab2, text=" Daily Attendance Details", command=run_script_2)
btn1_tab2.pack(pady=10)

btn2_tab2 = tk.Button(tab2, text="Attendance By Dept", command=run_script_3)
btn2_tab2.pack(pady=10)

btn3_tab2 = tk.Button(tab2, text=" Attendance By Date", command=run_script_4)
btn3_tab2.pack(pady=10)

btn4_tab2 = tk.Button(tab2, text=" Attendance Export", command=run_script_5)
btn4_tab2.pack(pady=10)

# Add buttons for scripts in Tab 3
btn1_tab3 = tk.Button(tab3, text="  Daily Attendance PDF ", command=run_script_6)
btn1_tab3.pack(pady=10)

btn1_tab3 = tk.Button(tab3, text="Daily Attendance PDF A1", command=run_script_7)
btn1_tab3.pack(pady=10)

btn1_tab3 = tk.Button(tab3, text="Daily Attendance PDF A2", command=run_script_8)
btn1_tab3.pack(pady=10)

# To Quit
btn1_tab3 = tk.Button(tab3, text=" Quit Application ", command=quit_app)
btn1_tab3.pack(pady=10)

# To Quit
btn4_tab2 = tk.Button(tab2, text=" Quit Application ", command=quit_app)
btn4_tab2.pack(pady=10)

# Add an exit button in Tab 4 (or Quit options)
btn_exit = tk.Button(tab4, text=" Quit Application ", command=quit_app)
btn_exit.pack(pady=10)

# Pack the notebook (tabs) into the main window
notebook.pack(expand=True, fill='both')

# Start the Tkinter main loop
root.mainloop()
