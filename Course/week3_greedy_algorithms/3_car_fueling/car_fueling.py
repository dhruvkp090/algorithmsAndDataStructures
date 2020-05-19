# python3
import sys


def compute_min_refills(distance, tank, stops):
    refills = 0
    lastStop = 0
    lsIndex = 0
    if tank > distance: # Distance is less than the tank six=ze
        return refills
    elif (stops[-1] + tank) < distance: # If the last stop and the tank size is far away from the destination
        return -1
    else:
        while (lastStop + tank) < distance:
            chunk = [x for x in stops[lsIndex:] if x <= (tank + lastStop)]
            if lastStop != max(chunk):
                refills += 1
                lastStop = max(chunk)
                lsIndex = stops.index(lastStop)
            else:
                refills = -1
                break
        return refills




if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
