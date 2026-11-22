
import time
from collections import defaultdict, deque
from config import RATE_LIMIT, RATE_WINDOW

requests = defaultdict(deque)


def allowed(number):
    now = time.time()
    queue = requests[number]

    while queue and now - queue[0] >= RATE_WINDOW:
        queue.popleft()

    if len(queue) >= RATE_LIMIT:
        return False

    queue.append(now)
    return True


def remaining(number):
    now = time.time()
    queue = requests[number]

    while queue and now - queue[0] >= RATE_WINDOW:
        queue.popleft()

    return max(0, RATE_LIMIT - len(queue))
