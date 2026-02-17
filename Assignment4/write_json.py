import json

#Dictionary data 
data={
    "Name": "Ajeet Gupta",
    "Age": 20,
    "City": "Vadodara",
    "Grade": "O"
}
#Writing data to json file
with open("data.json", "w") as file:
    json.dump(data, file)
print("Data successfully written to data.json.")