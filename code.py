def fcfs(requests, head):
    seek = 0
    for r in requests:
        seek += abs(head - r)
        head = r
    return seek


def sstf(requests, head):
    seek = 0
    req = requests.copy()
    while req:
        nearest = min(req, key=lambda x: abs(x - head))
        seek += abs(head - nearest)
        head = nearest
        req.remove(nearest)
    return seek


def scan(requests, head, size):
    seek = 0
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])

    for r in right:
        seek += abs(head - r)
        head = r

    seek += abs(head - (size - 1))
    head = size - 1

    for r in left:
        seek += abs(head - r)
        head = r

    return seek


def cscan(requests, head, size):
    seek = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    for r in right:
        seek += abs(head - r)
        head = r

    seek += abs(head - (size - 1))
    head = 0
    seek += size - 1

    for r in left:
        seek += abs(head - r)
        head = r

    return seek


# Example Run
requests = list(map(int, input("Enter requests: ").split()))
head = int(input("Enter head position: "))
size = int(input("Enter disk size: "))

print("FCFS:", fcfs(requests, head))
print("SSTF:", sstf(requests, head))
print("SCAN:", scan(requests, head, size))
print("C-SCAN:", cscan(requests, head, size))
