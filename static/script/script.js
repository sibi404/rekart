const phoneMenu = document.querySelector('#phone-menu');
const headLogin = document.querySelector('#head-login');
const burger = document.querySelector('#burger');

burger.addEventListener('click',() => {
    if(phoneMenu.classList.contains('hidden')){
        phoneMenu.classList.remove('hidden');
    }else{
        phoneMenu.classList.add('hidden');
    }
})