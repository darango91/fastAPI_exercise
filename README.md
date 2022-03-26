# FastAPI_exercise
Just a small Fast API exercise

To run this project you have to:
* Create a virtualenv
* Install the requirements

## Run the project using uvicorn
```
$ uvicorn main:app --reload
```

<details markdown="1">
<summary>Que hace el comando? <code>uvicorn main:app --reload</code>...</summary>

El comando `uvicorn main:app` hace lo siguiente:

* `main`: el archivo `main.py` (el "modulo" Python).
* `app`: el objeto creado dentro del `main.py` con la linea `app = FastAPI()`.
* `--reload`: Hace que el servidor se reinicie cada que hay cambios en el codigo, de ser usado solo para desarrollo.

</details>
