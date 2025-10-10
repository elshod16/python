import threading
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_primes(start, end, result_list):
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)

if name == "main":
    start_range = 1
    end_range = 100
    num_threads = 4
    primes = []
    threads = []
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        s = start_range + i * step
        e = start_range + (i+1) * step if i < num_threads - 1 else end_range
        t = threading.Thread(target=check_primes, args=(s, e, primes))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Topilgan prime sonlar:", sorted(primes))


  import threading
from collections import Counter

# Fayl bo‘lagini hisoblash funksiyasi
def process_lines(lines, counter_list):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter_list.append(local_counter)

if name == "main":
    filename = "big_text.txt"
    num_threads = 4
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    step = len(lines) // num_threads
    threads = []
    counters = []

    for i in range(num_threads):
        start = i * step
        end = (i+1) * step if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counters))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    final_counter = Counter()
    for c in counters:
        final_counter.update(c)
    print("So‘zlarning chastotasi:")
    for word, count in final_counter.most_common(10):
        print(f"{word}: {count}")
