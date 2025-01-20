import datetime

class Videogame:
    __ID = 0
    
    @classmethod
    def fromDict(cls, data:dict)->'Videogame':
        if not isinstance (data, dict):
            raise TypeError ("El valor ingresado por parametro en data debe ser un diccionario.")
        return cls(data["id"],data["title"], data["my_opinion"], data["completed"], data["my_score"], data["favourite"])
    
    def __init__(self, id: int, title: str, my_opinion: str, completed: bool, my_score: int, favourite: bool):
        if not isinstance (id, int) or id < 0:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero entero positivo.")

        if not isinstance (title, str) or title.isspace() or title == "":
            raise TypeError("El valor ingresado por parametro en title debe ser un string.")
        if not isinstance (my_opinion, str) or my_opinion.isspace() or my_opinion == "":
            raise TypeError("El valor ingresado por parametro en my_opinion debe ser un string.")
        if not isinstance (completed, bool):
            raise TypeError("El valor ingresado por parametro en completed debe un valor booleano.")
        if not isinstance(my_score, int) or my_score < 0:
            raise TypeError("El valor ingresado por parametro en my_score debe ser un numero entero positivo.")
        if not isinstance(favourite, bool):
            raise TypeError("El valor ingresado por parametro en favorito debe un valor booleano.")
        self.__id = id
        self.__title = title
        self.__my_opinion = my_opinion
        self.__completed = completed
        self.__my_score = my_score
        self.__favourite = favourite

        
    def get_id(self)->int:
        return self.__id
    
    def get_title(self)->str:
        return self.__title
    
    def get_my_opinion(self)->str:
        return self.__my_opinion
    
    def get_completed(self)->bool:
        return self.__completed

    def get_my_score(self)->int:
        return self.__my_score
    
    def get_favorite(self)->bool:
        return self.__favourite
    
    def set_id(self, id:int):
        if not isinstance (id, int) or id < 0:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero entero positivo.")
        self.__id = id
    
    def set_title(self, title:str):
        if not isinstance (title, str) or title.isspace() or title == "":
            raise TypeError("El valor ingresado por parametro en title debe ser un string.")
        self.__title = title
        
    def set_my_opinion(self, my_opinion:int):
        if not isinstance (my_opinion, int) or my_opinion < 0:
            raise TypeError("El valor ingresado por parametro en my_opinion debe ser un numero entero positivo.")
        self.__my_opinion = my_opinion
    
    def set_completed(self, completed:bool):
        if not isinstance (completed, bool):
            raise TypeError("El valor ingresado por parametro en completed debe un valor booleano.")
        self.__completed = completed
        
    def set_my_score(self, my_score:int):
        if not isinstance (my_score, int) or my_score < 0:
            raise TypeError("El valor ingresado por parametro en my_score debe ser un numero entero positivo.")
        self.__my_score = my_score
    
    def set_favourite(self, favourite:bool):
        if not isinstance(favourite, bool):
            raise TypeError("El valor ingresado por parametro en favorito debe un valor booleano.")
        self.__favourite = favourite
    
    def toDict(self)->dict:
        return {
            "id" : self.__id,
            "title" : self.__title,
            "my_opinion" : self.__my_opinion,
            "completed" : self.__completed,
            "my_score" : self.__my_score,
            "favourite": self.__favourite
        }