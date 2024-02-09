# You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.
# Return all possible synonymous sentences sorted lexicographically.

# Example 1:
# Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
# Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]

# Example 2:
# Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
# Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
 
# Time: O(), Space: O(nm)
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        adj = defaultdict(list)
        for i, j in synonyms:
            adj[i].append(j)
            adj[j].append(i)
        print(adj)

        output = set()
        q = deque([text])
        while q:
            cur = q.popleft()
            output.add(cur)
            arr = cur.split()
            for i, c in enumerate(arr):
                if c in adj:
                    for j in adj[c]:
                        sentence = " ".join(arr[:i]+[j]+arr[i+1:])
                        if sentence not in output:
                            q.append(sentence)
        return sorted(output)
      

# More efficient      
# Time: O(), Space: O()   
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent= {}
        rank = {}

        def find(x):
            parent.setdefault(x,x) 
            while parent[x]!=x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x  

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx==ry:
                return
            rank.setdefault(rx,1)
            rank.setdefault(ry,1)     

            if rank[rx]>rank[ry]:
                parent[ry] = rx
                rank[rx] += rank[ry]
            else:
                parent[rx] = ry
                rank[ry] += rank[rx]

        for x,y in synonyms:
            union(x,y)            

        graph = defaultdict(list)    
        for k in parent:
            par = find(k)
            graph[par].append(k)

        for g in graph:
            graph[g].sort()

        def backtrack(i, path):
            if i==len(text):
                output.append(path)
                return 

            curr = text[i]
            if curr not in parent:
                backtrack(i+1, path+[curr])
            else:
                for j in graph[parent[curr]]:
                    backtrack(i+1, path+[j])    

        output = []
        text = text.split(" ")
        backtrack(0,[])

        return [" ".join(sentence) for sentence in output]     

