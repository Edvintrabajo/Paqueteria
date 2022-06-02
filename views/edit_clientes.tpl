% include('header.tpl', title = "Editar cliente")
<div class="bodyglobal">
  <div class="contenedor-edit">
    <p>Editar cliente {{no}}:</p>
    <form class="form1 formedit" action="/edit_cliente/{{no}}" method="POST">
        <input type="text" placeholder="Nombre" size="10" name="Nombre">
        <input type="text" placeholder="Apellido" size="10" name="Apellido">
        <input type="text" placeholder="Direccion" size="20" name="Direccion">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>  
  </div>
</div> 
% include('footer.tpl')