const formInputMethod = document.getElementsByName("input-method")
const fileMethod = document.getElementById('file-chosen')
const textMethod = document.getElementById('text-chosen')

const handleFormInput = e => {
    if(e.target.value === 'text'){
        textMethod.style.display = 'block'
        fileMethod.style.display = 'none'
        textMethod.querySelector('textarea').required = true
        fileMethod.querySelector('input').required = false
        if(document.getElementById('temp-placement')){
            textarea = document.getElementById('temp-placement')
            textarea.style.display = 'none'
        }
    }
    if(e.target.value === 'file') {
        fileMethod.style.display = 'block'
        textMethod.style.display = 'none'
        fileMethod.querySelector('input').required = true
        textMethod.querySelector('textarea').required = false
        if(document.getElementById('temp-placement')){
            textarea = document.getElementById('temp-placement')
            textarea.style.display = 'block'
        }
    }
}


formInputMethod.forEach(input => input.addEventListener('click', handleFormInput))


const process = (text) => {
    let textarea
    if(document.getElementById('temp-placement')){
        textarea = document.getElementById('temp-placement')
        textarea.textContent = text
    }
    else {
        textarea = document.createElement('textarea')
        textarea.setAttribute('id', 'temp-placement')
        textarea.setAttribute('name', 'input-text')
        textarea.textContent = text
        document.getElementById('before-parsed').appendChild(textarea)
    }
}

$(document).ready(() => {
    $('[data-toggle="tooltip"]').tooltip()
})