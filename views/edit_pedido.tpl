% include('header.tpl', title = "Editar pedido")
<div class="bodyglobal">
  <div class="contenedor-edit">
    <p>Editar pedido {{no}}:</p>
    <form class="form1 formedit" action="/edit_pedido/{{no}}" method="POST">
      <select name="Estado">
        <option value="" selected="true" disabled>Estado</option>
        <option value="A">A (Almacenado)</option>
        <option value="S">S (Salido del Almacén)</option>
        <option value="E">E (Entregado)</option>
        <option value="I">I (Incidencia)</option>
      </select>
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>   
  </div>
</div>
% include('footer.tpl')