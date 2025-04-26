def recover_deleted_file(disk_image_path):
    with open(disk_image_path, "rb") as file:
        data = file.read()

    signature = b"DELETEDFILE"
    index = data.find(signature)
    if index != -1:
        recovered = data[index+len(signature):index+len(signature)+100]
        print(f"🔍 Recovered data: {recovered}")
    else:
        print("❌ No deleted file signature found.")

if __name__ == "__main__":
    path = input("Enter disk image path: ")
    recover_deleted_file(path)
