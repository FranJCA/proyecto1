const ingresos = [
    new Ingreso("Salario", 2100.00),
    new Ingreso("Venta coche de pies", 1500)
];

const egresos = [
    new Egreso("Renta departamento", 900),
    new Egreso("Ropa", 400)
];
//es la que funciona como el main de un codigo normal
let cargarApp = ()=>{
    cargarCabecero();
    cargarIngresos ();
    cargarEgresos();
    console.log(totalEgresos());
}

let totalIngresos = ()=>{
    let totalIngresos = 0 ;
    for (let ingreso of ingresos) {
        totalIngresos += ingreso.valor;
    }
    return totalIngresos;
}

let totalEgresos = ()=>{
    let totalEgresos = 0 ;
    for (let egreso of egresos) {
        totalEgresos += egreso.valor;
    }
    return totalEgresos;
}




let cargarCabecero = () =>{
    let presupuesto = totalIngresos () - totalEgresos();    
    let porcentageEgreso = totalEgresos()/totalIngresos();
    document.getElementById("presupuesto").innerHTML=formatoMoneda(presupuesto);
    document.getElementById("porcentaje").innerHTML=formatoPorcentaje(porcentageEgreso);
    document.getElementById("ingresos").innerHTML=formatoMoneda(totalIngresos());
    document.getElementById("egresos").innerHTML=formatoMoneda(totalEgresos());

}

const formatoMoneda = (valor)=>{
   return  valor.toLocaleString("en-US",{style:"currency",currency:"USD",minimunFractionDigits:2});

}

const formatoPorcentaje = (valor)=>{
    return valor.toLocaleString("en-US",{style:"percent",minimunFractionDigits:2})
}

//---------------------
const cargarIngresos = ()=>{
    let ingresosHTML ="";
    for (let ingreso of ingresos) {
        ingresosHTML += crearIngresosHTML(ingreso);
    }
    document.getElementById("lista-ingresos").innerHTML = ingresosHTML;
}

const  cargarEgresos = ()=>{
    let egresosHTML ="";
    for (let egreso of egresos) {
        egresosHTML += crearEgresosHTML(egreso);
    }
    document.getElementById("lista-egresos").innerHTML = egresosHTML;
}


const crearIngresosHTML =(ingreso)=>{
    let ingresoHTML = `
    <div class="elemento limpiarEstilos">
    <div class="elemento_descripcion">${ingreso.descripcion}</div>
    <div class="derecha limpiarEstilos">
        <div class="elemento_valor">${formatoMoneda(ingreso.valor)}</div>
        <div class="elemento_eliminar">
            <button class="elemento_eliminar--btn">
                <ion-icon name="close-circle-outline" 
                onclick="eliminarIngreso(${ingreso.id})"  ></ion-icon>
            </button>
        </div>
    </div>
</div>
    `;
    return ingresoHTML;

}

const crearEgresosHTML =(egreso)=>{
    let egresoHTML = `
    <div class="elemento limpiarEstilos">
    <div class="elemento_descripcion">${egreso.descripcion} </div>
    <div class="derecha limpiarEstilos">
        <div class="elemento_valor"> ${formatoMoneda(egreso.valor)}</div>
        <div class="elemento_porcentaje">${formatoPorcentaje(egreso.valor/totalEgresos()) }</div>
        <div class="elemento_eliminar">
          <button class="elemento_eliminar--btn">
              <ion-icon name="close-circle-outline"
              onclick="eliminarEgreso(${egreso.id})"   ></ion-icon>
          </button>
      </div>
      </div>
  </div>
    `;
    return egresoHTML;

}


const eliminarIngreso = (id)=>{
              //  hace de  i
  
  let indiceEliminar =  ingresos.findIndex(ingreso => ingreso.id === id );
                        // for(let ingreso of ingresos)
                        ingresos.splice(indiceEliminar, 1);
    cargarCabecero();
    cargarIngresos();
}

const eliminarEgreso = (id)=>{
let indiceEliminar =  egresos.findIndex(egreso => egreso.id === id );
    egresos.splice(indiceEliminar, 1);
cargarCabecero();
cargarEgresos();
}


let agregarDato = ()=>{
    let forma = document.forms["forma"];
    let tipo = forma["tipo"];
    let descripcion= forma["descripcion"];
    let valor = forma["valor"];

    if (descripcion.value !== "" && valor.value !=="") {
      if (tipo.value==="ingreso") {
                                        // el+ de value hace de number(valor.value) para convertir el string en numero
          ingresos.push(new Ingreso(descripcion.value, +valor.value));
            cargarCabecero();
            cargarIngresos();
        } else if(tipo.value ==="egreso"){
          egresos.push( new Egreso(descripcion.value, Number(valor.value)));
            cargarCabecero();   
            cargarEgresos();
        }
        

    } 

}