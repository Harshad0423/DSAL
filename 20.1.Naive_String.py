def NaiveStringMatching(text, pattern):
    n = len(text)
    m = len(pattern)
    found = False
    for i in range(n - m + 1):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            print(f"Pattern occurs with shift {i}")
            found = True
    if not found:
        print("Pattern not found.")

def main():
    t = input("Enter text: ")
    p = input("Enter pattern to search: ")
    NaiveStringMatching(t, p)

main()
