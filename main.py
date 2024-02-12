names=["Bora","Hasan","Kutay","Rand"]
print(names)
new_names= [x if x!= "Rand" else "Ramazan" for x in names]
print(new_names)
if len(new_names) < 5:
    new_names.append("Kemal")
    print(new_names)
new_names.sort()
print(new_names)