from config import me

print(me)

# read
print(me["first"] + " " + me["last"])


# modify values
me["first"] = "Saul N."
print(me["first"])


# add new keys
me["preferred_color"] = "Blue"
print(me)


address = me["address"]
print(address["number"])
print(str(address["number"]) + " " + address["street"] + " " + address["city"])
