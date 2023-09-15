#!/usr/bin/python3
import sys
import tkinter as tk
import tkinter.ttk as ttk
import assets
from assets import global_var
from assets.function_animate import write_json_a
from assets.function_animation_controller import write_json_ac
from assets.function_initialize import write_json_i
from assets.function_pre_animation import write_json_pa
from assets.function_render_controller import write_json_rc
from assets.function_pack_file_select import pack_file_select
from assets.function_pack_create import pack_create

class EntityPackCompatibilityV001App:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)

        #set title
        toplevel1.title(global_var.pack_name)

        #set icon
        self.img_dataassets_global_var = tk.PhotoImage(
            data=assets.global_var.gui_base64)
        toplevel1.iconphoto(True, self.img_dataassets_global_var)

        frame1 = ttk.Frame(toplevel1)
        frame1.configure(height=200, width=200)
        entry1 = ttk.Entry(frame1)
        self.entry_a = tk.StringVar(
            value='pack_a\\entity\\armor_stand.entity.json')
        entry1.configure(textvariable=self.entry_a, width=40)
        _text_ = 'pack_a\\entity\\armor_stand.entity.json'
        entry1.delete("0", "end")
        entry1.insert("0", _text_)
        entry1.grid(column=0, padx=4, pady=4, row=0, sticky="w")
        entry2 = ttk.Entry(frame1)
        self.entry_b = tk.StringVar(
            value='pack_b\\entity\\armor_stand.entity.json')
        entry2.configure(textvariable=self.entry_b, width=40)
        _text_ = 'pack_b\\entity\\armor_stand.entity.json'
        entry2.delete("0", "end")
        entry2.insert("0", _text_)
        entry2.grid(column=0, padx=4, pady=4, row=1, sticky="w")
        button1 = ttk.Button(frame1)
        button1.configure(text='Pack-A')
        button1.grid(column=1, padx=4, pady=4, row=0, sticky="e")
        button1.configure(command=self.pack_a_button)
        button2 = ttk.Button(frame1)
        button2.configure(text='Pack-B')
        button2.grid(column=1, padx=4, pady=4, row=1, sticky="e")
        button2.configure(command=self.pack_b_button)
        button3 = ttk.Button(frame1)
        button3.configure(text='Ok')
        button3.grid(column=1, padx=4, pady=4, row=2, sticky="e")
        button3.configure(command=self.ok_button)
        frame1.grid(column=0, padx=4, pady=4, row=0)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def pack_a_button(self):
        json_filename_a = pack_file_select()
        self.entry_a.set(json_filename_a)

    def pack_b_button(self):
        json_filename_b = pack_file_select()
        self.entry_b.set(json_filename_b)

    def ok_button(self):
        write_json_a(self.entry_a.get(), self.entry_b.get())
        write_json_ac(self.entry_a.get(), self.entry_b.get())
        write_json_i(self.entry_a.get(), self.entry_b.get())
        write_json_pa(self.entry_a.get(), self.entry_b.get())
        write_json_rc(self.entry_a.get(), self.entry_b.get())
        pack_create()
        tk.messagebox.showinfo("Completed", "The pack merger has completed")
        sys.exit()


if __name__ == "__main__":
    app = EntityPackCompatibilityV001App()
    app.run()
