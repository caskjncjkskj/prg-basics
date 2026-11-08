import math

circumference = float(input("Enter tree circumference in cm: "))
can_be_cut_down = circumference / math.pi >= 50
print(f"Tree can be cut down: {can_be_cut_down}")
