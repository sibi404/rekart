// const quantity = document.getElementById('item_quantity');

const total = document.getElementById('total');
const subTotal = document.getElementById('sub-total');


function quantityChange(id,action,event){
    if (action == 1){
        var url = `http://127.0.0.1:8000/cart/addCount/${id}`;
        var quantity = event.srcElement.previousElementSibling;
    }else if (action == 0){
        var url = `http://127.0.0.1:8000/cart/reduceCount/${id}`;
        var quantity = event.srcElement.nextElementSibling;
    }

    var parent = event.srcElement;
    console.log(parent);
    
    fetch(url)
    .then((resp) => {
        resp.json()
        .then(function(data){
            if (data.quantity == 'error'){
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "No more stock available!",
                    confirmButtonColor: '#1F6B48',
                    });
            }else if(data.quantity == 'empty'){
                /*
                console.log("Empty reached\n");
                
                while(!parent.classList.contains('parent')){
                    parent = parent.parentNode;
                }
                parent.remove();
                console.log("Parent removed\n");
                */
                location.reload();
            }else{
                quantity.innerText = data.quantity;

                const price = parseFloat(data.price);
                const subTotalVal = parseFloat(subTotal.innerText);
                const totalVal = parseFloat(total.innerHTML);

                if (action == 1){
                    subTotal.innerText = (subTotalVal + price).toFixed(2);
                    total.innerText = (totalVal + price).toFixed(2);
                }else{
                    subTotal.innerText = (subTotalVal - price).toFixed(2);
                    total.innerText = (totalVal - price).toFixed(2);
                }
            }
            
            
        })
    })
}