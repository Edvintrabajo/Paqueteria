% include('header.tpl', title = "repartidores")
<p>Añadir un nuevo repartidor:</p>
<form action="/new_repartidor" method="POST">
    <input type="text" placeholder="DNI" size="10" maxlength="100" name="DNI">
    <input type="text" placeholder="Nombre" size="10" maxlength="100" name="Nombre">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Los repartidores actuales son los siguientes:</p>
<table border="1">
    <tr>
        <th>DNI</th>
        <th>Nombre</th>
        <th colspan="2">Acciones</th>
    </tr>
    %for row in rows:
    <tr>
        %for i in range(2):
            <td>{{row[i]}}</td>
        %end
        <td>
            <form action="/edit_repartidor/{{row[0]}}" method="GET">
                <input type="submit" name="edit" value="Editar">
            </form>
        </td>
        <td>
            <form action="/delete_repartidor/{{row[0]}}" method="GET">
                <input type="submit" name="delete" value="Borrar">
            </form>
        </td>
    </tr>
    %end
</table>
% include('footer.tpl')