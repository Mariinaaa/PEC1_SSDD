import threading
counter = 0
def increment():
    global counter
    for _ in range(1000):
        counter += 1
        
threads = [threading.Thread(target=increment) for _ in range(10)]

for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

print("Counter:", counter)

