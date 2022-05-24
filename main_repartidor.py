import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.repartidor import Repartidor

repartidor = Repartidor()

@get('/repartidor')
def index_repartidor():
    rows= repartidor.select()
    return template('main_repartidores', rows=repartidor.select())

@post('/repartidor')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'DNIRepartidor': request.POST.dni.strip(), 
            'NombreRepartidor': request.POST.Nombre.strip()
        }

        if data.get('DNIRepartidor') == "" or data.get('NombreRepartidor') == "":
            return redirect("/error")

        repartidor.insert(data)

        # se muestra el resultado de la operación
        return redirect('/repartidor')

@get('/edit_repartidor/<no>')
def edit_item_form(no):
    fields = ['NombreRepartidor']
    where = {'DNIRepartidor': no}
    cur_data = repartidor.get(fields, where)  # get the current data for the item we are editing
    return template('edit_repartidor', old=cur_data, no=no)

@post('/edit_repartidor/<no>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'NombreRepartidor': request.POST.NombreRepartidor.strip()
        }
        if data.get('NombreRepartidor') == "":
            del data['NombreRepartidor']

        where = {'DNIrepartidor': no}
        
        repartidor.update(data, where)
        
    return redirect('/repartidor')

@get('/delete_repartidor/<no>')
def delete_item_form(no):
    fields = ['DNIrepartidor']
    where = {'DNIrepartidor': no}
    cur_data = repartidor.get(fields, where)  # get the current data for the item we are editing
    return template('delete_repartidor', old=cur_data, no=no)

@post('/delete_repartidor/<no>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'DNIrepartidor': no}
        repartidor.delete(where)

    return redirect('/repartidor')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)