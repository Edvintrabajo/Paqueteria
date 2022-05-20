% include('header.tpl', title = "productos")
<p>Añadir un nuevo producto:</p>
<form action="/new_producto" method="POST">
    <input type="text" size="65" maxlength="100" name="producto">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Los productos actuales son los siguientes:</p>
<table border="1">
    <tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>Cantidad</th>
        <th>Peso</th>
        <th colspan="2">Acciones</th>
    </tr>
    %for row in rows:
    <tr>
        %for i in range(4):
            <td>{{row[i]}}</td>
        %end
        <td>
            <form action="/edit_producto/{{row[0]}}" method="GET">
                <input type="submit" name="edit" value="Editar">
            </form>
        </td>
        <td>
            <form action="/delete_producto/{{row[0]}}" method="GET">
                <input type="submit" name="delete" value="Borrar">
            </form>
        </td>
    </tr>
    %end
</table>
% include('footer.tpl')