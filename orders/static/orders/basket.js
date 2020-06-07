document.addEventListener('DOMContentLoaded', () => {

    let bask = JSON.parse(localStorage.getItem('basket'));

    let div = document.querySelector('#basketList');

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
                'size': bask[i]['size'],
                'toppings': 'No extra toppings.'
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
                'size': bask[i]['size'],
                'toppings': toppings
            });

            document.querySelector('#basketList').innerHTML += content;
        }

    }
});