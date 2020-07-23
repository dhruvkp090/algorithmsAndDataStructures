# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
worker = namedtuple("worker", ["workerID", "freeTime"])

def leftChild(a):
    return (2*(a+1) - 1)

def rightChild(a):
    return (2*(a+1))

def shiftDown(data, a):
    size = len(data)
    minInd = a
    L = leftChild(a)
    if L < size and data[L].freeTime < data[minInd].freeTime:
        minInd = L
    elif L < size and data[L].workerID < data[minInd].workerID:
        if data[L].freeTime == data[minInd].freeTime:
            minInd = L
    R = rightChild(a)
    if R < size and data[R].freeTime < data[minInd].freeTime:
        minInd = R
    elif R < size and data[R].workerID < data[minInd].workerID:
        if data[R].freeTime == data[minInd].freeTime:
            minInd = R
    if a != minInd:
        temp = data[a]
        data[a] = data[minInd]
        data[minInd] = temp
        shiftDown(data, minInd)
    return data


# def build_heap(data):
#     """Build a heap from ``data`` inplace.

#     Returns a sequence of swaps performed by the algorithm.
#     """
#     size = len(data)
#     for i in range(size//2, -1,-1):
#         shiftDown(data, i)
#     return data


def assign_jobs(n_workers, jobs):
    result = []
    allWorkers = [worker(i, 0) for i in range(n_workers)]
    # allWorksrs = build_heap(allWorkers)
    for j in jobs:
        result.append(AssignedJob(allWorkers[0].workerID, allWorkers[0].freeTime))
        allWorkers[0] = worker(allWorkers[0].workerID, allWorkers[0].freeTime + j)
        allWorkers = shiftDown(allWorkers, 0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
