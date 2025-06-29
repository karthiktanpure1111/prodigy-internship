import tkinter as tk
from tkinter import messagebox, simpledialog
import os

CONTACT_FILE = "contacts.txt"

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📒 Contact Manager")
        self.root.geometry("500x400")

        self.contacts = []
        self.load_contacts()

        # GUI Components
        self.listbox = tk.Listbox(root, font=("Arial", 12), height=10, width=60)
        self.listbox.pack(pady=10)

        self.refresh_listbox()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add", command=self.add_contact, bg="lightgreen", width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Edit", command=self.edit_contact, bg="khaki", width=10).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_contact, bg="tomato", width=10).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Save & Exit", command=self.save_and_exit, bg="skyblue", width=15).grid(row=0, column=3, padx=5)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, contact in enumerate(self.contacts):
            self.listbox.insert(tk.END, f"{idx+1}. {contact}")

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter name:")
        phone = simpledialog.askstring("Phone", "Enter phone number:")
        email = simpledialog.askstring("Email", "Enter email:")

        if name and phone and email:
            self.contacts.append(Contact(name, phone, email))
            self.refresh_listbox()
        else:
            messagebox.showwarning("Invalid", "All fields are required.")

    def edit_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Contact", "Please select a contact to edit.")
            return

        index = selected[0]
        contact = self.contacts[index]

        name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=contact.name)
        phone = simpledialog.askstring("Edit Phone", "Enter new phone:", initialvalue=contact.phone)
        email = simpledialog.askstring("Edit Email", "Enter new email:", initialvalue=contact.email)

        if name and phone and email:
            contact.name = name
            contact.phone = phone
            contact.email = email
            self.refresh_listbox()

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Contact", "Please select a contact to delete.")
            return

        index = selected[0]
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
        if confirm:
            del self.contacts[index]
            self.refresh_listbox()

    def save_and_exit(self):
        with open(CONTACT_FILE, "w") as f:
            for contact in self.contacts:
                f.write(f"{contact.name}\n{contact.phone}\n{contact.email}\n")
        messagebox.showinfo("Saved", "Contacts saved successfully!")
        self.root.quit()

    def load_contacts(self):
        if not os.path.exists(CONTACT_FILE):
            return
        try:
            with open(CONTACT_FILE, "r") as f:
                lines = f.readlines()
                for i in range(0, len(lines), 3):
                    name = lines[i].strip()
                    phone = lines[i+1].strip()
                    email = lines[i+2].strip()
                    self.contacts.append(Contact(name, phone, email))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load contacts: {str(e)}")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
