class Solution:
    def lengthLongestPath(self, input: str) -> int:
        fileList = []
        currentName = ""
        currentLevel = 0
        i=0
        # 先把所有的file或者dir都从input string里parse出来
        # 存成一个list of tuples，每一个tuple代表一个file或者一个dir
        # tuple[0]是这个node的name，tuple[1]这个node的level即这个node的名字在input
        # string里前面有的tab的数量
        while i< len(input):
            if input[i]!="\n" and input[i]!="\t":
                while i<len(input) and input[i]!="\n":
                    currentName+=input[i]
                    i+=1
                fileList.append((currentName,currentLevel))
                currentName = ""
                currentLevel = 0
            if i<len(input):
                if input[i] == "\n":
                    i+=1
                else:
                    currentLevel+=1
                    i+=1
        # print(fileList)
        # 把一个在level 0的dir放到parseStack里
        # 把所有在level 0的dir放到levelZeroDir里
        # 如果整个input string了全是file没有dir的话，直接return最长的filename的长度
        longest = 0
        parseStack = []
        levelZeroDir =[]
        for node in fileList:
            if "." in node[0] and node[1]==0:
                longest = max(longest,len(node[0]))
            if "." not in node[0]:
                levelZeroDir.append((node[0],node[0]))
                if len(parseStack)==0:
                    parseStack.append(node)
        if len(parseStack)==0:
            return longest
        fileMap={parseStack[0][0]:[]}

        # 再parse fileList，形成一个map，map里每一个dir是一个key，key对应的value是
        # 一个list of 这个dir自己的subdir或者dir里直属的file的名字
        # example：如果input是"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        # fileList是[('dir', 0), ('subdir1', 1), ('subdir2', 1), ('file.ext', 2)]
        # fileMap是{'dir': ['subdir1', 'subdir2'], 'subdir1': [], 'subdir2': ['file.ext']}
        # 这个过程是用stack实现的，自己设计的还是比较精妙的，可以再细看一下
        for node in fileList[1:]:
            parentName, parentLevel = parseStack[-1]
            if node[1]==parentLevel+1:
                fileMap[parentName].append(node[0])
            else:
                while node[1]<parentLevel+1 and parseStack:
                    parseStack.pop()
                    if parseStack:
                        parentName, parentLevel = parseStack[-1]
                if parseStack:
                    fileMap[parentName].append(node[0])
            if "." not in node[0]:
                parseStack.append(node)
                fileMap[node[0]]=[]
        # print(fileMap)
        # 最后用一个DFS traverse整个file tree，找到最长的file的absolute path的length
        # 这个DFS的stack里存的是一个tuple, tuple[0]:name of the dir, tuple[1]:absolute path of dir
        #  只有dir才能进stack，file不能进，但是根据题目要求，只有file的path length才有竞争最长的资格
        stack = levelZeroDir[:]
        while stack:
            # 一个dir被从stack里pop出来的时候我们就知道它的path
            name,path = stack.pop()
            for node in fileMap[name]:
                # 过它的children时，直接把\和children的名字加到parent的path后面就可以了
                newPath = path+"\\"+node
                if "." not in node:
                    stack.append((node,newPath))
                else:
                    longest = max(longest,len(newPath))
        return longest