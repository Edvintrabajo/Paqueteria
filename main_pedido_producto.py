import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.pedido_producto import Pedido_Producto

pedido_producto = Pedido_Producto()

@get('/pedido_producto')
def index_pedido_producto():
    rows= pedido_producto.select()
    return template('main_pedido_producto', rows=pedido_producto.select())

@post('/pedido_producto')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'IDPedido': request.POST.id_pedido.strip(), 
            'IDProducto': request.POST.id_producto.strip()
        }

        if data.get('IDPedido') == "" or data.get('IDProducto') == "":
            return redirect("/error")

        pedido_producto.insert(data)

        # se muestra el resultado de la operación
        return redirect('/pedido_producto')

@get('/edit_pedido_producto/<no:int>')
def edit_item_form(no):
    fields = ['IDPedido', 'IDProducto']
    where = {'ID_Pedido_Producto': no}
    cur_data = pedido_producto.get(fields, where)  # get the current data for the item we are editing
    return template('edit_pedido_producto', old=cur_data, no=no)

@post('/edit_pedido_producto/<no:int>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'IDPedido': request.POST.id_pedido.strip(), 
            'IDProducto': request.POST.id_producto.strip()
        }

        if data.get('IDPedido') == "":
            del data['IDPedido']

        if data.get('IDProducto') == "":
            del data['IDProducto']

        where = {'ID_Pedido_Producto': no}
        
        pedido_producto.update(data, where)
        
    return redirect('/pedido_producto')

@get('/delete_pedido_producto/<no:int>')
def delete_item_form(no):
    fields = ['ID_Pedido_Producto']
    where = {'ID_Pedido_Producto': no}
    cur_data = pedido_producto.get(fields, where)  # get the current data for the item we are editing
    return template('delete_pedido_producto', old=cur_data, no=no)

@post('/delete_pedido_producto/<no:int>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'ID_Pedido_Producto': no}
        pedido_producto.delete(where)

    return redirect('/pedido_producto')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)