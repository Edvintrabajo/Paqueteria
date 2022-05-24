import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.repartidor import Repartidor

Repartidor = Repartidor()

@get('/Repartidor')
def index_Repartidor():
    rows= Repartidor.select()
    return template('main_Repartidors', rows=Repartidor.select())

@post('/Repartidor')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'DNIRepartidor': request.POST.dni.strip(), 
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionRepartidor': request.POST.Direccion.strip()
        }

        if data.get('DNIRepartidor') == "" or data.get('Nombre') == "" or data.get('Apellidos') == "" or data.get('DireccionRepartidor') == "":
            return redirect("/error")

        Repartidor.insert(data)

        # se muestra el resultado de la operación
        return redirect('/Repartidor')

@get('/edit_Repartidor/<no>')
def edit_item_form(no):
    fields = ['Nombre', 'Apellidos', 'DireccionRepartidor']
    where = {'DNIRepartidor': no}
    cur_data = Repartidor.get(fields, where)  # get the current data for the item we are editing
    return template('edit_Repartidors', old=cur_data, no=no)

@post('/edit_Repartidor/<no>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionRepartidor': request.POST.Direccion.strip()
        }
        if data.get('Nombre') == "":
            del data['Nombre']

        if data.get('Apellidos') == "":
            del data['Apellidos']

        if data.get('DireccionRepartidor') == "":
            del data['DireccionRepartidor']

        where = {'DNIRepartidor': no}
        
        Repartidor.update(data, where)
        
    return redirect('/Repartidor')

@get('/delete_Repartidor/<no>')
def delete_item_form(no):
    fields = ['DNIRepartidor']
    where = {'DNIRepartidor': no}
    cur_data = Repartidor.get(fields, where)  # get the current data for the item we are editing
    return template('delete_Repartidors', old=cur_data, no=no)

@post('/delete_Repartidor/<no>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'DNIRepartidor': no}
        Repartidor.delete(where)

    return redirect('/Repartidor')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)