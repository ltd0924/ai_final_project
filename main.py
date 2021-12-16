import io
import multiprocessing
import time

from galogic import *
import matplotlib.pyplot as plt
import progressbar

data=[]
with open('mtsp150.txt','r',encoding='utf8') as f:
    line=f.readline().split()
    while line:
        line=f.readline().split()
        data.append(line)


def mtsp():
    for i in range(numNodes):
        RouteManager.addDustbin(Dustbin(int(data[i][1]),int(data[i][2])))

    random.seed(seedValue)
    yaxis = []  # Fittest value (distance)
    xaxis = []  # Generation count

    pop = Population(populationSize, True)
    globalRoute = pop.getFittest()
    print('Initial minimum distance: ' + str(globalRoute.getDistance()))
    pbar = progressbar.ProgressBar()
    # Start evolving
    for i in pbar(range(numGenerations)):
        pop = GA.evolvePopulation(pop)
        localRoute = pop.getFittest()
        if globalRoute.getDistance() > localRoute.getDistance():
            globalRoute = localRoute
        yaxis.append(localRoute.getDistance())
        xaxis.append(i)

    print('Global minimum distance: ' + str(globalRoute.getDistance()))
    print('Final Route: ' + globalRoute.toString())
    return globalRoute.getDistance()
'''
fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.show()
'''

if __name__ == '__main__':
    dis = 0
    num = 30
    result = []
    t1 = time.time()
    pool = multiprocessing.Pool(5)  # 两个进程执行
    # pool = multiprocessing.Pool(multiprocessing.cpu_count()) # 全部cpu执行
    for i in range(num):
        result.append(pool.apply_async(func=mtsp))
    pool.close()
    pool.join()
    t2 = time.time()
    for i in range(len(result)):
       dis=dis+float(result[i].get())

    print('Average distance: '+str(dis/len(result)))
    print('time cost:'+str(t2-t1))

'''fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.show()
'''