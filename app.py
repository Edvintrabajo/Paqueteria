import sys
sys.path.append('models')
sys.path.append('forms')
from bottle import run, template, request, get, post, redirect, static_file, error, auth_basic
from models.clientes import Cliente
from models.pedido import Pedido
from models.oficinista import Oficinista
from models.productos import Producto
from models.repartidor import Repartidor
from models.oficinista_pedido import Oficinista_Pedido
from models.pedido_producto import Pedido_Producto
from validaciones import *
from forms.cliente import RegistrationForm


def is_authenticated_user(user, password):
    if user == "paqueteria":
        return True
    return False

#RUTAS CLIENTES
cliente = Cliente()

@get('/cliente')
@auth_basic(is_authenticated_user)
def index_cliente_get():
    return template('main_clientes', rows=cliente.select(), form = RegistrationForm(request.POST))

@post('/cliente')
def nuevo_cliente_post():
    form = RegistrationForm(request.POST) 
    if form.save.data and form.validate():
        form_data = {
            'DNIcliente': form.dni.data, 
            'Nombre': form.nombre.data,
            'Apellidos': form.apellido.data,
            'DireccionCliente': form.direccion.data
        }

        form_data.update({'DNIcliente': form_data.get("DNIcliente").upper()})

        if validaciondni(form_data.get('DNIcliente')) == False:
            errormsg = f"No has introducido un DNI válido"
            return template('404', error=errormsg)

        cliente.insert(form_data)

        # se muestra el resultado de la operación
        return redirect('/cliente')

@get('/edit_cliente/<no>')
def editar_cliente_get(no):
    fields = ['Nombre', 'Apellidos', 'DireccionCliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('edit_clientes', old=cur_data, no=no)

@post('/edit_cliente/<no>')
def editar_cliente_post(no):
    
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
def borrar_cliente_get(no):
    fields = ['DNIcliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('delete_clientes', old=cur_data, no=no)

@post('/delete_cliente/<no>')
def borrar_cliente_post(no):
    
    if request.POST.delete:
        where = {'DNIcliente': no}
        cliente.delete(where)

    return redirect('/cliente')


#RUTAS PEDIDO

pedido = Pedido()

@get('/pedido')
@auth_basic(is_authenticated_user)
def index_pedido_get():
    return template('main_pedidos', rows=pedido.select())

@post('/pedido')
def nuevo_pedido_post():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'Distancia': request.POST.Distancia.strip(),
            'DireccionEnvio': request.POST.Direccion.strip(),
            'DNIRepartidor': request.POST.DNIRepartidor.strip(),
            'DNIcliente': request.POST.DNICliente.strip()
        }

        if data.get('Distancia') == "" or data.get('DireccionEnvio') == "" or data.get('Estado') == "" or data.get('DNIRepartidor') == "" or data.get('DNIcliente') == "":
            errormsg = "Has dejado algún campo vacio"
            return template('404', error=errormsg)

        dnirepartidor = data.get("DNIRepartidor")
        dnicliente = data.get("DNIcliente")

        where = {'DNIRepartidor': dnirepartidor}

        if repartidor.get(['DNIRepartidor'], where) == False:

            errormsg = f"No existe el DNI {dnirepartidor} en la tabla"
            return template('404', error=errormsg)

        where = {'DNIcliente': dnicliente}

        if cliente.get(['DNIcliente'], where) == False:

            errormsg = f"No existe el DNI {dnicliente} en la tabla"
            return template('404', error=errormsg)

        pedido.insert(data)
        id_p = pedido.select_maxid()
        id_p = id_p[0]
        asignarprecio_distancia({"IDPedido" : id_p})

        # se muestra el resultado de la operación
        return redirect('/pedido')

@get('/edit_pedido/<no:int>')
def editar_pedido_get(no):
    fields = ['Estado']
    where = {'IDPedido': no}
    cur_data = pedido.get(fields, where)  # get the current data for the item we are editing
    return template('edit_pedido', old=cur_data, no=no)

@post('/edit_pedido/<no:int>')
def editar_pedido_post(no):
    
    if request.POST.save:
        data = {
            'Estado': request.POST.Estado.strip()  
        }

        if data.get('Estado') == "":
            return redirect('/pedido')

        data.update({'Estado': data.get("Estado").upper()})

        where = {'IDPedido': no}
        
        pedido.update(data, where)
        
    return redirect('/pedido')

@get('/delete_pedido/<no:int>')
def borrar_pedido_get(no):
    fields = ['IDPedido']
    where = {'IDPedido': no}
    cur_data = pedido.get(fields, where)  # get the current data for the item we are editing
    return template('delete_pedido', old=cur_data, no=no)

@post('/delete_pedido/<no:int>')
def borrar_pedido_post(no):
    
    if request.POST.delete:
        where = {'IDPedido': no}
        pedido.delete(where)
        pedido_producto.delete(where)
        oficinista_pedido.delete(where)

    return redirect('/pedido')


#RUTAS OFICINISTA

oficinista = Oficinista()

@get('/oficinista')
@auth_basic(is_authenticated_user)
def index_oficinista_get():
    return template('main_oficinistas', rows=oficinista.select())

@post('/oficinista')
def nuevo_oficinista_post():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'Nombre': request.POST.Nombre.strip(),
        }

        if data.get('Nombre') == "":
            errormsg = f"No has introducido ningún nombre"
            return template('404', error=errormsg)

        oficinista.insert(data)

        # se muestra el resultado de la operación
        return redirect('/oficinista')

