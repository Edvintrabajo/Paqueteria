% include('header.tpl', title = "Editar Pedido-Producto")
<div class="bodyglobal">
  <div class="contenedor-edit">
    <p>Editar Pedido-Producto {{no}}:</p>
    <form class="form1 formedit" action="/edit_pedido_producto/{{no}}" method="POST">
      <input type="text" placeholder="ID Pedido" size="10" maxlength="100" name="id_pedido">
      <input type="text" placeholder="ID Producto" size="10" maxlength="100" name="id_producto">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>
  </div>
</div>

% include('footer.tpl')