pathToFile = input("Path to file: ")

credentials = {}

with open(pathToFile) as openFile:
  lines = openFile.readlines()
  for line in lines:
    singleCredential = line.split(",")
    credentials[singleCredential[0].strip()] = singleCredential[1].strip()

print("Login ? y/n", end=" ")
answer = input("")
if (answer.lower() == "y"):
  print("Enter email: ", end=" ")
  email = input("")
  print("Enter password: ", end=" ")
  password = input("")

  if email in credentials.keys():
    if password in credentials.values():
      print("Access Granted\n")
    else:
      print("Invalid credentials")
  else:
    print("Invalid credentials")

# Path to file: ./credentials.txt
# Login ? y/n y
# Enter email:  brian@gmail.com
# Enter password:  brian321
# Access Granted