@get('/edit_oficinista/<no:int>')
def editar_oficinista_get(no):
    fields = ['Nombre']
    where = {'ID_Oficinista': no}
    cur_data = oficinista.get(fields, where)  # get the current data for the item we are editing
    return template('edit_oficinistas', old=cur_data, no=no)

@post('/edit_oficinista/<no:int>')
def editar_oficinista_post(no):
    
    if request.POST.save:
        data = {
            'Nombre': request.POST.Nombre.strip()
        }
        if data.get('Nombre') == "":
            return redirect('/oficinista')

        where = {'ID_Oficinista': no}
        
        oficinista.update(data, where)
        
    return redirect('/oficinista')

@get('/delete_oficinista/<no:int>')
def borrar_oficinista_get(no):
    fields = ['ID_Oficinista']
    where = {'ID_Oficinista': no}
    cur_data = oficinista.get(fields, where)  # get the current data for the item we are editing
    return template('delete_oficinistas', old=cur_data, no=no)

@post('/delete_oficinista/<no:int>')
def borrar_oficinista_post(no):
    
    if request.POST.delete:
        where = {'ID_Oficinista': no}
        oficinista.delete(where)
        oficinista_pedido.delete(where)

    return redirect('/oficinista')


#RUTAS PRODUCTO

producto = Producto()

@get('/producto')
@auth_basic(is_authenticated_user)
def index_producto_get():
    return template('main_productos', rows=producto.select())

@post('/producto')
def nuevo_producto_post():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'NombreProducto': request.POST.Nombre.strip(),
            'CantidadProducto': request.POST.Cantidad.strip(),
            'PesoProducto': request.POST.Peso.strip()
        }

        if data.get('NombreProducto') == "" or data.get('CantidadProducto') == "" or data.get('PesoProducto') == "":
            errormsg = "Has dejado algún campo vacio"
            return template('404', error=errormsg)

        cantidad = data.get("CantidadProducto")
        peso = data.get("PesoProducto")

        try:
            float(cantidad)
        except:
            errormsg = f"No has introducido una cantidad válida"
            return template('404', error=errormsg)

        try:
            float(peso)
        except:
            errormsg = f"No has introducido un peso válido"
            return template('404', error=errormsg)

        producto.insert(data)

        # se muestra el resultado de la operación
        return redirect('/producto')

@get('/edit_producto/<no:int>')
def editar_producto_get(no):
    fields = ['NombreProducto']
    where = {'IDProducto': no}
    cur_data = producto.get(fields, where)  # get the current data for the item we are editing
    return template('edit_productos', old=cur_data, no=no)

@post('/edit_producto/<no:int>')
def editar_producto_post(no):
    
    if request.POST.save:
        data = {
            'NombreProducto': request.POST.Nombre.strip()
        }
        if data.get('NombreProducto') == "":
            del data['NombreProducto']

        where = {'IDProducto': no}
        
        producto.update(data, where)
        
    return redirect('/producto')

@get('/delete_producto/<no:int>')
def borrar_producto_get(no):
    fields = ['IDProducto']
    where = {'IDProducto': no}
    cur_data = producto.get(fields, where)  # get the current data for the item we are editing
    return template('delete_productos', old=cur_data, no=no)

@post('/delete_producto/<no:int>')
def borrar_producto_post(no):
    
    if request.POST.delete:
        where = {'IDProducto': no}
        producto.delete(where)

    return redirect('/producto')


#RUTAS REPARTIDOR

repartidor = Repartidor()

@get('/repartidor')
@auth_basic(is_authenticated_user)
def index_repartidor_get():
    return template('main_repartidores', rows=repartidor.select())

