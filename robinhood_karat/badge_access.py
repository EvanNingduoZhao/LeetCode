badge_records = [
  ["Paul",     "1214", "enter"],
  ["Paul",      "830", "enter"],
  ["Curtis",   "1100", "enter"],
  ["Paul",      "903", "exit"],
  ["John",      "908", "exit"],
  ["Paul",     "1235", "exit"],
  ["Jennifer",  "900", "exit"],
  ["Curtis",   "1330", "exit"],
  ["John",      "815", "enter"],
  ["Jennifer", "1217", "enter"],
  ["Curtis",    "745", "enter"],
  ["John",     "1230", "enter"],
  ["Jennifer",  "800", "enter"],
  ["John",     "1235", "exit"],
  ["Curtis",    "810", "exit"],
  ["Jennifer", "1240", "exit"],
]
badge_times = [
  ["Paul",     "1355"],
  ["Jennifer", "1910"],
  ["John",      "830"],
  ["Paul",     "1315"],
  ["John",     "1615"],
  ["John",     "1640"],
  ["John",      "835"],
  ["Paul",     "1405"],
  ["John",      "855"],
  ["John",      "930"],
  ["John",      "915"],
  ["John",      "730"],
  ["John",      "940"],
  ["Jennifer", "1335"],
  ["Jennifer",  "730"],
  ["John",     "1630"],
  ["Jennifer",    "5"]
]

def find_fb_1(badge_times):
    badge_times.sort(key=lambda x:int(x[1]))
    personToTime = {}
    for person, time in badge_times:
        if person not in personToTime:
            personToTime[person]=[int(time)]
        else:
            personToTime[person].append(int(time))
    print(personToTime)
    res = {}
    for person in personToTime.keys():
        for i in range(len(personToTime[person])):
            target = personToTime[person][i]+100
            index = binarySearch(personToTime[person],i,target)
            if index>target:
                index-=1
            if index-i+1>=3:
                res[person]=personToTime[person][i:index+1]
                break
    return res




def binarySearch(nums,start,target):
    end = len(nums)-1
    while start < end:
        mid = start + (end-start)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start = mid +1
        else:
            end = mid
    return start


print(find_fb_1(badge_times))



def find_fb(badge_records):
    badge_records.sort(key=lambda t: t[1])

    curr_room = set()

    # [start, end, set of ppl in room during period]
    room_state = []

    for i, (name, time, event) in enumerate(badge_records):
        if event == "enter":
            if i>=1:
                prev_time=badge_records[i-1][1]
                room_state.append([prev_time,time,curr_room.copy()])

            curr_room.add(name)
        else:
            _, prev_time, _ = badge_records[i - 1]
            room_state.append([prev_time, time, curr_room.copy()])
            curr_room.remove(name)

    largest_group = set()
    ans = []

    for i in range(len(room_state)):
        for j in range(i + 1, len(room_state)):
            i_start, i_end, i_room = room_state[i]
            j_start, j_end, j_room = room_state[j]

            if j_start > i_end:
                common = i_room & j_room
                if len(common) > len(largest_group):
                    largest_group = common.copy()

    # find all time periods where the largest group was found together
    for start, end, room in room_state:
        if largest_group <= room:
            ans.append([start, end])

    return largest_group, ans

print(find_fb(badge_records))