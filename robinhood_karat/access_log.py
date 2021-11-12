# https://leetcode.com/playground/RUtFRJ32
def access_log_1(logs):
    if not logs or len(logs)==0:
        return None
    userTime={}
    for log in logs:
        user = log[1]
        time = log[0]
        if user not in userTime:
            userTime[user] = [time]
        else:
            if len(userTime[user])==1:
                if time<userTime[user][0]:
                    userTime[user].insert(0,time)
                else:
                    userTime[user].append(time)
            else:
                if time < userTime[user][0]:
                    userTime[user][0] = time
                if time > userTime[user][1]:
                    userTime[user][1]=time
    for k, v in userTime.items():
        if len(v)==1:
            userTime[k].append(v[0])
    return userTime

def access_log2(logs):
    resourceToTime ={}
    for log in logs:
        resource = log[2]
        time=int(log[0])
        if resource in resourceToTime:
            resourceToTime[resource].append(time)
        else:
            resourceToTime[resource]=[time]
    maxAccessedResource = None
    maxAccessedTimes = 0
    for k,v in resourceToTime.items():
        resourceToTime[k]=sorted(v)
        for i in range(len(resourceToTime[k])):
            target = resourceToTime[k][i]+300
            index = binarySearch(resourceToTime[k],i,target)
            if resourceToTime[k][index] > target:
                index-=1
            if index-i+1 > maxAccessedTimes:
                maxAccessedTimes = index-i+1
                maxAccessedResource = k
    return maxAccessedResource, maxAccessedTimes

def binarySearch(nums,start,target):
    end = len(nums)-1
    while start<end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            end = mid
        else:
            start = mid+1
    return start


def access_log3(logs):
    logs.sort(key = lambda x:int(x[0]))
    userToResource = {}
    for log in logs:
        user = log[1]
        resource = log[2]
        if user not in userToResource:
            userToResource[user]=[resource]
        else:
            userToResource[user].append(resource)
    print(userToResource)
    adjMap ={}
    adjMap["START"]={}
    print(adjMap)
    for user, resources in userToResource.items():
        first = resources[0]
        if first in adjMap["START"]:
            adjMap["START"][first]+=1
        else:
            adjMap["START"][first]= 1
        for i in range(1,len(resources)):
            curr = resources[i]
            prev= resources[i-1]
            if prev not in adjMap:
                adjMap[prev]={curr:1}
            else:
                if curr in adjMap[prev]:
                    adjMap[prev][curr]+=1
                else:
                    adjMap[prev][curr]= 1
        last = resources[-1]
        if last in adjMap:
            if "END" in adjMap[last]:
                adjMap[last]["END"]+=1
            else:
                adjMap[last]["END"]= 1
        else:
            adjMap[last]={"END":1}
    for k, v in adjMap.items():
        total = 0
        for resource, count in v.items():
            total+=count
        for resource, curr in v.items():
            v[resource]=round(curr/total,3)
    return adjMap







logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

# print(access_log_1(logs1))

logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]
# print(access_log2(logs2))
# logs1.sort(key=lambda x:int(x[0]))
# for log in logs1:
#     print(log)
print(access_log3(logs1))