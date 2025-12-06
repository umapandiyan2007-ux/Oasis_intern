import tkinter as tk



# Function to calculate BMI

def calculate_bmi():

    try:

        height = float(entry_height.get())

        weight = float(entry_weight.get())



        # If height is in cm, convert to meters

        if height > 3:

            height = height / 100  



        bmi = weight / (height ** 2)

        result.set(f"Your BMI: {bmi:.2f}")

        

        if bmi < 18.5:

            status.set("Underweight")

            status_label.config(fg="blue")

        elif 18.5 <= bmi < 24.9:

            status.set("Normal weight")

            status_label.config(fg="green")

        elif 25 <= bmi < 29.9:

            status.set("Overweight")

            status_label.config(fg="orange")

        else:

            status.set("Obese")

            status_label.config(fg="red")

    except:

        result.set("Invalid input!")

        status.set("")

        status_label.config(fg="black")



# Function to clear fields

def clear_fields():

    entry_height.delete(0, tk.END)

    entry_weight.delete(0, tk.END)

    result.set("")

    status.set("")

    status_label.config(fg="black")



# Main window

root = tk.Tk()

root.title("BMI Calculator")

root.geometry("350x250")

root.resizable(False, False)



# Input frame

frame_input = tk.Frame(root)

frame_input.pack(pady=10)



tk.Label(frame_input, text="Height (cm or m):").grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_height = tk.Entry(frame_input)

entry_height.grid(row=0, column=1, padx=5, pady=5)



tk.Label(frame_input, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_weight = tk.Entry(frame_input)

entry_weight.grid(row=1, column=1, padx=5, pady=5)



# Button frame

frame_buttons = tk.Frame(root)

frame_buttons.pack(pady=5)



tk.Button(frame_buttons, text="Calculate BMI", command=calculate_bmi, width=15).grid(row=0, column=0, padx=5)

tk.Button(frame_buttons, text="Clear", command=clear_fields, width=10).grid(row=0, column=1, padx=5)



# Output

result = tk.StringVar()

status = tk.StringVar()



tk.Label(root, textvariable=result, font=("Arial", 12, "bold")).pack(pady=5)

status_label = tk.Label(root, textvariable=status, font=("Arial", 11, "bold"))

status_label.pack()



root.mainloop()
