% include('header.tpl', title = "Clientes")

<div class="contenedor-nav">
    <nav class="nav">
        <a href="/" class="nombre-empresa">Paqueteria</a>
    </nav>
</div>

<div class="contenedor-todo">
    <p>Añadir un nuevo cliente:</p>
    <form action="/cliente" method="POST">

        <div class="div">

            <div>
                {{ form.dni }}
            </div>

            <div>
                {{ form.nombre }}
            </div>

            <div>
                {{ form.apellido }}
            </div>
            
            <div>
                {{ form.direccion }}
            </div>

            <div>
                {{ form.save }}
            </div>

        </div>

    </form>
    <p>Los clientes actuales son los siguientes:</p>
    <div class="contenedor-tabla">
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
    </div>
</div>
% include('footer.tpl')