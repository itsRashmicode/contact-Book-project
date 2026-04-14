
import tkinter as tk
from tkinter import messagebox

contacts = []

# Add Contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact Added!")
    clear_fields()
    view_contacts()

# View Contacts
def view_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search Contact
def search_contact():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Delete Contact
def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact!")
        return

    index = selected[0]
    del contacts[index]
    view_contacts()

# Update Contact
def update_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact!")
        return

    index = selected[0]
    contacts[index] = {
        "name": entry_name.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get(),
        "address": entry_address.get()
    }
    messagebox.showinfo("Updated", "Contact Updated!")
    view_contacts()

# Fill fields when clicking list
def fill_fields(event):
    selected = listbox.curselection()
    if selected:
        contact = contacts[selected[0]]
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

        entry_name.insert(0, contact['name'])
        entry_phone.insert(0, contact['phone'])
        entry_email.insert(0, contact['email'])
        entry_address.insert(0, contact['address'])

# Clear fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Labels & Entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Search
tk.Label(root, text="Search").pack()
entry_search = tk.Entry(root)
entry_search.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", fill_fields)

# Run App
root.mainloop()