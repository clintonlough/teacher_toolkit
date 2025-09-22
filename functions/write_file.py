import os

def write_file(filename, content):

    full_path = "lesson_plans"
    file_path = os.path.join(full_path,filename)
    abs_path = os.path.abspath(file_path)
    print(abs_path)

    # Create the directory if it doesn't exist
    os.makedirs(full_path, exist_ok=True)
    
    with open(abs_path, 'w') as f:
        f.write(content)
        print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    

if __name__ == "__main__": 
    write_file()