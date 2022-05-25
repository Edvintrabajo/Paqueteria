% include('header.tpl', title = "Borrar producto")
<p>Borrar producto con el ID = {{no}}</p>
<form action="/delete_producto/{{no}}" method="POST">
  <p>Hac click para confirmar que deseas eliminar el producto: </p>
  <p><b>{{old[0]}}</b></p>

  <input type="submit" name="delete" value="Borrar">
  <input type="submit" name="cancel" value="Cancelar">
</form>
% include('footer.tpl')