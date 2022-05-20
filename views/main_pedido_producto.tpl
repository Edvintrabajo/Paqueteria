% include('header.tpl', title = "Pedido-Producto")
<p>Asignar un producto a un pedido:</p>
<form action="/new_pedido_producto" method="POST">
    <input type="text" size="65" maxlength="100" name="Pedido-Producto">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Estos son los productos asignados a cada pedido:</p>
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
% include('footer.tpl')