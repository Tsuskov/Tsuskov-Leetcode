
class Solution:
    def maxPoints(self, points):
        if len(points) < 3: # if there are less than 3 points, then all points are on the same line
            return len(points)  # so return the number of points
        
        max_points = 0
        
        for i in range(len(points)): # for each point, calculate the slope with all other points
            slope_count = {} # dictionary to store the slope and the number of points with that slope
            same_points = 1 # number of points with the same coordinates as the current point
            
            for j in range(i+1, len(points)): # for each point after the current point
                x_diff = points[j][0] - points[i][0] # calculate the difference in x coordinates
                y_diff = points[j][1] - points[i][1] # calculate the difference in y coordinates
                
                if x_diff == 0 and y_diff == 0: # if the points are the same, increment same_points
                    same_points += 1
                    continue
                
                if x_diff == 0: # if the slope is infinity, set slope to infinity
                    slope = float('inf')
                else:
                    slope = y_diff / x_diff # calculate the slope
                
                if slope not in slope_count: # if the slope is not in the dictionary, add it
                    slope_count[slope] = 1 # and set the number of points with that slope to 1
                else:
                    slope_count[slope] += 1 # otherwise, increment the number of points with that slope
            
                if slope_count:
                 max_points = max(max_points, max(slope_count.values()) + same_points) # update the maximum number of points on a line
                else:
                 max_points = max(max_points, same_points) # update the maximum number of points on a line

        return max_points

x = Solution()
print(x.maxPoints([[1, 1], [2, 2], [3, 3]]))