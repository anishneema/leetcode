class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        prereq = {i:[] for i in range(numCourses)}

        for courses, prereqs in prerequisites:

            prereq[courses].append(prereqs)

        visited = set()
        
        def dfs(i):

            if i in visited:
                return False
            
            if prereq[i] == []:
                return True
            
            visited.add(i)
            
            for pre in prereq[i]:

                if not dfs(pre):

                    return False

            visited.remove(i)
            prereq[i] = []
            return True

        for i in range(numCourses):

            if not dfs(i):
                return False
        
        return True