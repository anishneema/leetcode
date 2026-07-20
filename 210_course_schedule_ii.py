class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ans = []

        prereq = {i:[] for i in range(numCourses)}
        for courses, pre in prerequisites:
            prereq[courses].append(pre)

        visited = set()
        done = set()
        def dfs(course):

            if course in visited:
                return False
            
            
            if course in done:
                
                return True
            
            visited.add(course)
            
            for prereqs in prereq[course]:

                if not dfs(prereqs):
                    return False
            
            ans.append(course)
            visited.remove(course)
            done.add(course)
            return True
        
        for i in range(numCourses):

            if not dfs(i):
                return []
        
        return ans