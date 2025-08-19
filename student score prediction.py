import tkinter as tk
from tkinter import messagebox
import numpy as np

# ----------------- Mock Prediction Function -----------------
def simple_predict(input_data):
    """
    A simple formula-based predictor instead of ML model.
    This is just for demo purposes.
    """
    study, attendance, sleep, previous, tutoring, activity = input_data

    # Simple weighted formula
    score = (
        (study * 5) +           # more hours studied → more marks
        (attendance * 0.3) +    # attendance adds
        (sleep * 2) +           # healthy sleep helps
        (previous * 0.4) +      # previous performance
        (tutoring * 3) +        # tutoring boosts
        (activity * 1.5)        # physical activity impact
    )

    return min(100, max(0, score))  # keep score between 0–100

# ----------------- Functions -----------------
def predict_score():
    try:
        # Get inputs
        study = float(entry_study.get())
        attendance = float(entry_attendance.get())
        sleep = float(entry_sleep.get())
        previous = float(entry_previous.get())
        tutoring = float(entry_tutoring.get())
        activity = float(entry_activity.get())

        # Predict using formula
        input_data = np.array([study, attendance, sleep, previous, tutoring, activity])
        prediction = simple_predict(input_data)

        # Display
        result_label.config(
            text=f"📊 Predicted Score: {prediction:.2f}",
            fg="#004080"
        )
    except ValueError:
        messagebox.showerror("⚠ Input Error", "Please enter valid numeric values!")

def reset_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    result_label.config(text="Predicted Score: ", fg="#004080")

def on_enter(e):
    e.widget["background"] = "#0066cc"

def on_leave(e):
    e.widget["background"] = "#3399ff"

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("🎓 Student Exam Score Predictor")
root.geometry("650x600")
root.configure(bg="#f0f8ff")   # light blue background
root.resizable(False, False)

# ----------------- Header -----------------
header = tk.Label(
    root,
    text="✨ Student Exam Score Predictor ✨",
    bg="#3399ff",
    fg="white",
    font=("Helvetica", 20, "bold"),
    pady=15
)
header.pack(fill="x")

# ----------------- Form -----------------
form_frame = tk.Frame(root, bg="#f0f8ff", pady=20)
form_frame.pack(pady=15)

labels = [
    "Hours Studied",
    "Attendance (%)",
    "Sleep Hours",
    "Previous Scores",
    "Tutoring Sessions",
    "Physical Activity"
]
entries = []

for i, label_text in enumerate(labels):
    lbl = tk.Label(
        form_frame,
        text=label_text + ":",
        font=("Arial", 12, "bold"),
        bg="#f0f8ff",
        fg="#003366",
        anchor="w"
    )
    lbl.grid(row=i, column=0, padx=15, pady=8, sticky="w")
    entry = tk.Entry(
        form_frame,
        font=("Arial", 12),
        width=30,
        bd=1,
        relief="solid",
        highlightbackground="#3399ff",
        highlightthickness=1
    )
    entry.grid(row=i, column=1, padx=15, pady=8)
    entries.append(entry)

entry_study, entry_attendance, entry_sleep, entry_previous, entry_tutoring, entry_activity = entries

# ----------------- Buttons -----------------
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=15)

btn_predict = tk.Button(
    btn_frame,
    text="🔮 Predict",
    font=("Arial", 14, "bold"),
    bg="#3399ff",
    fg="white",
    padx=20,
    pady=10,
    relief="flat",
    command=predict_score
)
btn_predict.grid(row=0, column=0, padx=20)
btn_predict.bind("<Enter>", on_enter)
btn_predict.bind("<Leave>", on_leave)

btn_reset = tk.Button(
    btn_frame,
    text="♻ Reset",
    font=("Arial", 14, "bold"),
    bg="#cccccc",
    fg="#003366",
    padx=20,
    pady=10,
    relief="flat",
    command=reset_fields
)
btn_reset.grid(row=0, column=1, padx=20)

# ----------------- Result -----------------
result_label = tk.Label(
    root,
    text="Predicted Score: ",
    bg="#f0f8ff",
    font=("Helvetica", 18, "bold"),
    fg="#004080"
)
result_label.pack(pady=30)

# ----------------- Footer -----------------
footer = tk.Label(
    root,
    text="Designed with ❤ using Python",
    bg="#f0f8ff",
    fg="gray",
    font=("Arial", 10, "italic")
)
footer.pack(side="bottom", pady=10)

# ----------------- Run -----------------
root.mainloop()
