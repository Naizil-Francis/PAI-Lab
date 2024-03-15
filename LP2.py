import random

def nim_game():
    heap_size = 13  # Number of matchsticks in the heap
    current_player = "Max"
    while heap_size > 0:
        print(f"\nCurrent heap size: {heap_size}")
        if current_player == "Max":
            move = max_heap_move(heap_size)
        else:
            move = min_heap_move(heap_size)
        print(f"{current_player} takes {move} matchsticks.")
        heap_size -= move
        current_player = "Min" if current_player == "Max" else "Max"
    print(f"\n{current_player} wins!")

def max_heap_move(heap_size):
    first_bit = heap_size & 1
    heap_size_without_first_bit = heap_size >> 1
    result = heap_size_without_first_bit + first_bit
    return heap_size-result
  
def min_heap_move(heap_size):
    b=int(heap_size/2)
    if b>1:
        a= random.randint(1,b)
    else :
         a= 1
    return a

if __name__ == "__main__":
    nim_game()