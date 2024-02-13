class Solution:    
    def doUnion(self,a,n,b,m):
        union_set = set()
    
        for i in a:
            union_set.add(i)
        for j in b:
            union_set.add(j)
        return len(union_set)            
                
