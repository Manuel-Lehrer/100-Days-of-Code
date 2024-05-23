#FileNotFound
# try:
#     file = open("data.txt")
#     a_dic = {"key": "value"}
#     print(a_dic["key"])
# except FileNotFoundError:
#     file = open("data.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error i made up")



#KeyError
# a_dic= {"key": "value"}
# value = a_dic["non"]

# Index Error

# Type Error
# string + int for example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not exceed 3 meters")

bmi = weight / height ** 2
print(bmi)