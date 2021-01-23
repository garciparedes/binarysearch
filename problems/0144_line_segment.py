class Solution:
    def solve(self, coordinates):
        if len(coordinates) < 2:
            return True

        slope = self.compute_slope(coordinates[1], coordinates[0])
        for i in range(2, len(coordinates)):
            if self.compute_slope(coordinates[i], coordinates[0]) != slope:
                return False;
          
        return True

    @staticmethod
    def compute_slope(a, b):
        if a[0] == b[0]:
            return float("inf")
        return (b[1] - a[1]) / (b[0] - a[0])
