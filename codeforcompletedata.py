import requests,pprint,json
fileOfslugs = open('slugs1.json',"r")
list_slugs = json.load(fileOfslugs)

fileOfcourse = open("hangman1.json","r")
dict_course = json.load(fileOfcourse)

list_course = dict_course["availableCourses"]

print(list_course[0]["id"])

for i in range(len(list_slugs)):
    # list_course[i]["data"] = 
    if list_slugs[i] == []:
        list_course[i]["data"] = list_slugs[i]
    else:
        for mainSlug in list_slugs[i]:
            list_for_childexercise = []
            if type(mainSlug) == list:
                if mainSlug == []:
                    list_course[i]["childExercises"] = []
                elif mainSlug != []:
                    res = requests.get("http://saral.navgurukul.org/api/courses/"+str(list_course[i]["id"])+"/exercise/getBySlug?slug="+mainSlug).json()
                    list_for_childexercise.append(res)
            list_course[i]["childExercises"] = list_for_childexercise
                # else:
                #     res = requests.get("http://saral.navgurukul.org/api/courses/"+str(list_course[i]["id"])+"/exercise/getBySlug?slug="+list_slugs[i]).json()
                #     list_course[i]["childExercises"] = res
print(list_for_childexercise)




import requests,pprint,json

    
file2 = open("Slugs.json","r+")
ind = json.load(file2)

listOfslugs = []

for One in ind:
    for ind2 in One:
        if type(ind2) != list:
            dictForcontent = {}
            for key,value in ind2.items():
                if key == "content":
                    dictForcontent[key] = value
                elif key == "id":
                    dictForcontent[key] = value
            listOfslugs.append(dictForcontent)

        elif type(ind2) == list:
            for dict_ in ind2:
                dictForcontent = {}
                for key1,value1 in dict_.items():
                    if key1 == "content":
                        dictForcontent[key1] = value1
                    elif key1 == "id":
                        dictForcontent[key1] = value1
                listOfslugs.append(dictForcontent)

data = open("contentId.json","w+")
json.dump(listOfslugs,data,indent=4)



import requests,pprint,json
file = open("contentId.json","r+")
dataC = json.load(file)

file2 = open("saraAvailableCourses.json","r+")
totaldata = json.load(file2)

totalD = totaldata[0]["courses"]

count = 0

for dict_ in totalD:
    count +=1
    if count == 1:
        continue
    else:
        for subDicts in dict_["data"]:
            for individualDict in dataC:
                if individualDict['id'] == subDicts["id"]:
                    subDicts["content"] = individualDict["content"]
            for childDict in subDicts["childExercises"]:
                for individualDict in dataC:
                    if individualDict["id"] == childDict["id"]:
                        childDict["content"] = individualDict["content"]
complete = open("completedata.json","w+")
json.dump(totaldata,complete,indent=4)
