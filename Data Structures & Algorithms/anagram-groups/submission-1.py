class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mydict = {}

        for string in strs:
            arr = [0]*26
            for char in string:
                idx = ord(char)-97
                arr[idx]+=1
            
            arr = tuple(arr)
            if arr not in mydict:
                mydict[arr] = [string]
            else:
                mydict[arr].append(string)
        res = []
        for key, values in mydict.items():
            res.append(values)
        
        return res
