% include('header.tpl', title = "Editar Oficinista")
<div class="bodyglobal">
  <div class="contenedor-edit">
      <p>Editar asignación de Oficinista a pedido {{no}}:</p>
      <form class="form1 formedit" action="/edit_oficinista_pedido/{{no}}" method="POST">
          <input type="text" placeholder="ID Oficinista" size="10" name="IDOficinista">
        <br>
        <input type="submit" name="save" value="Guardar">
        <input type="submit" name="cancel" value="Cancelar">
      </form>   
  </div>
</div>
% include('footer.tpl')