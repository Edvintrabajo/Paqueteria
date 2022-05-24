% include('header.tpl', title = "Editar Oficinista")

    <p>Editar Oficinista {{no}}:</p>
    <form action="/edit_oficinista/{{no}}" method="POST">
        <input type="text" placeholder="Nombre" size="10" name="Nombre">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>   

% include('footer.tpl')