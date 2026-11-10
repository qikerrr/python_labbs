class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_from_list(values):
    head = None

    for i in reversed(values):
        head = Node(i, head)

    return head

def ll_to_list(head):
    res = []

    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    return res

def ll_length(head):
    n = 0
    cur = head

    while cur is not None:
        n += 1
        cur = cur.next

    return n

def ll_prepend(head, value):
    return Node(value, head)

def ll_append(head, value):
    new_node = Node(value)

    if head is None:
        return new_node
    cur = head

    while cur.next is not None:
        cur = cur.next

    cur.next = new_node
    return head

def ll_insert(head, idx, value):

    if idx < 0:
        raise IndexError("idx < 0")
    if idx == 0:
        return Node(value, head)

    cur = head
    for i in range(idx - 1):
        if cur is None:
            raise IndexError("Недопустимый индекс!")
        cur = cur.next

    if cur is None:
        raise IndexError("Недопустимый индекс!")

    cur.next = Node(value, cur.next)
    return head

def ll_remove(head, value):

    if head is None:
        raise ValueError("Список пуст!")
    
    if head.value == value:
        return head.next

    cur = head
    while cur.next is not None:
        if cur.next.value == value:
            cur.next = cur.next.next
            return head

        cur = cur.next

    raise ValueError(f"Значение {value} не найдено")
        
def ll_reverse(head):

    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def ll_repr(head):

    parts = []
    cur = head
    while cur is not None:
        parts.append(f'[{cur.value}]')
        cur = cur.next

    return " -> ".join(parts) + " -> None" if parts else "None"


