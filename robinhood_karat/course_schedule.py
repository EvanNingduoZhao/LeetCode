# https://leetcode.com/playground/nrNVGm2X
def course_schedule(preq):
    preqToCourse = {}
    posInChain = {}
    for pair in preq:
        preqToCourse[pair[0]]=pair[1]
        if pair[0] not in posInChain:
            posInChain[pair[0]]=0
        if pair[1] not in posInChain:
            posInChain[pair[1]]=1
        posInChain[pair[1]]+=1
    path = []
    for course in posInChain.keys():
        if posInChain[course]==0:
            path.append(course)
            while course:
                if course in preqToCourse:
                    course = preqToCourse[course]
                    path.append(course)
                else:
                    course = None
        break
    print(path)
    print(len(path))
    if len(path)%2==0:
        return path[int(len(path)/2-1)]
    else:
        return path[int((len(path)-1)/2)]

preq = [["c1","c2"],["c3","c4"],["c2","c3"],["c4","c5"]]
print(course_schedule(preq))

def course_schedule_2(preq):
    preqToCourses = {}
    posInChain = {}
    for pair in preq:
        if pair[0] in preqToCourses:
            preqToCourses[pair[0]].append(pair[1])
        else:
            preqToCourses[pair[0]]=[pair[1]]
        if pair[0] not in posInChain:
            posInChain[pair[0]]=0
        if pair[1] not in posInChain:
            posInChain[pair[1]]=1
        posInChain[pair[1]]+=1
    midCourses = []
    for course in posInChain.keys():
        if posInChain[course]==0:
            print("start course is:",course)
            findMidCourse(preqToCourses,course,[],midCourses)
    return midCourses

def findMidCourse(preqToCourses, course, path, midCourses):
    path.append(course)
    if course not in preqToCourses.keys():
        print(path)
        print(len(path))
        # midCourse = None
        if len(path) % 2 == 0:
            midCourse = path[int(len(path) / 2 - 1)]
        else:
            midCourse = path[int((len(path) - 1) / 2)]
        if midCourse not in midCourses:
            midCourses.append(midCourse)
        return
    for nextCourse in preqToCourses[course]:
        pathCopy =  path[:]
        findMidCourse(preqToCourses,nextCourse,pathCopy,midCourses)

preq = [ ["Logic", "COBOL"],
            ["Data Structures", "Algorithms"],
            ["Creative Writing", "Data Structures"],
            ["Algorithms", "COBOL"],
            ["Intro to Computer Science", "Data Structures"],
            ["Logic", "Compilers"],
            ["Data Structures", "Logic"],
            ["Graphics", "Networking"],
            ["Networking", "Algorithms"],
            ["Creative Writing", "System Administration"],
            ["Databases", "System Administration"],
            ["Creative Writing", "Databases"],
            ["Intro to Computer Science", "Graphics"]]
print(course_schedule_2(preq))
