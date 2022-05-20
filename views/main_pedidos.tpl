% include('header.tpl', title = "pedidos")
<p>Añadir un nuevo pedido:</p>
<form action="/new_pedido" method="POST">
    <input type="text" size="65" maxlength="100" name="pedido">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Los pedidos actuales son los siguientes:</p>
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
% include('footer.tpl')