class sol():
    def length(self,s: str)-> int:
        n=len(s)
        left=0
        maximumLength= 0
        charset=set()
        for right in range(n):
            while(s[right]in charset):
                charset.remove((s[left]))
                left+=1
            charset.add(s[right])
            maximumLength=max(maximumLength,right-left+1)
        print("longest non repeated substring is : ",s[left:left+maximumLength])
        return maximumLength

S=str(input("enter the string: "))    
s=sol()
print("length of sub string: ",s.length(S))