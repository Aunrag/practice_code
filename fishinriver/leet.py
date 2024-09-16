
 '''   def find_subarray_powers(nums, k):
        n = len(nums)
        results = []
        
        # Iterate over all possible subarrays of size k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            
            # Check if subarray is consecutive and sorted
            min_val = min(subarray)
            max_val = max(subarray)
            
            if max_val - min_val == k - 1 and len(set(subarray)) == k:
                results.append(max_val)
            else:
                results.append(-1)

        
        return results

    
    

import array as arr
a=arr.array('i',[])
a=(1,2,3,4,3,2,5)
b=3
print(find_subarray_powers(a,b))

def subarray_powers(nums, k):
    n = len(nums)
    results = []

    for i in range(n - k + 1):
        subarray = nums[i:i + k]
        min_val = min(subarray)
        max_val = max(subarray)
        
        if max_val - min_val == k - 1 and len(set(subarray)) == k:
            results.append(max_val)
        else:
            results.append(-1)
    
    return results

a = (1, 2, 3, 4, 3, 2, 5)
b = 3
print(subarray_powers(a, b))

def ugly(n):
    if n <= 0:
        raise ValueError("The value of n must be positive.")
    if n == 1:
        return 1
    u=[]
    i=0
    while (len(u)<n):
         if(i%2==0) or (i%3==0) or (i%5==0):
             if i not in u:
                 u.append(i)
            
         i=i+1

    return u[n-1]

no = ugly(10)
print(no)
t=ugly(1)
print(t)

def ugly(n):
    if n <= 0:
        raise ValueError("The value of n must be positive.")
    if n == 1:
        return 1
    u=[]
    i=0
    while (len(u)<n):
        if(i%2==0) or (i%3==0) or (i%5==0):
            if i not in u:
                u.append(i)
            
        i=+1         
    return u[n-1]

no1 = ugly(10)
print(no1)
no2= ugly(1)
print(no2)'''
def count_substrings(s: str, k: int) -> int:
    n = len(s)
    result = 0
    
    # Function to count substrings with at most `max_count` number of specific character
    def count_valid_substrings(max_count: int) -> int:
        count = 0
        start = 0
        zero_count = 0
        one_count = 0
        
        for end in range(n):
            if s[end] == '0':
                zero_count += 1
            else:
                one_count += 1
            
            while zero_count > max_count and one_count > max_count:
                if s[start] == '0':
                    zero_count -= 1
                else:
                    one_count -= 1
                start += 1
            
            count += (end - start + 1)
        
        return count
    
    # Count substrings with at most k zeros
    valid_with_k_zeros = count_valid_substrings(k)
    # Count substrings with at most k ones
    valid_with_k_ones = count_valid_substrings(k)
    
    # Subtract the substrings that satisfy both constraints
    # Since the entire string is counted twice (once as '0' and once as '1')
    # We need to exclude the overlapping count
    total_substrings = valid_with_k_zeros + valid_with_k_ones - n * (n + 1) // 2
    
    return total_substrings

# Example usage
print(count_substrings("10101", 1))  # Output: 12
print(count_substrings("1010101", 2))  # Output: 25
print(count_substrings("11111", 1))  # Output: 15
