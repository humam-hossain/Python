def every_test(n):
    result = 0
    fabrics = list()

    for fabric in range(n):
        str = input().split(" ")

        color = str[0]
        durability = int(str[1])
        id = int(str[2])

        fabric = {
            "id": id,
            "durability": durability,
            "color": color
        }

        fabrics.append(fabric)
    print(fabrics)
    
    print(sorted(fabrics, key=lambda d: d["durability"]))

    return result


t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    result = every_test(n)
    print(f'Case #{test_case}: {result}')
