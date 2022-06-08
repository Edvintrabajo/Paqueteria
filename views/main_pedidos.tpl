% include('header.tpl', title = "pedidos")

<div class="contenedor-nav">
    <nav class="nav">
        <a href="/" class="nombre-empresa">Paqueteria</a>
    </nav>
</div>

<div class="contenedor-todo">
    <p>Añadir un nuevo pedido:</p>
    <form class="form1" action="/pedido" method="POST">
        <input type="text" placeholder="Distancia" size="10" maxlength="100" name="Distancia">
        <input type="text" placeholder="Direccion" size="10" maxlength="100" name="Direccion">
        <input type="text" placeholder="DNI Repartidor" size="10" maxlength="100" name="DNIRepartidor">
        <input type="text" placeholder="DNI Cliente" size="10" maxlength="100" name="DNICliente">
        <input type="submit" name="save" value="Añadir">
    </form>
    <p>Los pedidos actuales son los siguientes:</p>
    <div class="contenedor-tabla">
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Peso</th>
                <th>Coste</th>
                <th>Distancia</th>
                <th>Direccion</th>
                <th>Estado</th>
                <th>DNI Repartidor</th>
                <th>DNI Cliente</th>
                <th colspan="2">Acciones</th>
            </tr>
            %for row in rows:
            <tr>
                %for i in range(8):
                    <td>{{row[i]}}</td>
                %end
                <td>
                    <form action="/edit_pedido/{{row[0]}}" method="GET">
                        <input type="submit" name="edit" value="Editar">
                    </form>
                </td>
                <td>
                    <form action="/delete_pedido/{{row[0]}}" method="GET">
                        <input type="submit" name="delete" value="Borrar">
                    </form>
                </td>
            </tr>
            %end
        </table>
    </div>
</div>
% include('footer.tpl')