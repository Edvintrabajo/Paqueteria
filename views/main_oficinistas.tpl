% include('header.tpl', title = "Oficinistas")
<p>Añadir un nuevo oficinista:</p>
<form action="/new_oficinista" method="POST">
    <input type="text" size="65" maxlength="100" name="Oficinista">
    <input type="submit" name="save" value="Añadir">
</form>
<p>Los oficinistas actuales son los siguientes:</p>
<table border="1">
    <tr>
        <th>ID</th>
        <th>Nombre</th>
        <th colspan="2">Acciones</th>
    </tr>
    %for row in rows:
    <tr>
        %for i in range(2):
            <td>{{row[i]}}</td>
        %end
        <td>
            <form action="/edit_oficinista/{{row[0]}}" method="GET">
                <input type="submit" name="edit" value="Editar">
            </form>
        </td>
        <td>
            <form action="/delete_oficinista/{{row[0]}}" method="GET">
                <input type="submit" name="delete" value="Borrar">
            </form>
        </td>
    </tr>
    %end
</table>
% include('footer.tpl')