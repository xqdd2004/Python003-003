
import threading
import time
import random

fork_0 = threading.Lock()
fork_1 = threading.Lock()
fork_2 = threading.Lock()
fork_3 = threading.Lock()
fork_4 = threading.Lock()
'''
    实现思路：

    每位哲学家，要能同时拿到左边和右边的叉子才能吃饭
    把五把叉子都上锁，先到先得，如果不能同时拿到两把叉子，就把拿到的叉子放回去
    
    数据描述：
    output[i] = [a, b, c] (3 个整数)
    a 哲学家编号。
    b 指定叉子：{1 : 左边, 2 : 右边, 0：吃面时}.
    c 指定行为：{1 : 拿起, 2 : 放下, 3 : 吃面, 4：思考}。
    如 [4,2,1] 表示 4 号哲学家拿起了右边的叉子。所有自列表组合起来，就完整描述了“当每个哲学家分别需要进食 n 次”时这五位哲学家具体的行为记录。   

'''
eating_log= []

def wantstoeat(name, eat_num, left_fork, right_fork):
    print(f'哲学家{name} 开始工作')
    thinking(name)
    while eat_num > 0:
        pickLeftFork = left_fork.acquire(timeout=1)
        print(f'哲学家{name} 抢到左边叉子的结果：{pickLeftFork}')
        if pickLeftFork :
            #拿起左边的叉子
            eating_log.append([name, 1, 1])    
        pickRightFork = right_fork.acquire(timeout=1)
        print(f'哲学家{name} 抢到右边叉子的结果：{pickRightFork}')
        if pickRightFork :
            #拿起右边的叉子
            eating_log.append([name, 2, 1])  

        if pickLeftFork==True and pickRightFork==True: 
            eating(name) 
            eat_num -= 1 
            print(f'哲学家{name} 今天还可以吃饭{eat_num}次')
        else:
            print(f'哲学家{name} 没抢上吃饭, 今天还可以吃饭{eat_num}次,下次努力')
       
        if pickLeftFork :
            eating_log.append([name, 1, 2])
            left_fork.release()
        if pickRightFork:
            right_fork.release()
            eating_log.append([name, 2, 2]) 
        
        if eat_num==0:
            break;
        thinking( name )

#吃饭，随机吃饭10秒以内
def eating(name):
    print(f'哲学家{name} 开始吃饭')
    time.sleep(random.randint(2,10))
    eating_log.append([name, 0, 3])  
    print(f'哲学家{name} 吃饭完毕,请继续思考')  

#思考，随机休息10秒以内
def thinking(name):
    print(f'哲学家{name} 开始思考')
    time.sleep( random.randint(1,10))
    eating_log.append([name, 0, 4])  
    print(f'哲学家{name} 思考完毕，准备吃饭')

if __name__ == "__main__":
    t0 = threading.Thread(target=wantstoeat, args=(0,5,fork_0, fork_1))
    t1 = threading.Thread(target=wantstoeat, args=(1,5,fork_1, fork_2))
    t2 = threading.Thread(target=wantstoeat, args=(2,5,fork_2, fork_3))
    t3 = threading.Thread(target=wantstoeat, args=(3,5,fork_3, fork_4))
    t4 = threading.Thread(target=wantstoeat, args=(4,5,fork_4, fork_0))

    # t0 = DiningPhilosophers(0, 5, fork_0, fork_1)
    # t1 = DiningPhilosophers(1, 2, fork_1, fork_2)
    # t2 = DiningPhilosophers(2, 5, fork_2, fork_3)
    # t3 = DiningPhilosophers(3, 5, fork_3, fork_4)
    # t4 = DiningPhilosophers(4, 2, fork_4, fork_0)

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print('\n哲学家们吃饭行为记录:\n')
    print(eating_log)


