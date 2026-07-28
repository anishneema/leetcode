class Solution:
    def checkValidString(self, s: str) -> bool:
        
        star_stack = []
        left_stack = []

        for i in range(len(s)):

            char = s[i]

            if char == '(':
                left_stack.append(i)
            elif char == ')':
                
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            
            else:
                star_stack.append(i)
        
        while star_stack and left_stack:

            if star_stack[-1] < left_stack[-1]:
                return False
            
            star_stack.pop()
            left_stack.pop()
        
        return len(left_stack) == 0