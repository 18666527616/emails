import person_pb2

# 创建一个 Person 对象
person = person_pb2.Person()
person.name = "John"
person.age = 30
person.address = "1234 Elm Street"

# 将 Person 对象序列化为二进制数据
person_data = person.SerializeToString()

# 将二进制数据写入文件
with open("person.bin", "wb") as f:
    f.write(person_data)

# 从文件中读取二进制数据
with open("person.bin", "rb") as f:
    person_data = f.read()

# 将二进制数据反序列化为 Person 对象
person = person_pb2.Person()
person.ParseFromString(person_data)

# 输出读取到的数据
print("Name:", person.name)
print("Age:", person.age)
print("Address:", person.address)
