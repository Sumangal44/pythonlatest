def compound(amount, rate, time):
    """Calculate compound interest."""
    for _ in range(time):
        amount += amount * rate
    return amount

compound(amount=1000, rate=0.05, time=10)

def main():
    print("Hello from pythonlatest!")
    amoount:float = float(input("Enter the principal amount: "))
    rate:float = float(input("Enter the rate of interest: ")) / 100
    time:int = int(input("Enter the time in years: "))
    