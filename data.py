import sys, os

# assign directory
directory = sys.argv[1]
file_list = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f.endswith(".txt"):
            file_list.append(f)

for filename in file_list:
    with open (filename, "r", encoding="utf-8") as f:
        file = f.readlines()

    if file[0].startswith("==="):
        with open (filename, "w", encoding="utf-8") as f:
            f.writelines(file[1:])
