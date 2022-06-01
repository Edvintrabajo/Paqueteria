% include('header.tpl', title = "Oficinistas")

<div class="contenedor-nav">
    <nav class="nav">
        <a href="/" class="nombre-empresa">Paqueteria</a>
    </nav>
</div>

<div class="contenedor-todo">
    <p>Añadir un nuevo oficinista:</p>
    <form class="form1" action="/oficinista" method="POST">
        <input type="text" placeholder="Nombre" size="20" maxlength="100" name="Nombre">
        <input type="submit" name="save" value="Añadir">
    </form>
    <p>Los oficinistas actuales son los siguientes:</p>

    <div class="contenedor-tabla">
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
    </div>

</div>
% include('footer.tpl')