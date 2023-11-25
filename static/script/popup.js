const popup = document.getElementById("popup");



function openPopup(){
    popup.classList.add('open-popup');
}

function closePopup(){
    popup.classList.remove('open-popup');
}

//  To close popup window with ESC key
document.onkeydown = function(event){
    event = event || window.event;
    var isEscape = false;
    if ("key" in event){
        isEscape = (event.key === 'Escape');
    } else {
        isEscape = (event.keyCode === 27);
    }
    if (isEscape){
        closePopup();
    }
}