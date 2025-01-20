from models.entities.videogame import Videogame
import json

class Repo_videogames:
    __FILE_PATH = "data/videogames.json"
    
    def __init__(self):
        self.__videogames = self.__cargarTodos()
        
    def __cargarTodos(self):
        lista = []
        
        try:
            with open (Repo_videogames.__FILE_PATH, "r") as file:
                data = json.load(file)
                for videogame in data:
                    lista.append(Videogame.fromDict(videogame))
        except FileNotFoundError:
            print (f"No se encontró el archivo videogames.json en la ruta {Repo_videogames.__FILE_PATH}")
        except json.JSONDecodeError as err:
            print(f"El archivo videogames.json esta vacío o puede tener datos invalidos.\nERROR: {err}")
        except Exception as err:
            print(f"El archivo videogames.json tiene un error inesperado: {err}")
        return lista
    
    def __guardarTodos(self):
        lista = []
        for videogame in self.__videogames:
            lista.append(videogame.toDict())
        
        try:
            with open(Repo_videogames.__FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print ("No se encontró el archivo json.")
        
    def obtenerPorID(self, id):
        for videogame in self.__videogames:
            if videogame.get_id() == id:
                return videogame
        return None
    
    def existeID(self, id):
        for videogame in self.__videogames:
            if videogame.get_id() == id:
                return True
        return False
    
    def getAllGames(self):
        return self.__videogames
    
    # POST
    def addVideogame(self, id, title, my_opinion, completed, my_score, favourite):
        if not self.existeID(id):
            self.__videogames.append(Videogame(id, title, my_opinion, completed, my_score, favourite))
            self.__guardarTodos()
            return True
        return False
    
    # DELETE
    def deleteVideogame(self, id):
        for videogame in self.__videogames:
            if videogame.get_id() == id:
                self.__videogames.remove(videogame)
                self.__guardarTodos()
                return True
        return False
    
    # UPDATE
    def updateVideogame(self, id, title, my_opinion, completed, my_score, favourite):
        for videogame in self.__videogames:
            if videogame.get_id() == id:
                videogame.set_title(title)
                videogame.set_my_opinion(my_opinion)
                videogame.set_completed(completed)
                videogame.set_my_score(my_score)
                videogame.set_favourite(favourite)
                self.__guardarTodos()
                return True
        return False
