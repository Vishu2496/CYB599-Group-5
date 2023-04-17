#!/usr/bin/env python
# coding: utf-8

# In[8]:


class OrderedSearchAlgorithm:
    def __init__(self, positions):
        
        # Initializing the problem with the list of positions
        self.positions = positions
    
    # Performing a binary search on the ordered list of positions and determines the index of the best position
    def get_best_position(self, target):
        nearest = 0
        farthest = len(self.positions) - 1

        # Intializing the binary search
        while nearest <= farthest: # while the nearest and farthest are not the same
            mid = (nearest + farthest) // 2 # find the middle
            if target == self.positions[mid]: # if the target is the middle
                return mid # return the middle
            elif target < self.positions[mid]: # if the target is less than the middle
                farthest = mid - 1 # set the farthest to the middle - 1
            else:
                nearest = mid + 1 # set the nearest to the middle + 1
        return nearest


def test_ordered_search():
    positions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
                 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    problem = OrderedSearchProblem(positions)

    assert problem.get_best_position(0) == 0
    assert problem.get_best_position(1) == 0
    assert problem.get_best_position(2) == 1
    assert problem.get_best_position(3) == 1
    assert problem.get_best_position(4) == 2
    assert problem.get_best_position(5) == 2
    assert problem.get_best_position(6) == 3
    assert problem.get_best_position(7) == 3
    assert problem.get_best_position(8) == 4
    assert problem.get_best_position(9) == 4
    assert problem.get_best_position(10) == 5
    assert problem.get_best_position(11) == 5
    assert problem.get_best_position(12) == 6
    assert problem.get_best_position(13) == 6
    assert problem.get_best_position(14) == 7
    assert problem.get_best_position(15) == 7
    assert problem.get_best_position(16) == 8
    assert problem.get_best_position(17) == 8
    assert problem.get_best_position(18) == 9
    assert problem.get_best_position(19) == 9
    assert problem.get_best_position(20) == 10
    assert problem.get_best_position(21) == 10
    assert problem.get_best_position(22) == 11
    assert problem.get_best_position(23) == 11
    assert problem.get_best_position(24) == 12
    assert problem.get_best_position(25) == 12

if __name__ == '__main__':

    positions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
                 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    
    problem = OrderedSearchAlgorithm(positions)
    print("The best position for 24 is: ", problem.get_best_position(24))
    print("The best position for 26 is: ", problem.get_best_position(26))
    print("The best position for 28 is: ", problem.get_best_position(28))
    print("The best position for 30 is: ", problem.get_best_position(30))
    print("The best position for 32 is: ", problem.get_best_position(32))
    print("The best position for 34 is: ", problem.get_best_position(34))


# In[ ]:




