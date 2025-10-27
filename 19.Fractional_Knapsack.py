def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    # Calculate profit/weight ratio
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
    print("Profit/Weight Ratios (Profit/Weight, Weight, Profit):")
    for r in ratio:
        print(r)
    print()

    # Sort parcels by ratio in descending order
    ratio.sort(reverse=True, key=lambda x: x[0])
    print("Sorted Profit/Weight Ratios (Profit/Weight, Weight, Profit):")
    for r in ratio:
        print(r)
    print()

    max_profit = 0.0
    selected = []  # to store which items (or fractions) are chosen

    for r, w, p in ratio:
        if capacity == 0:
            break
        if w <= capacity:
            # Take full parcel
            max_profit += p
            capacity -= w
            selected.append((w, p, 1.0))  # full parcel taken
        else:
            # Take fractional parcel
            fraction = capacity / w
            max_profit += p * fraction
            selected.append((capacity, p * fraction, fraction))
            capacity = 0

    return max_profit, selected

# Main code to call Fractional Knapsack function
def main():
    weights = []
    profits = []
    n = int(input("Enter number of parcels: "))

    for i in range(n):
        wt = int(input(f"Enter Weight of parcel {i+1}: "))
        weights.append(wt)
        pf = int(input(f"Enter Profit of parcel {i+1}: "))
        profits.append(pf)
        print()

    capacity = int(input("Enter capacity of truck: "))

    max_profit, selection = fractional_knapsack(weights, profits, capacity)
    print("Selected parcels (Weight taken, Profit gained, Fraction taken):")
    for s in selection:
        print(s)

    print("\nMaximum Profit:", max_profit)

main()