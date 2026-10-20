severity = "Error"
if severity == "ERROR":
    print("Se encontró un error")
else:
    print("No se encontró un error")
def count_errors(log_list):
    total = len(log_list)
    return total

lista = ["Database", "API", "Storage"]
respuesta = count_errors(lista)
print("Total de errores:", respuesta)