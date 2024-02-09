const titulos = document.querySelectorAll('.card h4')
for (let h4 of titulos){
    h4.innerHTML = h4.innerHTML.substring(0, 30) + '...'
}

const precos = document.querySelectorAll('.preco')
const divisao = document.querySelectorAll('.divisao')
for (let i = 0; i < precos.length; i++){
    const valor = parseFloat(precos[i].innerHTML.substring(2).replace(",", "."))
    if(valor > 50) {
        const dividido = valor / 3
        divisao[i].innerHTML = "ou 3x de R$ " +  dividido.toFixed(2)
    } else {
        divisao[i].innerHTML = "ou 1x de R$ " +  valor
    }
}

const imgs = document.getElementById("img")
const img = document.querySelectorAll("#img img")

let idx = 0

function carrossel(){
    idx++

    if(idx > img.length - 1){
        idx = 0
    }

    imgs.style.transform = `translateX(${-idx * 100}%)`
}

setInterval(carrossel, 5000)

function filtrar() {
    var input, filter, ul, li, a, i, txtValue, span, count=0

    input = document.getElementById('inputBusca');
    ul = document.getElementById('listaProdutos');

    filter = input.value.toUpperCase();


    li = ul.getElementsByTagName("li");
    
    for(i = 0; i < li.length; i++){
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;

        if(txtValue.toUpperCase().indexOf(filter) > -1){
            li[i].style.display = "";
            count++
            span = li[i].querySelector(".item-nome")
            if(span){
                span.innerHTML = txtValue.replace(new RegExp(filter, "gi"), (match)=> {
                    return "<strong>" + match + "</strong>";
                })
            }
        }else {
            li[i].style.display = "none";
        }
    }

    if(filter.length == 0){
        ul.style.display = "none"
    }else {
        ul.style.display = "block"
    }
}