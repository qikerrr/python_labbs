from collections import deque
from typing import Any

#Стек

def stack_push(st, item):
    st.append(item)

def stack_pop(st):
    if not st:
        raise IndexError("Стек пуст!")
    
    return st.pop()

def stack_peek(st):
    if not st:
        return None
    
    return st[-1]

def stack_is_empty(st):
    return len(st)==0

#Очередь

def queue_enqueue(q, item):
    q.append(item)

def queue_dequeue(q):
    if not q:
        raise IndexError("Очередь пустая!")

    return q.popleft()

def queue_peek(q):
    if not q:
        return None

    return q[0]

def queue_is_empty(q):
    return len(q)==0

#Задача на стек

def is_balanced(s):
    stack = []
    pairs = { ')':'(', ']':'[', '}':'{' }

    for ck in s:
        if ck in '([{':
            stack.append(ck)

        elif ck in ')]}':
            if not stack or stack.pop() != pairs[ck]:
                return False

    return len(stack) == 0