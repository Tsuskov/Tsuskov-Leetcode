class Solution:
    def __init__(self):
        self.towers = [[], [], []] # A, B, C

    def moveDisk(self, source, target): # source, target: 0, 1, 2
        disk = self.towers[source].pop() # pop from source
        self.towers[target].append(disk) # append to target
        self.printTowers() # print towers

    def printTowers(self):
        print('A:', ' '.join(str(d) for d in self.towers[0])) # print towers
        print('B:', ' '.join(str(d) for d in self.towers[1]))  # print towers
        print('C:', ' '.join(str(d) for d in self.towers[2])) # print towers
        print('---')

    def towerHanoi(self, n, source, target, auxiliary): # n: number of disks, source, target, auxiliary: 0, 1, 2
        self.towers[source] = list(range(n, 0, -1)) # source: 1 to n
        self.printTowers() # print towers
        self._towerHanoi(n, source, target, auxiliary) # call recursive function

    def _towerHanoi(self, n, source, target, auxiliary): # n: number of disks, source, target, auxiliary: 0, 1, 2
        if n == 1: # base case
            self.moveDisk(source, target) # move disk from source to target
        else: # recursive case
            self._towerHanoi(n-1, source, auxiliary, target) # move n-1 disks from source to auxiliary
            self.moveDisk(source, target) # move disk from source to target
            self._towerHanoi(n-1, auxiliary, target, source) # move n-1 disks from auxiliary to target

x = Solution()
x.towerHanoi(3, 0, 2, 1)