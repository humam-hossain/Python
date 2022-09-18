def get_ruler(kingdom):
    ruler = ''

    # ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    # 32–47 / 58–64 / 91–96 / 123–126

    if (ord(kingdom[-1]) >= 65 and ord(kingdom[-1]) <=90) or (ord(kingdom[-1]) >= 97 and ord(kingdom[-1]) <=122):
        if kingdom[-1] == 'y' or kingdom[-1] == 'Y':
            ruler = "nobody"
        elif kingdom[-1] == 'A' or kingdom[-1] == 'E' or kingdom[-1] == 'I' or kingdom[-1] == 'O' or kingdom[-1] == 'U' or kingdom[-1] == 'a' or kingdom[-1] == 'e' or kingdom[-1] == 'i' or kingdom[-1] == 'o' or kingdom[-1] == 'u':
            ruler = "Alice"
        else:
            ruler = 'Bob'
    return ruler

def main():
  # Get the number of test cases
    T = int(input())
    for t in range(T):
    # Get the kingdom
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
    main()
