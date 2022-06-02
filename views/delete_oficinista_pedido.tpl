% include('header.tpl', title = "Borrar Oficinista-Pedido")
<div class="bodyglobal">
  <div class="contenedor-delete">
    <p>Borrar Oficinista nº = {{no}}</p>
    <form class="input-delete" action="/delete_oficinista_pedido/{{no}}" method="POST">
      <p>Hac click para confirmar que deseas eliminar la asignacion de Pedido: </p>
      <p><b>{{old[0]}}</b></p>

      <input class="input1" type="submit" name="delete" value="Borrar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>
  </div>
</div>
% include('footer.tpl')