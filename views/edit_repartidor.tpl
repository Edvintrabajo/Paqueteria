% include('header.tpl', title = "Editar repartidor")
<div class="bodyglobal">
  <div class="contenedor-edit">
    <div class="contenedor-todo">
        <p>Editar repartidor {{no}}:</p>
        <form class="form1 formedit" action="/edit_repartidor/{{no}}" method="POST">
            <input type="text" placeholder="Nombre" size="10" name="NombreRepartidor">
          <br>
          <input type="submit" name="save" value="Guardar">
          <input type="submit" name="cancel" value="Cancelar">
        </form>   
    </div>
  </div>
</div>
% include('footer.tpl')