from models.repositories.repository_videogames import Repo_videogames

repo_videogames = None

def obtenerRepositoriovideogames():
    global repo_videogames
    
    if repo_videogames is None:
        repo_videogames = Repo_videogames()
    return repo_videogames
