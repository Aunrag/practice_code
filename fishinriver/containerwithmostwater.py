'''class maxarea():
    def area(self):
        n=int(input("enter number of lines: "))
        import array as arr 
        a=arr.array('i',[])
        for i in range(0,n):
            c=int(input("enter the height: "))
            a.append(c)
        A=0  
        for i in range(0,n):
            s=a[i]
            for j in range(i+1,n):
                d=a[j]
                area=((j-i)*(min(s,d)))
                A=max(A,area)
                
        print(A) 
    
        
height=maxarea()
height.area()
'''
