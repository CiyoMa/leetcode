"""
Given two words (start and end), and a dictionary, find all shortest 
transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def nextWords(word, visitedWords, alphabeta, goal, nextLevel, pathMaps, frontier):
            #nextWords = set()
            size = len(word)
            #frontier = set()
            visitedWords.add(word)
            for i in range(size):
                prefix = word[:i]
                suffix = word[i+1:]
                ## Do store prefix suffix first and put it on the outloop!
                ## otherwise too many intermediate string will be created!!
                for char in alphabeta:
                    next = prefix + char + suffix
                    if next == goal:
                        temp = pathMaps.get(next,set())
                        temp.add(word)
                        pathMaps[next] = temp
                        return True
                    if next in dict and next not in visitedWords and next not in frontier:
                        temp = pathMaps.get(next,set())
                        temp.add(word)
                        pathMaps[next] = temp
                        #frontier.add(next)
                        #visitedWords.add(next)
                        nextLevel.add(next)
            #visitedWords |= frontier
                        # if word == 'tex':
                        #     print next,word
                        # else:
                        #     print next,word
            return False

        # @return a list of list of words from begin to current word on the
        #  shortest path
        def constructPath(word,pathMaps,begin): #,dp):
            if word == begin:
                return [[begin]]
            # if word in dp:
            #     return dp[word]#[:]

            result = []
            for w in pathMaps[word]:
                result += constructPath(w,pathMaps,begin)#,dp)[:]
            #print word,result#,len(result)
            for i in result:
                #print i
                i.append(word)
            #print word,result#,len(result)
            # if word not in dp:
            #     dp[word] = result
            return result

        visitedWords = set([start])
        frontier = set([start])
        k = 1
        alphabeta = 'abcdefghijklmnopqrstuvwxyz'
        pathMaps = {}
        flag = False
        while len(frontier) > 0 and not flag:
            k += 1
            #print k
            nextLevel = set()
            
            for word in frontier:
            #while len(frontier) > 0:
                #word = frontier.pop()
                next = nextWords(word, visitedWords, alphabeta, end, nextLevel, pathMaps, frontier)
                #print word, next
                if next:
                    #print k
                    flag = True
                #nextLevel |= next
                #visitedWords |= next #.add(word)
            if flag:
                break
            frontier = nextLevel

        if not flag:
            return []
        # dp = {}
        # for i in pathMaps.items():
        #     print i
        return constructPath(end, pathMaps, start)#, dp)
        # for i in pathMaps.items():
        #     print i
        #print pathMaps[end]
        # last = pathMaps[end][0]
        # print end,
        # while last != start:
        #     print last,
        #     last = pathMaps[last][0]
        # print start,
        # print 
        # return 0

import time
start = 'hit'
end = 'cog'
dic = ["hot","dot","dog","lot","log"]
start, end, dic = "red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]

#"qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
#"hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"]
#"nape", "mild", ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"]

s = Solution()
t1 = time.time()
#s.findLadders(start,end,dic)
print ( time.time() - t1 ) * 1000
print s.findLadders(start,end,dic)