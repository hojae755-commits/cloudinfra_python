mem1 = {"num": 21, "name":"이한", "isMan":True}
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

mem1["nums"] = 2
mem1["name"] = "이란"
mem1["isMan"] = False

del mem1["isMan"]
mem1.clear()