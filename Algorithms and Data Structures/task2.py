# the time complexity is O(n^2) 
# the space complexity is O(n) since we have to maintain a dictionary with maximum n entries
# n is the string length

def len_longest_substring_no_repeats(string):
    ans = 0
    n = len(string)

    # i is starting index of the substring analyzed
    for i in range(n):                              # O(n) loop
        length = 0
        visited = {}

        # j is the ending index of the substring analyzed
        for j in range(i, n):                           # O(n) nested loop
            visited.setdefault(string[j], False)        # all the operations below have constant time complexity O(1)

            # when a repetition is met, we shift i to the right, and begin growing substrings again
            if(visited[string[j]]):
                ans = max(ans, length)
                break

            # if the symbol added to the right is yet new, then mark it as visited and increment the substring length
            visited[string[j]] = True
            length += 1
    
    return ans