@post('/repartidor')
def nuevo_repartidor_post():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'DNIRepartidor': request.POST.dni.strip(), 
            'NombreRepartidor': request.POST.Nombre.strip()
        }

        if data.get('DNIRepartidor') == "" or data.get('NombreRepartidor') == "":
            errormsg = "Has dejado algún campo vacio"
            return template('404', error=errormsg)

        repartidor.insert(data)

        # se muestra el resultado de la operación
        return redirect('/repartidor')

@get('/edit_repartidor/<no>')
def editar_repartidor_get(no):
    fields = ['NombreRepartidor']
    where = {'DNIRepartidor': no}
    cur_data = repartidor.get(fields, where)  # get the current data for the item we are editing
    return template('edit_repartidor', old=cur_data, no=no)

@post('/edit_repartidor/<no>')
def editar_repartidor_post(no):
    
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
def borrar_repartidor_get(no):
    fields = ['DNIrepartidor']
    where = {'DNIrepartidor': no}
    cur_data = repartidor.get(fields, where)  # get the current data for the item we are editing
    return template('delete_repartidor', old=cur_data, no=no)

@post('/delete_repartidor/<no>')
def borrar_repartidor_post(no):
    
    if request.POST.delete:
        where = {'DNIrepartidor': no}
        repartidor.delete(where)

    return redirect('/repartidor')


#RUTAS OFICINISTA_PEDIDO

oficinista_pedido = Oficinista_Pedido()

@get('/oficinista_pedido')
@auth_basic(is_authenticated_user)
def index_oficinista_pedido_get():
    return template('main_oficinista_pedido', rows=oficinista_pedido.select())

@post('/oficinista_pedido')
def nuevo_oficinista_pedido_post():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'IDPedido': request.POST.IDPedido.strip(),
            'ID_Oficinista': request.POST.IDOficinista.strip()
        }

        if data.get('ID_Oficinista') == "" or data.get('IDPedido') == "":
            errormsg = "Has dejado algún campo vacio"
            return template('404', error=errormsg)
            
        idpedido = data.get("IDPedido")
        idoficinista = data.get("ID_Oficinista")

        where = {'IDPedido': idpedido}

        if pedido.get(['IDPedido'], where) == False:

            errormsg = f"No existe el ID pedido {idpedido} en la tabla"
            return template('404', error=errormsg)

        where = {'ID_Oficinista': idoficinista}

        if oficinista.get(['ID_Oficinista'], where) == False:

            errormsg = f"No existe el ID oficinista {idoficinista} en la tabla"
            return template('404', error=errormsg)

        else:

            oficinista_pedido.insert(data)

        # se muestra el resultado de la operación
        return redirect('/oficinista_pedido')

@get('/edit_oficinista_pedido/<no:int>')
def editar_oficinista_pedido_get(no):
    fields = ['ID_Oficinista']
    where = {'IDPedido': no}
    cur_data = oficinista_pedido.get(fields, where)  # get the current data for the item we are editing
    return template('edit_oficinista_pedido', old=cur_data, no=no)

@post('/edit_oficinista_pedido/<no:int>')
def editar_oficinista_pedido_post(no):
    
    if request.POST.save:
        data = {
            'ID_Oficinista': request.POST.IDOficinista.strip()
        }

        if data.get('ID_Oficinista') == "":
            return redirect('/oficinista_pedido')

        idoficinista = data.get("ID_Oficinista")

        where = {'ID_Oficinista': idoficinista}

        if oficinista.get(['ID_Oficinista'], where) == False:

            errormsg = f"No existe el ID oficinista {idoficinista} en la tabla"
            return template('404', error=errormsg)

        else:
            where = {'IDPedido': no}
            oficinista_pedido.update(data, where)
        
    return redirect('/oficinista_pedido')



@get('/delete_oficinista_pedido/<no:int>')
def borrar_oficinista_get(no):
    fields = ['IDPedido']
    where = {'IDPedido': no}
    cur_data = oficinista_pedido.get(fields, where)  # get the current data for the item we are editing
    return template('delete_oficinista_pedido', old=cur_data, no=no)

@post('/delete_oficinista_pedido/<no:int>')
def borrar_oficinista_post(no):
    
    if request.POST.delete:
        where = {'IDPedido': no}
        oficinista_pedido.delete(where)

    return redirect('/oficinista_pedido')


#RUTAS PEDIDO_PRODUCTO

pedido_producto = Pedido_Producto()

@get('/pedido_producto')
@auth_basic(is_authenticated_user)
def index_pedido_producto_get():
    return template('main_pedido_producto', rows=pedido_producto.select())

