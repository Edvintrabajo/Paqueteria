% include('header.tpl', title = "Borrar Oficinista-Pedido")
<p>Borrar Oficinista nº = {{no}}</p>
<form action="/delete_oficinista_pedido/{{no}}" method="POST">
  <p>Hac click para confirmar que deseas eliminar la asignacion de Pedido: </p>
  <p><b>{{old[0]}}</b></p>

  <input type="submit" name="delete" value="Borrar">
  <input type="submit" name="cancel" value="Cancelar">
</form>
% include('footer.tpl')