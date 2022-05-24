import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.pedido import Pedido

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

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)