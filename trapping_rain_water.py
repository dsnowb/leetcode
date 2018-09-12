class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        
        water = 0
        def add_water(height):
            nonlocal water
            if len(height) < 3:
                return
            
            maxl = 0
            maxr = 1
            for i in range(2, len(height)):
                if height[i] > height[maxr]:
                    if height[maxr] > height[maxl]:
                        maxl = maxr
                    maxr = i
                    
            if maxl > maxr:
                maxl, maxr = maxr, maxl

            less = height[maxl] if height[maxl] < height[maxr] else height[maxr]
                
            for i in range(maxl + 1, maxr):
                water += less - height[i]
            
            add_water(height[:maxl + 1])
            add_water(height[maxr:])
            
        add_water(height)
        return water
