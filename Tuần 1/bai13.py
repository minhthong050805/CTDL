def tim_ten(ds, ten):
    for i in range(len(ds)):
        if ds[i].lower() == ten.lower():
            return i
    return -1

ds = ["An", "Binh", "Chau"]
print(tim_ten(ds, "an"))
print(tim_ten(ds, "Duc"))
