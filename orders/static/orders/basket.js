document.addEventListener('DOMContentLoaded', () => {

    let bask = JSON.parse(localStorage.getItem('basket'));
    let div = document.querySelector('#basketList');

    if (bask == null) {
        div.innerHTML = 'You do not have any items in your basket!';
        document.querySelector('#placeOrder').disabled = true;
        document.querySelector('#deleteOrder').disabled = true;
    } else {

        for (i in bask) {

            let div = document.createElement("div");
            div.setAttribute('className', 'input-group');
            div.setAttribute('id', `item${i}`);
            div.setAttribute('name', `item${i}`);

            if (bask[i]['toppings'] == '') {
                // Create template
                const template1 = Handlebars.compile(document.querySelector('#basketItem1').innerHTML);

                // Add to DOM.
                const content = template1({
                    'ident': bask[i]['ident'],
                    'item': bask[i]['item'],
                    'type': bask[i]['type'],
                    'category': bask[i]['category'],
                    'size': bask[i]['size'],
                    'toppings': 'No extra toppings.',
                    'price': bask[i]['price']
                });

                document.querySelector('#basketList').innerHTML += content;

            } else {
                // Create template
                const template1 = Handlebars.compile(document.querySelector('#basketItem1').innerHTML);

                let toppings = '';

                for (k in bask[i]['toppings']) {
                    toppings += `${bask[i]['toppings'][k]}`;
                    if (k >= 0 && k < (bask[i]['toppings'].length - 1)) {
                        toppings += ', ';
                    }
                }

                // Add to DOM.
                const content = template1({
                    'ident': bask[i]['ident'],
                    'item': bask[i]['item'],
                    'type': bask[i]['type'],
                    'category': bask[i]['category'],
                    'size': bask[i]['size'],
                    'toppings': toppings,
                    'price': bask[i]['price']
                });

                document.querySelector('#basketList').innerHTML += content;
            }

        }
    }

    document.querySelector('#placeOrder').onclick = (button) => {

        document.querySelector('#hiddenData').value = localStorage.getItem('basket');
        localStorage.removeItem('basket');
    };

    document.querySelector('#deleteOrder').onclick = (button) => {

        document.querySelector('#basketList').innerHTML = 'You do not have any items in your basket!';
        localStorage.removeItem('basket');
        document.querySelector('#placeOrder').disabled = true;
        document.querySelector('#deleteOrder').disabled = true;
        document.querySelector('#confirmation').hidden = false;
        document.querySelector('#confirmation').innerHTML = 'Successfully removed all items from basket!';
    };
});