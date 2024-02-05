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