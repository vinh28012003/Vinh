#Dictionary (Object)

information = {
    # key: value
    "do_kho": ['snack', 'thit bo kho'],
    "dong_lanh": {
        "do_song": [],
        "do_gan_chin": [],
        "do_da_chin": "khong co do"
    },
    "is_open": True, # Accepted all tupe data with value
    "gia_dung": "chao ran"
}


# Create
# Read
# Update
# Delete

# Get value by key
#print(
    #dictionary.key
    #information["do_kho"]["do_song"])
#information["do_kho"]["do_song"].append("ca map")
information["dong_lanh"]["do_da_chin"] = "ca kho lang vu dai"
#print(information["dong_lanh"]["do_song"])

# Delete key from dictionary

del information["is_open"]

print(information)