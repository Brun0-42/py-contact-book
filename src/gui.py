# coding: utf-8

import tkinter
import logging

#---------------------------------------------------------------------------# 
class ContactGui:
	def __init__(self, contacts_list):
		label_width = 15
		edit_width = 40

		self._contacts_list = contacts_list
		self._root = tkinter.Tk()
		self._root.geometry('500x500')

		# Contact list
		self._frame_contacts = tkinter.Frame()
		self._frame_contacts.pack(pady=10)

		self._contacts_scroll_bar = tkinter.Scrollbar(self._frame_contacts)
		self._contacts_scroll_bar.pack( side = tkinter.RIGHT, fill = tkinter.Y )

		self._contacts_listbox = tkinter.Listbox(self._frame_contacts, yscrollcommand=self._contacts_scroll_bar.set, width=400, height=10)
		self._contacts_listbox.pack(side = tkinter.LEFT, fill = tkinter.BOTH )

		self._contacts_scroll_bar.config (command= self._contacts_listbox.yview)

		# Button
		self._frame_button = tkinter.Frame()
		self._frame_button.pack(pady=10)
		tkinter.Button(self._frame_button,text="View",font="arial 12 bold",command=self.view).pack(side=tkinter.RIGHT)

		# Given name
		self._frame_given_name = tkinter.Frame()
		self._frame_given_name.pack(pady=10)

		self._given_name = tkinter.StringVar()

		tkinter.Label(self._frame_given_name, text = 'Name', font='arial 12 bold', width=label_width).pack(side=tkinter.LEFT)
		tkinter.Entry(self._frame_given_name, textvariable = self._given_name,width=edit_width).pack()

		# Familly name
		self._frame_family_name = tkinter.Frame()
		self._frame_family_name.pack()

		self._family_name = tkinter.StringVar()

		tkinter.Label(self._frame_family_name, text = 'first name', font='arial 12 bold', width=label_width).pack(side=tkinter.LEFT)
		tkinter.Entry(self._frame_family_name, textvariable = self._family_name,width=edit_width).pack()

		# Phone number
		self._frame_phone_number = tkinter.Frame()
		self._frame_phone_number.pack(pady=10)

		self._phone_number = tkinter.StringVar()

		tkinter.Label(self._frame_phone_number, text = 'Phone No.', font='arial 12 bold', width=label_width).pack(side=tkinter.LEFT)
		tkinter.Entry(self._frame_phone_number, textvariable = self._phone_number,width=edit_width).pack()

		self.update()
		
	def update(self):
		self._contacts_listbox.delete(0, tkinter.END)
		for contact in self._contacts_list:
			self._contacts_listbox.insert(tkinter.END, str(contact._name))

	# View Information
	def view(self):
		contact = self._contacts_list[int(self._contacts_listbox.curselection()[0])]
		self._given_name.set(contact._name._given_name)
		self._family_name.set(contact._name._family_name)
		self._phone_number.set(contact._phone)

	def run(self):
		self._root.mainloop()
