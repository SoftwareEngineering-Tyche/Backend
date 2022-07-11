class Db :


    def __init__(self):
        self.data = {}

    def set(self,id,key,value):
        try:
            self.data[id][key] = value
        except:
            self.data[id] = {key:value}

    def get(self,id,key):
        try:
            return self.data[id].get(key)
        except:
            pass



