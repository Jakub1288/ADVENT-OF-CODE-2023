FILE_NAME="input07.txt"

def load_file(file_name):
    file=open(file_name, "r")
    return file.read()

if __name__=="__main__":
    lines=load_file(FILE_NAME)
    print (type(lines))