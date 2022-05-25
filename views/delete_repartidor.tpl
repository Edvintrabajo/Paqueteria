% include('header.tpl', title = "Borrar repartidor")
<p>Borrar repartidor con el DNI = {{no}}</p>
<form action="/delete_repartidor/{{no}}" method="POST">
  <p>Hac click para confirmar que deseas eliminar el repartidor: </p>
  <p><b>{{old[0]}}</b></p>

  <input type="submit" name="delete" value="Borrar">
  <input type="submit" name="cancel" value="Cancelar">
</form>
% include('footer.tpl')