# Krists Kristaps Dūda 10.grupa
# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread = [(0,1)for i in range(n)]
    heapq.heapify(thread)
    
    for i in range(m):
        time, index = heapq.heappop(thread)
        output.append((index,time))
        heapq.heappush(thread, (time+data[i], index))
        
        
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    
    n, m = map(int, input().split())
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []
    data = list(map(int, input().split()))
    
    assert 1<=n<=10**5
    assert 1<=m<=10**5
    assert len(data) == m
    assert all(0<=ti<=10**9 for ti in data)

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    
    for index, begin_time in result:
        print(index, begin_time)



if __name__ == "__main__":
    main()
