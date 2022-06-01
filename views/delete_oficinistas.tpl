% include('header.tpl', title = "Borrar Oficinista")
<div class="contenedor-delete">
  <p>Borrar Oficinista con el DNI = {{no}}</p>
  <form action="/delete_oficinista/{{no}}" method="POST">
    <p>Hac click para confirmar que deseas eliminar el oficinista: </p>
    <p><b>{{old[0]}}</b></p>

    <input type="submit" name="delete" value="Borrar">
    <input type="submit" name="cancel" value="Cancelar">
  </form>
</div>
% include('footer.tpl')