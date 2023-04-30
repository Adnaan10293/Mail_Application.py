import tkinter as tk
import smtplib

def send_email():
    # Get the input values from the GUI
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    message = message_entry.get("1.0", tk.END)

    # Connect to the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()

    # Login to the sender's email account
    smtp_connection.login(sender_email, sender_password)

    # Construct the email message
    email_message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(sender_email, receiver_email, subject, message)

    # Send the email
    smtp_connection.sendmail(sender_email, receiver_email, email_message)

    # Close the SMTP connection
    smtp_connection.quit()

    # Show a success message
    success_label.config(text="Email sent successfully!")

# Create the main window
window = tk.Tk()
window.title("Adnaan-Mail")

# Create the input fields and labels
sender_email_label = tk.Label(window, text="Sender Email:")
sender_email_entry = tk.Entry(window)
sender_password_label = tk.Label(window, text="Sender Password:")
sender_password_entry = tk.Entry(window, show="*")
receiver_email_label = tk.Label(window, text="Receiver Email:")
receiver_email_entry = tk.Entry(window)
subject_label = tk.Label(window, text="Subject:")
subject_entry = tk.Entry(window)
message_label = tk.Label(window, text="Message:")
message_entry = tk.Text(window, height=10, width=50)
send_button = tk.Button(window, text="Send Email", command=send_email)
success_label = tk.Label(window, text="")

# Add the input fields and labels to the window
sender_email_label.grid(row=0, column=0)
sender_email_entry.grid(row=0, column=1)
sender_password_label.grid(row=1, column=0)
sender_password_entry.grid(row=1, column=1)
receiver_email_label.grid(row=2, column=0)
receiver_email_entry.grid(row=2, column=1)
subject_label.grid(row=3, column=0)
subject_entry.grid(row=3, column=1)
message_label.grid(row=4, column=0)
message_entry.grid(row=4, column=1)
send_button.grid(row=5, column=1)
success_label.grid(row=6, column=1)

# Start the main loop
window.mainloop()
