import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.clientes import Cliente
from models.pedido import Pedido
from models.oficinista import Oficinista
from models.productos import Producto
from models.repartidor import Repartidor
from models.oficinista_pedido import Oficinista_Pedido
from models.pedido_producto import Pedido_Producto

#RUTAS CLIENTES
cliente = Cliente()

@get('/cliente')
def index_cliente():
    rows= cliente.select()
    return template('main_clientes', rows=cliente.select())

@post('/cliente')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'DNIcliente': request.POST.dni.strip(), 
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionCliente': request.POST.Direccion.strip()
        }

        if data.get('DNIcliente') == "" or data.get('Nombre') == "" or data.get('Apellidos') == "" or data.get('DireccionCliente') == "":
            return redirect("/error")

        cliente.insert(data)

        # se muestra el resultado de la operación
        return redirect('/cliente')

@get('/edit_cliente/<no>')
def edit_item_form(no):
    fields = ['Nombre', 'Apellidos', 'DireccionCliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('edit_clientes', old=cur_data, no=no)

@post('/edit_cliente/<no>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionCliente': request.POST.Direccion.strip()
        }
        if data.get('Nombre') == "":
            del data['Nombre']

        if data.get('Apellidos') == "":
            del data['Apellidos']

        if data.get('DireccionCliente') == "":
            del data['DireccionCliente']

        where = {'DNIcliente': no}
        
        cliente.update(data, where)
        
    return redirect('/cliente')

@get('/delete_cliente/<no>')
def delete_item_form(no):
    fields = ['DNIcliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('delete_clientes', old=cur_data, no=no)

@post('/delete_cliente/<no>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'DNIcliente': no}
        cliente.delete(where)

    return redirect('/cliente')


#RUTAS PEDIDO

pedido = Pedido()

@get('/pedido')
def index_pedido():
    rows= pedido.select()
    return template('main_pedidos', rows=pedido.select())

@post('/pedido')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'PesoTotal': request.POST.Peso.strip(), 
            'CosteTotal': request.POST.Coste.strip(),
            'Distancia': request.POST.Distancia.strip(),
            'DireccionEnvio': request.POST.Direccion.strip(),
            'Estado': request.POST.Estado.strip(),
            'DNIRepartidor': request.POST.DNIRepartidor.strip(),
            'DNIcliente': request.POST.DNICliente.strip()
            
        }

        if data.get('PesoTotal') == "" or data.get('CosteTotal') == "" or data.get('Distancia') == "" or data.get('DireccionEnvio') == "" or data.get('Estado') == "" or data.get('DNIRepartidor') == "" or data.get('DNIcliente') == "":
            return redirect("/error")

        pedido.insert(data)

        # se muestra el resultado de la operación
        return redirect('/pedido')

@get('/edit_pedido/<no:int>')
def edit_item_form(no):
    fields = ['PesoTotal', 'CosteTotal', 'Distancia', 'DireccionEnvio', 'Estado']
    where = {'IDPedido': no}
    cur_data = pedido.get(fields, where)  # get the current data for the item we are editing
    return template('edit_pedido', old=cur_data, no=no)

@post('/edit_pedido/<no:int>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'PesoTotal': request.POST.Peso.strip(), 
            'CosteTotal': request.POST.Coste.strip(),
            'Distancia': request.POST.Distancia.strip(),
            'DireccionEnvio': request.POST.Direccion.strip(),
            'Estado': request.POST.Estado.strip(),
            'DNIRepartidor': request.POST.DNIRepartidor.strip(),
            'DNIcliente': request.POST.DNICliente.strip()
            
        }
        
        if data.get('PesoTotal') == "":
            del data['PesoTotal']

        if data.get('CosteTotal') == "":
            del data['CosteTotal']

        if data.get('Distancia') == "":
            del data['Distancia']

        if data.get('DireccionEnvio') == "":
            del data['DireccionEnvio']

        if data.get('Estado') == "":
            del data['Estado']

        if data.get('DNIRepartidor') == "":
            del data['DNIRepartidor']

        if data.get('DNIcliente') == "":
            del data['DNIcliente']

        where = {'IDPedido': no}
        
        pedido.update(data, where)
        
    return redirect('/pedido')

@get('/delete_pedido/<no:int>')
def delete_item_form(no):
    fields = ['IDPedido']
    where = {'IDPedido': no}
    cur_data = pedido.get(fields, where)  # get the current data for the item we are editing
    return template('delete_pedido', old=cur_data, no=no)

@post('/delete_pedido/<no:int>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'IDPedido': no}
        pedido.delete(where)

    return redirect('/pedido')


#RUTAS OFICINISTA

oficinista = Oficinista()

@get('/oficinista')
def index_oficinista():
    rows= oficinista.select()
    return template('main_oficinistas', rows=oficinista.select())

@post('/oficinista')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'Nombre': request.POST.Nombre.strip(),
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


#RUTAS PRODUCTO

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


#RUTAS REPARTIDOR

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


#RUTAS OFICINISTA_PEDIDO

oficinista_pedido = Oficinista_Pedido()

@get('/oficinista_pedido')
def index_oficinista_pedido():
    rows= oficinista_pedido.select()
    return template('main_oficinista_pedido', rows=oficinista_pedido.select())

@post('/oficinista_pedido')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'IDPedido': request.POST.IDPedido.strip(),
            'ID_Oficinista': request.POST.IDOficinista.strip()
        }

        if data.get('ID_Oficinista') == "" or data.get('IDPedido') == "":
            return redirect("/error")

        oficinista_pedido.insert(data)

        # se muestra el resultado de la operación
        return redirect('/oficinista_pedido')

@get('/edit_oficinista_pedido/<no:int>')
def edit_item_form(no):
    fields = ['ID_Oficinista']
    where = {'IDPedido': no}
    cur_data = oficinista_pedido.get(fields, where)  # get the current data for the item we are editing
    return template('edit_oficinista_pedido', old=cur_data, no=no)

@post('/edit_oficinista_pedido/<no:int>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'ID_Oficinista': request.POST.IDOficinista.strip()
        }

        if data.get('ID_Oficinista') == "":
            del data['ID_Oficinista']


        where = {'IDPedido': no}
        
        oficinista_pedido.update(data, where)
        
    return redirect('/oficinista_pedido')

@get('/delete_oficinista_pedido/<no:int>')
def delete_item_form(no):
    fields = ['IDPedido']
    where = {'IDPedido': no}
    cur_data = oficinista_pedido.get(fields, where)  # get the current data for the item we are editing
    return template('delete_oficinista_pedido', old=cur_data, no=no)

@post('/delete_oficinista_pedido/<no:int>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'IDPedido': no}
        oficinista_pedido.delete(where)

    return redirect('/oficinista_pedido')


#RUTAS PEDIDO_PRODUCTO

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


#RUTAS GLOBALES

#RUTA ERROR
@error(404)
def error404(error):
    return static_file('404.html', root='static')



if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)