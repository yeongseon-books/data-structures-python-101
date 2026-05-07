from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: "Node | None" = None


def tiny_singly_linked_list(values: list[int]) -> Node | None:
    head: Node | None = None
    tail: Node | None = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def deque_rotation(values: list[int], steps: int) -> list[int]:
    dq = deque(values, maxlen=len(values) if values else None)
    dq.rotate(steps)
    return list(dq)


def sliding_window(values: list[int], window: int) -> list[int]:
    dq: deque[int] = deque(maxlen=window)
    sums: list[int] = []
    for v in values:
        dq.append(v)
        if len(dq) == window:
            sums.append(sum(dq))
    return sums


if __name__ == "__main__":
    head = tiny_singly_linked_list([1, 2, 3])
    print(head)
    print(deque_rotation([1, 2, 3, 4], 1))
    print(sliding_window([1, 2, 3, 4, 5], 3))
