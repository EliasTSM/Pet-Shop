function mostarSenha() {
    var inputPwd = document.getElementById("senha");
    var btnShowPwd = document.getElementById("btn-senha");

    console.log(inputPwd.type)

    if(inputPwd.type === 'password'){
        inputPwd.setAttribute('type', 'text')
        btnShowPwd.classList.replace('fa-eye', 'fa-eye-slash')
    } else {
        inputPwd.setAttribute('type', 'password')
        btnShowPwd.classList.replace('fa-eye-slash', 'fa-eye')
    }
}

const abrirModal = document.querySelector(".add-left")
const modal = document.querySelector("dialog")

abrirModal.onclick = function (){
    modal.showModal()
}