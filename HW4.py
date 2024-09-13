#Name: Chaysen Wise
#Class: 5th hour
#Assignment: HW4

print ("Hello World!")

carDict = {
    "brand" : "Mazda",
    "model" : "Miata",
    "year" : [1994,1995,1996]
}

print (carDict["year"][2])

carDict.update({"has pop ups" : True})

print (carDict)

carDict.clear()

print (carDict)

ClassDict = {
    "Student1" : {
         "name" : "Kevin",
        "grade" : "11",
      "esports" : True,
},
"Student2" : {
         "name" : "Zach",
        "grade" : "12",
      "esports" : False,
},
    "Student3": {
 "name": "Chaysen",
"grade": "11",
"esports": False,
}
}

print(ClassDict["Student1"]["name"],ClassDict["Student2"]["name"],ClassDict["Student3"]["name"],)