import json
import json5

# function to add to JSON
def write_json_a(filename_a, filename_b):
    # First we load existing data into a dict.
    with open(filename_a, 'r+') as file_a, open(filename_b, 'r+') as file_b:
        file_data_a = json5.load(file_a)
        file_data_b = json5.load(file_b)
    level_a = file_data_a.get("minecraft:client_entity", []).get("description", []).get("scripts")
    level_b = file_data_b.get("minecraft:client_entity", []).get("description", []).get("scripts")
    key = "animate"
    # create object if not exist
    if key in level_a:
        if key not in level_b:
            level_b[key] = []
            for item_a in level_a[key]:
                split_a = (item_a,)
                level_b[key].extend(split_a)
        else:
            #compare files a and b
            for item_a in level_a[key]:
                if item_a not in level_b[key]:
                    split_a = (item_a,)
                    level_b[key].extend(split_a)
            for item_b in level_b[key]:
                if item_b not in level_a[key]:
                    split_b = (item_b,)
                    level_a[key].extend(split_b)
    else:
        if key in level_b:
            level_a[key] = []
            for item_b in level_b[key]:
                split_b = (item_b,)
                level_a[key].extend(split_b)
    #convert back to json
    with open(filename_a, 'w') as file_a, open(filename_b, 'w') as file_b:
        json.dump(file_data_a, file_a, indent = 4)
        json.dump(file_data_b, file_b, indent = 4)