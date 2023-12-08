import sqlite3


class main():
    def __init__(self) -> None:
        #print(self)
        pass
    def update(self, filename, Basename,updatename, updateTo, params=None):
        #updatename is name of column
        #parames is 
        self.connect(filename)
        if params:
            query = f"UPDATE {Basename} SET {updatename} = '{updateTo}' WHERE {params};"
        else:
             query = f"UPDATE {Basename} SET {updatename} = '{updateTo}';"
        self.cursor.execute(query)
        self.connection.commit()
        pass
    def createDataBase(self, filename, Basename, entries):
        self.connect(filename)
        #Entries must be a dictionary in format of {"NAME":"TYPE"}, ex {"Phone":"INT"}
        entries = str(entries).strip("}{").replace("'",'').replace(":",'')
        query = f"""
                create table if not exists {Basename} (id integer primary key autoincrement,
                {entries});
                """
        self.cursor.execute(query)
    def retrieveEntries(self, filename, Basename, entries):
                self.connect(filename)
                query = f"select {entries} from {Basename}"
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                return result
        
    def connect(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        return self.cursor
    def insertInto(self, filename, Basename, entries, values):
        #entries in format: "NAME, NAME, NAME", values in format: ["VALUE", "VALUE"]
        valuesBase = []
        for i in values:
             valuesBase.append(f"{i}")
        valuesBase = str(valuesBase).strip("[]")
        #print(valuesBase)
        self.connect(filename)
        #query = f"insert into {Basename} ({entries}) values ({"?" * len(values)})"
        #print(('?,' * len(values)).strip(","))
        self.cursor.execute(f"insert into {Basename} ({entries}) values ({('?,' * len(values)).strip(',')})", values)
        self.connection.commit()


if __name__ == "__main__":
    entries = {"Name":"tinytext", "Inventory":"tinytext"}
    x = main()
    x.createDataBase("database.db","database",entries)
    entries = "Name, Inventory"
    values = ["John", "(House car money)"]
    x.insertInto("database.db","database", entries, values)
    print(x.retrieveEntries("database.db","database",entries))