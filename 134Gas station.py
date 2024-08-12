from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)  # number of stations
        total_tank = 0 # total tank
        curr_tank = 0 # current tank
        starting_station = 0 # starting station 
        for i in range(n): # loop through all stations
            total_tank += gas[i] - cost[i] # add gas and subtract cost
            curr_tank += gas[i] - cost[i] # add gas and subtract cost
            if curr_tank < 0: # if current tank is less than 0
                starting_station = i + 1 # set starting station to i + 1
                curr_tank = 0 # set current tank to 0
        return starting_station if total_tank >= 0 else -1 # return starting station if total tank is greater than or equal to 0 else return -1