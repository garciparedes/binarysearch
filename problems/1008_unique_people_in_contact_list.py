class Solution:
    def solve(self, contacts):
        seen = set()
        ans = 0
        for group in contacts:
            valid = True
            for email in group:
                if email in seen:
                    valid = False
                seen.add(email)
            
            if valid:
                ans += 1
        return ans       
