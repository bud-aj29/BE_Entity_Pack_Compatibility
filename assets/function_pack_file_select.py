import os
import shutil 
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

# function to select pack, extract pack, then select entity file
def pack_file_select():
    messagebox.showinfo("Select Pack", "Select pack to extract")
    # specifying the name of the zip file
    in_filename = askopenfilename(initialdir=os.getcwd(), title='Select pack to extract', filetypes=[("rp files", ".zip .mcpack")])

    #name directories
    temp_dir_name = os.path.basename(os.path.splitext(in_filename)[0])
    temp_dir = os.path.join(os.getcwd(),'temp')
    temp_dir_pack = os.path.join(os.getcwd(),'temp', temp_dir_name)

    #make directories
    if not os.path.isdir(temp_dir):
        os.makedirs(temp_dir)
    if not os.path.isdir(temp_dir_pack):
        os.makedirs(temp_dir_pack)

    # extract zip file
    shutil.unpack_archive(in_filename, temp_dir_pack, 'zip')

    messagebox.showinfo("Select JSON", "Pack extracted to temp folder."+'\n'+"In extracted files, select entity json file to edit"+'\n'+"(eg. Vanilla_Resource_Pack\\entity\\armor_stand.entity.json)")
    #specify filename of json to load and add objects
    json_filename = askopenfilename(initialdir=temp_dir_pack, title='In extracted files, select entity json file to edit', filetypes=[("json files", ".json")])

    messagebox.showinfo("JSON Selected", "json selected")
    return (json_filename)
