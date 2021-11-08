import threading
import time


def task():
    time.sleep(5)

def main():
    #开始时间
    start_time = time.time()
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    thread1.start()
    thread2.start()
    #让其他线程等待自己执行完成
    thread1.join()
    thread2.join()
    #结束时间
    end_time = time.time()
    print(end_time - start_time)

if __name__ == "__main__":
    main()



'''
def task():
    print("扔第二个苹果")
    

def task2():
    print("扔第三个苹果")

def main():
    #threading.Thread 创建了一个线程
    thread1 = threading.Thread(target=task)
    #让线程执行
    thread1.start()
    thread2 = threading.Thread(target=task2)
    thread2.start()
    print("扔第一个苹果")

if __name__ == "__main__":
    main()
'''