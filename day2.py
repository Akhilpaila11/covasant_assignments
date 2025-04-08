import os
directory_path = r"C:\Users\Akhil\Desktop\python"
max_file_size = 0
max_file_name = ""
for file in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file)
    print( os.listdir(directory_path))
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        if file_size > max_file_size:
            max_file_size = file_size
            max_file_name = file

print(f"The largest file is: {max_file_name}")
print(f"Size: {max_file_size} bytes")