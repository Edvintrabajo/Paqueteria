% include('header.tpl', title = "Borrar pedido")
<div class="contenedor-delete">

  <p>Borrar pedido con el ID = {{no}}</p>
  <form action="/delete_pedido/{{no}}" method="POST">
    <p>Hac click para confirmar que deseas eliminar el pedido: </p>
    <p><b>{{old[0]}}</b></p>

    <input type="submit" name="delete" value="Borrar">
    <input type="submit" name="cancel" value="Cancelar">
  </form>
</div>
% include('footer.tpl')