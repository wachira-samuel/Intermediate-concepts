from multiprocessing import Process, Value, Array, Lock
from time import sleep


def add_100(numbers=Value, lock=None, number=None):
    for i in range(100):
        sleep(0.01)
        for i in range(len(numbers)):
                numbers[i] += 1
        # lock. release()


if __name__ == "__main__":
    lock = Lock()
    shared_array = Array("d", [0.0, 100.0, 200.0])
    print('Number at the beginning is:', shared_array[:])
    p1 = Process(target=add_100, args=(shared_array,))
    p2 = Process(target=add_100, args=(shared_array,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("The number at the end is", shared_array)
