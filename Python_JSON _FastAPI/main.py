"""
Servidor FastAPI per a gestió d'alumnes
Basat en els exemples dels apunts de FastAPI
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

# Crear l'aplicació (com als apunts)
app = FastAPI()

# Model de dades (com als apunts de Pydantic)
class Alumne(BaseModel):
    nom: str
    cognom: str
    data: dict
    email: str
    feina: bool
    curs: str

# Carregar dades inicials (com a l'apunt de fitxers)
def carregar_alumnes() -> List[dict]:
    try:
        with open("alumnes.json", "r") as fitxer:
            return json.load(fitxer)
    except FileNotFoundError:
        return []

# Desar dades (com a l'apunt de fitxers)
def desar_alumnes(alumnes: List[dict]):
    with open("alumnes.json", "w") as fitxer:
        json.dump(alumnes, fitxer, indent=4)

# Endpoint arrel (com als exemples)
@app.get("/")
def read_root():
    return "Institut TIC de Barcelona"

# Endpoint per obtenir total alumnes (ús de len() com als apunts)
@app.get("/alumnes/")
def get_total_alumnes():
    alumnes = carregar_alumnes()
    return {"total_alumnes": len(alumnes)}

# Endpoint per obtenir alumne per ID (ús de for com als apunts)
@app.get("/id/{alumne_id}")
def get_alumne(alumne_id: int):
    alumnes = carregar_alumnes()
    
    for alumne in alumnes:
        if alumne["id"] == alumne_id:
            return alumne
    
    raise HTTPException(status_code=404, detail="Alumne no trobat")

# Endpoint per esborrar alumne (ús de list comprehension com als apunts)
@app.delete("/del/{alumne_id}")
def delete_alumne(alumne_id: int):
    alumnes = carregar_alumnes()
    alumnes_actualitzats = [a for a in alumnes if a["id"] != alumne_id]
    
    if len(alumnes_actualitzats) == len(alumnes):
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    
    desar_alumnes(alumnes_actualitzats)
    return {"missatge": f"Alumne amb ID {alumne_id} eliminat"}

# Endpoint per afegir alumne (ús de max() com als apunts)
@app.post("/alumne/")
def add_alumne(alumne: Alumne):
    alumnes = carregar_alumnes()
    nou_id = max([a["id"] for a in alumnes], default=0) + 1
    
    # Crear un nuevo diccionario con el orden deseado
    nou_alumne = {
        "id": nou_id,
        "nom": alumne.nom,
        "cognom": alumne.cognom,
        "data": alumne.data,
        "email": alumne.email,
        "feina": alumne.feina,
        "curs": alumne.curs
    }
    
    alumnes.append(nou_alumne)
    desar_alumnes(alumnes)
    return {"missatge": "Alumne afegit", "id": nou_id}

# Execució del servidor (com als apunts)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    