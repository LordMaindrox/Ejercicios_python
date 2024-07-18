import time
incognita = 4564
start = time.time()
for i in range(100000000000000):

  if i == incognita:
    print(i)
    end = time.time()

    print(end-start)
