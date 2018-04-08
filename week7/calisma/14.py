import os


def dump_files(root_directory, search):
    files = os.listdir(root_directory)
    for f in files:
        full_path = os.path.join(root_directory, f)
        if (os.path.isdir(full_path)):
            dump_files(full_path, search)
        else:
            line = search_file(full_path, search)
            if (line != None):
                print(full_path)
                print(line)


def search_file(file, text):
    try:
        h = open(file)
        for line in h:
            if (line.find(text) > -1):
                return line
    except:
        pass
    return None


if __name__ == "__main__":
    dump_files("/home/pamir/dev/projects/pyhton", "password")