@post('/pedido_producto')
def nuevo_pedido_producto_post():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'IDPedido': request.POST.id_pedido.strip(), 
            'IDProducto': request.POST.id_producto.strip()
        }

        if data.get('IDPedido') == "" or data.get('IDProducto') == "":
            errormsg = "Has dejado algún campo vacio"
            return template('404', error=errormsg)
            
        idpedido = data.get("IDPedido")
        idproducto = data.get("IDProducto")

        where = {'IDPedido': idpedido}

        if pedido.get(['IDPedido'], where) == False:

            errormsg = f"No existe el ID pedido {idpedido} en la tabla"
            return template('404', error=errormsg)

        where = {'IDProducto': idproducto}

        if producto.get(['IDProducto'], where) == False:

            errormsg = f"No existe el ID producto {idproducto} en la tabla"
            return template('404', error=errormsg)

        id_productos = pedido_producto.get_all({"IDProducto"}, {"IDProducto" : idproducto})
        if len(id_productos) != 0:
            errormsg = f"El ID producto {idproducto} ya está asignado en otro pedido"
            return template('404', error=errormsg)

        else:
            pedido_producto.insert(data)
            id_p_p = pedido_producto.get_p_p({"ID_Pedido_Producto"},[idpedido, idproducto])
            id_p_p = id_p_p[0]
            asignarprecio({"ID_Pedido_Producto" : id_p_p})
        return redirect('/pedido_producto')

@get('/edit_pedido_producto/<no:int>')
def editar_pedido_producto_get(no):
    fields = ['IDPedido', 'IDProducto']
    where = {'ID_Pedido_Producto': no}
    cur_data = pedido_producto.get(fields, where)  # get the current data for the item we are editing
    return template('edit_pedido_producto', old=cur_data, no=no)

@post('/edit_pedido_producto/<no:int>')
def editar_pedido_producto_post(no):
    
    if request.POST.save:
        data = {
            'IDPedido': request.POST.id_pedido.strip(), 
            'IDProducto': request.POST.id_producto.strip()
        }

        idpedido = data.get("IDPedido")
        idproducto = data.get("IDProducto")

        if data.get('IDPedido') == "":
            del data['IDPedido']

        if data.get('IDProducto') == "":
            del data['IDProducto']

        where = {'IDPedido': idpedido}

        if pedido.get(['IDPedido'], where) == False:

            errormsg = f"No existe el ID pedido {idpedido} en la tabla"
            return template('404', error=errormsg)

        where = {'IDProducto': idproducto}

        if idproducto != "":
            if producto.get(['IDProducto'], where) == False:

                errormsg = f"No existe el ID producto {idproducto} en la tabla"
                return template('404', error=errormsg)

        idproducto_antiguo = pedido_producto.get(['IDProducto'], {'ID_Pedido_Producto' : no})
        idproducto_antiguo = str(idproducto_antiguo[0])

        if idproducto_antiguo != idproducto:

            id_productos = pedido_producto.get_all({"IDProducto"}, {"IDProducto" : idproducto})
            if len(id_productos) != 0:
                errormsg = f"El ID producto {idproducto} ya está asignado en otro pedido"
                return template('404', error=errormsg)

        where1 = {'ID_Pedido_Producto': no}
        eliminar_producto_en_pedido({"ID_Pedido_Producto" : no})
        pedido_producto.update(data, where1)
        asignarprecio({"ID_Pedido_Producto" : no})
        
    return redirect('/pedido_producto')

@get('/delete_pedido_producto/<no:int>')
def borrar_pedido_get(no):
    fields = ['ID_Pedido_Producto']
    where = {'ID_Pedido_Producto': no}
    cur_data = pedido_producto.get(fields, where)  # get the current data for the item we are editing
    return template('delete_pedido_producto', old=cur_data, no=no)

@post('/delete_pedido_producto/<no:int>')
def borrar_pedido_post(no):
    
    if request.POST.delete:
        where = {'ID_Pedido_Producto': no}
        eliminar_producto_en_pedido({"ID_Pedido_Producto" : no})
        pedido_producto.delete(where)

    return redirect('/pedido_producto')


#RUTAS GLOBALES

@get('/')
@auth_basic(is_authenticated_user)
def index_get():
    return static_file('index.html', root='static')

@get("/static/<filepath:path>")
@auth_basic(is_authenticated_user)
def html(filepath):
    return static_file(filepath, root = "static")

#RUTA ERROR
@error(404)
@auth_basic(is_authenticated_user)
def error404(error):
    errormsg = f"Página no encontrada"
    return template('404', error=errormsg)



if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
