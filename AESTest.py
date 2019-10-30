from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# print(key)

# file = open('key.key','wb')
# file.write(key)
# file.close()

file = open('key.key','rb')
key = file.read()
# print(key)
file.close()


input_file = 'test.properties'
output_file = 'test.encrypted'

# with open(input_file,'rb') as f:
#     data = f.read()
#
# fernet = Fernet(key)
# encrypted_data = fernet.encrypt(data)
#
# with open(output_file,'wb') as out:
#     out.write(encrypted_data)

fernet = Fernet(key)

with open(output_file,'rb') as f:
    data = f.read()

decrypt_data = fernet.decrypt(data)


list_data = decrypt_data.decode("utf-8").split("\n")
print(type(list_data))

token_keys = {}

for x in list_data:
    keu_token = x.split(":")
    print(keu_token)
    token_keys[keu_token[0]]=keu_token[1]

print(token_keys.get("map_key"))