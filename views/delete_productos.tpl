% include('header.tpl', title = "Borrar producto")
<div class="bodyglobal">
  <div class="contenedor-delete">
    <p>Borrar producto con el ID = {{no}}</p>
    <form class="input-delete" action="/delete_producto/{{no}}" method="POST">
      <p>Hac click para confirmar que deseas eliminar el producto: </p>
      <p><b>{{old[0]}}</b></p>

      <input class="input1" type="submit" name="delete" value="Borrar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>
  </div>
</div>
% include('footer.tpl')