% include('header.tpl', title = "Oficinistas-Pedidos")

<div class="contenedor-nav">
    <nav class="nav">
        <a href="/" class="nombre-empresa">Paqueteria</a>
    </nav>
</div>

<div class="contenedor-todo">
    <p>Asignar un oficinista a un pedido:</p>
    <form class="form1" action="/oficinista_pedido" method="POST">
        <input type="text" placeholder="ID Pedido" size="10" maxlength="100" name="IDPedido">
        <input type="text" placeholder="ID Oficinista" size="10" maxlength="100" name="IDOficinista">
        <input type="submit" name="save" value="Añadir">
    </form>
    <p>Estos son los oficinistas asignados a cada pedido:</p>

    <div class="contenedor-tabla">
        <table border="1">
            <tr>
                <th>ID Pedido</th>
                <th>ID Oficinista</th>
                <th colspan="2">Acciones</th>
            </tr>
            %for row in rows:
            <tr>
                %for i in range(2):
                    <td>{{row[i]}}</td>
                %end
                <td>
                    <form action="/edit_oficinista_pedido/{{row[0]}}" method="GET">
                        <input type="submit" name="edit" value="Editar">
                    </form>
                </td>
                <td>
                    <form action="/delete_oficinista_pedido/{{row[0]}}" method="GET">
                        <input type="submit" name="delete" value="Borrar">
                    </form>
                </td>
            </tr>
            %end
        </table>
    </div>
</div>
% include('footer.tpl')