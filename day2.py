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

Q-2
import os

def collect_text_files(directory, filter_pattern, output_file):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(filter_pattern):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read() + '\n')  
    with open(output_file, 'r') as outfile:
        combined_text = outfile.read()
    print(combined_text)  
    return f"Files merged into: {output_file}"

directory = r"C:\Users\Akhil\Desktop\python"
filter_pattern = ".txt"
output_file = "combined_output.txt"
print(output_file)
print(collect_text_files(directory, filter_pattern, output_file))
