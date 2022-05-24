import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.productos import Producto

producto = Producto()

@get('/producto')
def index_producto():
    rows= producto.select()
    return template('main_productos', rows=producto.select())

@post('/producto')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'NombreProducto': request.POST.Nombre.strip(),
            'CantidadProducto': request.POST.Cantidad.strip(),
            'PesoProducto': request.POST.Peso.strip()
        }

        if data.get('NombreProducto') == "" or data.get('CantidadProducto') == "" or data.get('PesoProducto') == "":
            return redirect("/error")

        producto.insert(data)

        # se muestra el resultado de la operación
        return redirect('/producto')

@get('/edit_producto/<no:int>')
def edit_item_form(no):
    fields = ['NombreProducto', 'CantidadProducto', 'PesoProducto']
    where = {'IDProducto': no}
    cur_data = producto.get(fields, where)  # get the current data for the item we are editing
    return template('edit_productos', old=cur_data, no=no)

@post('/edit_producto/<no:int>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'NombreProducto': request.POST.Nombre.strip(),
            'CantidadProducto': request.POST.Cantidad.strip(),
            'PesoProducto': request.POST.Peso.strip()
        }
        if data.get('NombreProducto') == "":
            del data['NombreProducto']

        if data.get('CantidadProducto') == "":
            del data['CantidadProducto']

        if data.get('PesoProducto') == "":
            del data['PesoProducto']

        where = {'IDProducto': no}
        
        producto.update(data, where)
        
    return redirect('/producto')

@get('/delete_producto/<no:int>')
def delete_item_form(no):
    fields = ['IDProducto']
    where = {'IDProducto': no}
    cur_data = producto.get(fields, where)  # get the current data for the item we are editing
    return template('delete_productos', old=cur_data, no=no)

@post('/delete_producto/<no:int>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'IDProducto': no}
        producto.delete(where)

    return redirect('/producto')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)