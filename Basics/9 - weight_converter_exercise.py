from tkinter import Widget
from traceback import print_tb


weight = float(input("Weight: "))
metric = input("(K)g or (L)bs: ")

if metric.lower() == "k":
    converted = weight*2.2046
    print(f"Weight in Lbs: {converted}")
elif metric.lower() == "l":
    converted = weight/2.2046
    print(f"Weigth in Kg: {converted}")
else:
    print("Wrong metric sign!")
