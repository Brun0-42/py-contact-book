# coding: utf-8

import tkinter
import logging

#---------------------------------------------------------------------------# 
class ContactGui:
	def __init__(self, contacts_list, title="Main view", icon_path=None):
		self._contacts_list = contacts_list

		self._root = tkinter.Tk()
		self._root.geometry('600x400')
		self._root.title(title)

		#if icon_path is not None:
		self._root.iconphoto(False, tkinter.PhotoImage(file=icon_path))

	    # layout on the root window
		self._root.columnconfigure(0, weight=100)
		self._root.columnconfigure(1, weight=10)

		self._list_frame = self._create_list_edit_label_frame(self._root)
		self._list_frame.grid(column=0, row=0)

		self._button_frame = self._create_button_frame(self._root)
		self._button_frame.grid(column=1, row=0)

	def _create_list_edit_label_frame(self, container):
		frame = tkinter.Frame(container)

		frame.columnconfigure(0, weight=1)
		frame.rowconfigure(0, weight=50)
		frame.rowconfigure(1, weight=50)

		list_frame = self._create_list_frame(frame)
		list_frame.grid(column=0, row=0)

		edit_contact_frame = self._edit_contact_frame(frame)
		edit_contact_frame.grid(column=0, row=1)

		for widget in frame.winfo_children():
			widget.grid(padx=5, pady=5)

		return frame

	def _create_list_frame(self, container):
		frame = tkinter.Frame(container)

		self._contacts_scroll_bar=tkinter.Scrollbar(frame, orient="vertical")
		self._contacts_scroll_bar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

		self._contacts_listbox = tkinter.Listbox(frame, yscrollcommand=self._contacts_scroll_bar.set, width=50, height=10)
		self._contacts_listbox.pack(side = tkinter.RIGHT, fill = tkinter.BOTH )

		self.update()

		return frame
		
	def _create_button_frame(self, container):
		frame = tkinter.Frame(container)

		frame.columnconfigure(0)

		tkinter.Button(frame, text='View', command=self.view).grid(column=0, row=0)
		# tkinter.Button(frame, text='fffff').grid(column=0, row=1)
		# tkinter.Button(frame, text='aaaaa').grid(column=0, row=2)
		# tkinter.Button(frame, text='bbbbb').grid(column=0, row=3)

		for widget in frame.winfo_children():
			widget.grid(padx=5, pady=5)

		return frame

	def _edit_contact_frame(self, container):
		edit_width = 30

		frame = tkinter.Frame(container)

		frame.columnconfigure(0, weight=10)

		tkinter.Label(frame, text='Family name:').grid(column=0, row=0)
		tkinter.Label(frame, text='First name:').grid(column=0, row=1)
		tkinter.Label(frame, text='Phone No.:').grid(column=0, row=2)

		self._family_name = tkinter.StringVar()
		self._given_name = tkinter.StringVar()
		self._phone_number = tkinter.StringVar()

		frame.columnconfigure(1, weight=10)
		tkinter.Entry(frame, textvariable = self._family_name,width=edit_width).grid(column=1, row=0)
		tkinter.Entry(frame, textvariable = self._given_name,width=edit_width).grid(column=1, row=1)
		tkinter.Entry(frame, textvariable = self._phone_number,width=edit_width).grid(column=1, row=2)

		for widget in frame.winfo_children():
			widget.grid(padx=5, pady=5)

		return frame

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
