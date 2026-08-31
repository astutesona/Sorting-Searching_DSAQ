class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        
      
        base = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
        
       
        
        window = 0
        max_extra = 0
        
        for i in range(len(customers)):
            
          
            if grumpy[i] == 1:
                window += customers[i]
            
          
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    window -= customers[i - minutes]
            
            max_extra = max(max_extra, window)
        
        return base + max_extra
