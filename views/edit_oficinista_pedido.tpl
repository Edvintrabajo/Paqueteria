% include('header.tpl', title = "Editar Oficinista")

    <p>Editar asignación de Oficinista a pedido {{no}}:</p>
    <form action="/edit_oficinista_pedido/{{no}}" method="POST">
        <input type="text" placeholder="ID Oficinista" size="10" name="IDOficinista">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>   

% include('footer.tpl')