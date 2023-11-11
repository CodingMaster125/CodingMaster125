P = float(input("Enter the principal amount"))
R = float(input("Enter the annual interest (in percentage): "))
T = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times the interest is compounded per year: "))

simple_interest = (P*R*T)/100
compound_interest = P*((1 + R/(n*100))**(n*T))
print("\nBusiness Name: Yusuf and Sons")
print(f"Simple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")
