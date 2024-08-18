import json

class Helper:
    @staticmethod
    def getfileData(filestr:str):
        with open(filestr) as f:
            data = f.readlines()
            return data
    
    @staticmethod
    def getJson(filestr:str):
        return json.loads( Helper.getfileData(filestr) )
    
    @staticmethod
    def getModelSize(file:str):
        for i in range ( len(file) ):
            if("model_size" in file[i]):
                model_size = file[i+1].split()
                return int(model_size[0]), int(model_size[2])

    @staticmethod
    def getAPItoken(filepath:str):
        with open(filepath, 'r', encoding='utf-8') as F:
            return F.readlines()
            