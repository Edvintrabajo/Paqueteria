% include('header.tpl', title = "Editar producto")

    <p>Editar producto {{no}}:</p>
    <form action="/edit_producto/{{no}}" method="POST">
        <input type="text" placeholder="Nombre" size="10" name="Nombre">
        <input type="text" placeholder="Cantidad" size="10" name="Cantidad">
        <input type="text" placeholder="Peso" size="20" name="Peso">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>   

% include('footer.tpl')