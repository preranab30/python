import threading
import time
def displayLetter(lst):
    print(f"Hello {threading.current_thread().name}!")
    for i in lst:
        print(i)
        time.sleep(1)

def display_digit(lst):
    print(f"hello {threading.current_thread().name}!")
    for i in lst:
        print(i)
        time.sleep(1)

lst1 = list(map(int, input().split(",")))
lst2 = list(input().split(","))
display_digit(lst1)
displayLetter(lst2)
t1 = threading.Thread(target= display_digit(lst1))
t2 = threading.Thread(target = displayLetter(lst2))
t1.daemon = True # set Daemon thread
t1.start()
t2.start()