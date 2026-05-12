def infinite_chai():
    count = 1
    while True:
        yield f"Cup {count}"
        count += 1

refill = infinite_chai()


for _ in range(100):
    print(next(refill))

