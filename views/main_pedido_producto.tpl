% include('header.tpl', title = "Pedido-Producto")

<div class="contenedor-nav">
    <nav class="nav">
        <a href="/" class="nombre-empresa">Paqueteria</a>
    </nav>
</div>

<div class="contenedor-todo">
    <p>Asignar un producto a un pedido:</p>
    <form class="form1" action="/pedido_producto" method="POST">
        <input type="text" placeholder="ID Pedido" size="10" maxlength="100" name="id_pedido">
        <input type="text" placeholder="ID Producto" size="10" maxlength="100" name="id_producto">
        <input type="submit" name="save" value="Añadir">
    </form>
    <p>Estos son los productos asignados a cada pedido:</p>
    <div class="contenedor-tabla">
        <table border="1">
            <tr>
                <th>ID</th>
                <th>ID Pedido</th>
                <th>ID Producto</th>
                <th colspan="2">Acciones</th>
            </tr>
            %for row in rows:
            <tr>
                %for i in range(3):
                    <td>{{row[i]}}</td>
                %end
                <td>
                    <form action="/edit_pedido_producto/{{row[0]}}" method="GET">
                        <input type="submit" name="edit" value="Editar">
                    </form>
                </td>
                <td>
                    <form action="/delete_pedido_producto/{{row[0]}}" method="GET">
                        <input type="submit" name="delete" value="Borrar">
                    </form>
                </td>
            </tr>
            %end
        </table>
    </div>
</div>
% include('footer.tpl')