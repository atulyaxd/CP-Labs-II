subjects = {1:'EM', 2:'EM-II', 3:'EP', 4:'IMCE', 5:'EC'}

key = int(input("Enter Key (int only): "))
if key in subjects:
    print(f"{key} exists.")
elif key not in subjects:
    print(f"{key} does not exists.")

