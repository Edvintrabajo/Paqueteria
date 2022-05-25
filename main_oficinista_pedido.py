import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.oficinista import Oficinista

oficinista = Oficinista()

@get('/oficinista')
def index_oficinista():
    rows= oficinista.select()
    return template('main_oficinistas', rows=oficinista.select())

@post('/oficinista')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'IDPedido': request.POST.Nombre.strip(),
        }

        if data.get('Nombre') == "":
            return redirect("/error")

        oficinista.insert(data)

        # se muestra el resultado de la operación
        return redirect('/oficinista')

@get('/edit_oficinista/<no:int>')
def edit_item_form(no):
    fields = ['Nombre']
    where = {'ID_Oficinista': no}
    cur_data = oficinista.get(fields, where)  # get the current data for the item we are editing
    return template('edit_oficinistas', old=cur_data, no=no)

@post('/edit_oficinista/<no:int>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'Nombre': request.POST.Nombre.strip()
        }
        if data.get('Nombre') == "":
            del data['Nombre']


        where = {'ID_Oficinista': no}
        
        oficinista.update(data, where)
        
    return redirect('/oficinista')

@get('/delete_oficinista/<no:int>')
def delete_item_form(no):
    fields = ['ID_Oficinista']
    where = {'ID_Oficinista': no}
    cur_data = oficinista.get(fields, where)  # get the current data for the item we are editing
    return template('delete_oficinistas', old=cur_data, no=no)

@post('/delete_oficinista/<no:int>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'ID_Oficinista': no}
        oficinista.delete(where)

    return redirect('/oficinista')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)