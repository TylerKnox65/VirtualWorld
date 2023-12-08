entries = {"Name":"tinytext", "Phone": 'int', "Car":"tinytext"}
funny = str(entries).strip("}{").replace("'",'').replace(":",'')
baseEntries = []
for i in entries:
            baseEntries.append(i)
            baseEntries.append(entries[i])
            
print(baseEntries)
print(funny)