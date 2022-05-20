% include('header.tpl', title = "Clientes")
<p>Añadir un nuevo cliente:</p>
<form action="/new_cliente" method="POST">
    <input type="text" size="65" maxlength="100" name="Cliente">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Los clientes actuales son los siguientes:</p>
<table border="1">
    <tr>
        <th>DNI</th>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Direccion</th>
        <th colspan="2">Acciones</th>
    </tr>
    %for row in rows:
    <tr>
        %for i in range(4):
            <td>{{row[i]}}</td>
        %end
        <td>
            <form action="/edit_cliente/{{row[0]}}" method="GET">
                <input type="submit" name="edit" value="Editar">
            </form>
        </td>
        <td>
            <form action="/delete_cliente/{{row[0]}}" method="GET">
                <input type="submit" name="delete" value="Borrar">
            </form>
        </td>
    </tr>
    %end
</table>
% include('footer.tpl')