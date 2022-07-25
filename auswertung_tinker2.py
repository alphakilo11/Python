with open("temp_log2.txt") as file:
    data = file.read()
cleanup_list = [" ", "["]
foo = data.replace(" ", "")
foo = foo.split("],")
print(foo[1])