import os, csv, pickle


def load_user_dict(working_dir):
    # try to open the .pkl file with saved dictionary
    user_dict_filepath = os.path.join(working_dir, "user_dict.pkl")
    try:
        user_dict_file = open(user_dict_filepath, "rb")
    except FileNotFoundError:
        return {}

    # load the dictionary from .pkl file
    user_dict = pickle.load(user_dict_file)

    user_dict_file.close()
    return user_dict


def save_user_dict(working_dir, user_dict):
    # try to open the .pkl file with saved dictionary
    user_dict_filepath = os.path.join(working_dir, "user_dict.pkl")
    user_dict_file = open(user_dict_filepath, "wb")

    # save the dictionary to .pkl file
    pickle.dump(user_dict, user_dict_file)
    user_dict_file.close()


# argument workingDir is an address of directory containing src-data folder
# the script will create processed-data folder in workingDir if it doesn't exist
def match_users_to_images(working_dir) :

    csvFilenames = []
    pngFilenames = []

    # scanning the directory for .csv and .png files
    for root, dirs, files in os.walk(os.path.join(working_dir, "src-data")):
        for file in files:
            if file.endswith('.csv'):
                csvFilenames.append(file)
            elif file.endswith('.png'):
                pngFilenames.append(file)

    # loading the "user_dict" dictionary (DB prototype)
    # it maps the unique user string to user id
    # unique user string is a concatenation of "first_name", "last_name", and "birthts" strings
    user_dict = load_user_dict(working_dir)

    # set minimal id for potential new users
    # if this is the 1st program launch, set minimal id to 1
    if len(user_dict) > 0:
        id = max(user_dict.values()) + 1
    else:
        id = 1

    # organizing the output
    outputPath = os.path.join(working_dir, "processed-data", "output.csv")
    outputFile = open(outputPath, 'w+', newline='')

    fieldnames = ["user_id", "first_name", "last_name", "births", "img_path"]
    writer = csv.DictWriter(outputFile, fieldnames)
    writer.writeheader()

    # parsing the info from the .csv files
    for csvFilename in csvFilenames:
        csvPath = os.path.join(working_dir, "src-data", csvFilename)
        csvFile = open(csvPath, 'r')

        reader = csv.DictReader(csvFile)
        user_info = next(reader)
        
        # fixing some source data bugs
        user_info['last_name'] = user_info.pop(' last_name')
        user_info['births'] = user_info.pop(' birthts')

        # creating a user unique string
        user_unique_string = user_info['first_name'] + user_info['last_name'] + user_info['births']
        
        img_path = ""
        wanted_png_filename = os.path.splitext(csvFilename)[0]+'.png'
        if wanted_png_filename in pngFilenames:
            img_path = os.path.join(working_dir, "src-data", wanted_png_filename)

        # if the considered user is not in the DB yet, then add them and assing a new id to them
        if not user_unique_string in user_dict:
            user_dict[user_unique_string] = id
            id += 1

        writer.writerow({'user_id': user_dict[user_unique_string], **user_info, 'img_path' : img_path})

        csvFile.close()

    outputFile.close()

    save_user_dict(working_dir, user_dict)