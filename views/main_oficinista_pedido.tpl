% include('header.tpl', title = "Oficinistas-Pedidos")
<p>Asignar un oficinista a un pedido:</p>
<form action="/new_oficinista_pedido" method="POST">
    <input type="text" size="65" maxlength="100" name="Oficinista_pedido">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Estos son los oficinistas asignados a cada pedido:</p>
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
% include('footer.tpl')