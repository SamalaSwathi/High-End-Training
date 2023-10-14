#Leetcode:804
"""Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
"""


def uniqueMorseRepresentations(self, words: List[str]) -> int:
    a='abcdefghijklmnopqrstuvwxyz'
    m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    d={}
    for  i in range(len(a)):
        d[a[i]]=m[i]
    l=[]
    for i in words:
        s=''
        for j in i:
            s+=d[j]
        l.append(s)
    return len(set(l))
n=list(map(int,input().split()))
