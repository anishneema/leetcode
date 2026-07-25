class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        possible = []


        for x,y,z in triplets:

            if target[0] < x or target[1] < y or target[2] < z:
                continue
            
            possible.append([x,y,z])
        
        var1 = False
        var2 = False
        var3 = False

        for x, y, z in possible:

            if target[0] == x:
                var1 = True
            if target[1] == y:
                var2 = True
            if target[2] == z:
                var3 = True
        

        return var1 and var2 and var3