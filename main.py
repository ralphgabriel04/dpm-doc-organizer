import os 

# Define the path to the file
path = input("Enter the path where you want to create the folder: ")

 # Get the number of folder and the base name of the file
num_folder = int(input("Enter the number of folders you want to create: "))
base_name = input("Enter the name of the folder: ")

# Create the folder
for i in range(num_folder):
    folder_name = f"{base_name}_{i}"
    full_path = os.path.join(path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"Folder {folder_name}{i+1} created successfully!")
    
print("All folders created successfully!")