% include('header.tpl', title = "Editar pedido")

    <p>Editar pedido {{no}}:</p>
    <form class="form1 formedit" action="/edit_pedido/{{no}}" method="POST">
        <input type="text" placeholder="Peso" size="10" maxlength="100" name="Peso">
        <input type="text" placeholder="Coste" size="10" maxlength="100" name="Coste">
        <input type="text" placeholder="Distancia" size="10" maxlength="100" name="Distancia">
        <input type="text" placeholder="Direccion" size="10" maxlength="100" name="Direccion">
        <input type="text" placeholder="Estado" size="10" maxlength="100" name="Estado">
        <input type="text" placeholder="DNI Repartidor" size="10" maxlength="100" name="DNIRepartidor">
        <input type="text" placeholder="DNI Cliente" size="10" maxlength="100" name="DNICliente">
      <br>
      <input type="submit" name="save" value="Guardar">
      <input type="submit" name="cancel" value="Cancelar">
    </form>   

% include('footer.tpl')