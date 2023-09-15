import os
import shutil

# function to create pack, then delete temp directory
def pack_create():
    temp_dir = os.path.join(os.getcwd(),'temp')
    temp_dir_list = next(os.walk(temp_dir))[1]
    temp_dir_name_a = temp_dir_list[0]
    temp_dir_name_b = temp_dir_list[1]
    temp_dir_out_a = os.path.join(temp_dir,temp_dir_name_a)
    temp_dir_out_b = os.path.join(temp_dir,temp_dir_name_b)

    #zip from temp directory
    shutil.make_archive(temp_dir_name_a, 'zip', temp_dir_out_a)
    shutil.make_archive(temp_dir_name_b, 'zip', temp_dir_out_b)

    #delete temp directory
    shutil.rmtree(temp_dir)

    #rename zip to mcpack
    os.rename(temp_dir_name_a+'.zip', temp_dir_name_a+'(EP_compatibility).mcpack')
    os.rename(temp_dir_name_b+'.zip', temp_dir_name_b+'(EP_compatibility).mcpack')
