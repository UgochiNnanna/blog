computer_database = {
    "username": ["Ugochi", "Chioma", "Joel"],
    "password": "asdf",
    "storage": "150gb, 120gb, 80gb",
    "color": "white, black",
    "files": "barbie.mp3, picture.img, videos.mp4"
}

username = input("Your username: ")
password = input("Your Password: ")

if password == computer_database["password"]:
    print("Login Successful.")
    file_name = input("File name: ")
    length_of_file = len(file_name)
    print(f"[file_name] has successfully been uploaded .")

elif password != computer_database["password"]:
    print("Password incorrect, please try again.")

else:
    print("Please fill in the fields correctly.")