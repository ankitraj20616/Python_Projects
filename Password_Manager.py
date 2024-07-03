from cryptography.fernet import Fernet
class passwordManager:
    def __init__(self, fer) -> None:
        self.fer = fer

    def view(self)->None:
        with open("Passwords.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.rstrip()
                user, password = data.split("|")
                print("User: "+user+", Password: "+fer.decrypt(password.encode()).decode())

    def add(self)->None :
        account = input("Enter account: ")
        pwd = input("Enter password for that account: ")
        with open("Passwords.txt", 'a') as file:
            file.write(account + "|" + fer.encrypt(pwd.encode()).decode()+"\n")
    

if __name__ == "__main__":
    def write_key():
        key = Fernet.generate_key()
        with open("key.key" ,'wb') as key_file:
            key_file.write(key)

    def load_key():
        file = open("key.key", 'rb')
        key = file.read()
        file.close()
        return key

    master_password = input("Enter the master password to open Password Manager: ")
    # write_key() 
    # This will run once only to encode and set the master password , once we set the master password 
    # then from 2nd times execution use that master password and store , view, etc about your file
    # if you want to reset master password then reset the key.key anf Passwords.txt and starting executing with write_key() first and follow the upper steps
    key = load_key() + master_password.encode()
    fer = Fernet(key)

    manager = passwordManager(fer)

    while True:
        mode = input("Enter mode:-view for view mode, add for adding a new password, q for quit: ").lower()
        if mode == 'q':
            print("Exiting from password manager.")
            break

        if mode == "view":
            manager.view()
        elif mode == "add":
            manager.add()
        else:
            print("Invalid option, try again!")
            continue
