% include('header.tpl', title = "productos")

<div class="contenedor-nav">
    <nav class="nav">
        <a href="/" class="nombre-empresa">Paqueteria</a>
    </nav>
</div>

<div class="contenedor-todo">
    <p>Añadir un nuevo producto:</p>
    <form class="form1" action="/producto" method="POST">
        <input type="text" placeholder="Nombre" size="10" maxlength="100" name="Nombre">
        <input type="text" placeholder="Cantidad" size="10" maxlength="100" name="Cantidad">
        <input type="text" placeholder="Peso" size="10" maxlength="100" name="Peso">
        <input type="submit" name="save" value="Añadir">
    </form>
    <p>Los productos actuales son los siguientes:</p>

    <div class="contenedor-tabla">
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
    </div>

</div>
% include('footer.tpl')