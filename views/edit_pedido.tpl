% include('header.tpl', title = "Editar pedido")
<div class="bodyglobal">
  <div class="contenedor-edit">
    <p>Editar pedido {{no}}:</p>
    <form class="form1 formedit" action="/edit_pedido/{{no}}" method="POST">
        <input type="text" placeholder="Estado" size="10" maxlength="100" name="Estado">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>   
  </div>
</div>
% include('footer.tpl')