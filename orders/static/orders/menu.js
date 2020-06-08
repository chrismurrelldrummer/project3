document.addEventListener('DOMContentLoaded', () => {

    // sub extras price change
    document.querySelectorAll('input[type="checkbox"]').forEach((input) => {

        input.onchange = () => {

            const row = input.parentNode.parentNode.parentNode.id.replace('tops', '');

            if (input.checked == true) {
                
                let sm = parseFloat(document.querySelector(`#subsmplace${row}`).value);
                let lg = parseFloat(document.querySelector(`#sublgplace${row}`).value);

                sm += 0.50;
                lg += 0.50;

                document.querySelector(`#subsmplace${row}`).value = sm.toFixed(2);
                document.querySelector(`#sublgplace${row}`).value = lg.toFixed(2);

                document.querySelector(`#subsmplace${row}`).innerHTML = `+ $${sm.toFixed(2)}`;
                document.querySelector(`#sublgplace${row}`).innerHTML = `+ $${lg.toFixed(2)}`;
            } else {

                let sm = parseFloat(document.querySelector(`#subsmplace${row}`).value);
                let lg = parseFloat(document.querySelector(`#sublgplace${row}`).value);

                sm -= 0.50;
                lg -= 0.50;

                document.querySelector(`#subsmplace${row}`).value = sm.toFixed(2);
                document.querySelector(`#sublgplace${row}`).value = lg.toFixed(2);

                document.querySelector(`#subsmplace${row}`).innerHTML = `+ $${sm.toFixed(2)}`;
                document.querySelector(`#sublgplace${row}`).innerHTML = `+ $${lg.toFixed(2)}`;
            }
        }
    });

    // size toggles
    document.querySelectorAll('#pizlarge').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#pizsmplace${row}`).hidden = true;
            document.querySelector(`#pizlgplace${row}`).hidden = false;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#pizsmall').className = 'btn btn-info';
            document.querySelector('#pizsmall').checked = false;
        }
    });

    document.querySelectorAll('#pizsmall').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#pizsmplace${row}`).hidden = false;
            document.querySelector(`#pizlgplace${row}`).hidden = true;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#pizlarge').className = 'btn btn-info';
            document.querySelector('#pizlarge').checked = false;
        }
    });

    document.querySelectorAll('#sublarge').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#subsmplace${row}`).hidden = true;
            document.querySelector(`#sublgplace${row}`).hidden = false;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#subsmall').className = 'btn btn-info';
            document.querySelector('#subsmall').checked = false;
        }
    });

    document.querySelectorAll('#subsmall').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#subsmplace${row}`).hidden = false;
            document.querySelector(`#sublgplace${row}`).hidden = true;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#sublarge').className = 'btn btn-info';
            document.querySelector('#sublarge').checked = false;
        }
    });

    document.querySelectorAll('#platlarge').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#platsmplace${row}`).hidden = true;
            document.querySelector(`#platlgplace${row}`).hidden = false;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#platsmall').className = 'btn btn-info';
            document.querySelector('#platsmall').checked = false;
        }
    });

    document.querySelectorAll('#platsmall').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#platsmplace${row}`).hidden = false;
            document.querySelector(`#platlgplace${row}`).hidden = true;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#platlarge').className = 'btn btn-info';
            document.querySelector('#platlarge').checked = false;
        }
    });

    // place order buttons
    document.querySelectorAll('.smplace').forEach((button) => {

        button.onclick = () => {

            const ident = button.dataset.ident;
            const size = 'small';

            let tops = [];

            document.querySelectorAll(`#topSelect${ident}`).forEach((select) => {
                tops.push(select.selectedOptions[0].innerHTML);
            });

            data = {
                'item': button.name.replace('place', ''),
                'ident': ident,
                'size': size,
                'toppings': tops
            }

            let bask = JSON.parse(localStorage.getItem('basket'));

            if (bask == null) {
                localStorage.setItem('basket', JSON.stringify([data]));
            } else {
                bask.push(data);
                localStorage.setItem('basket', JSON.stringify(bask));
            }

            button.blur();

            let quantity = document.querySelector(`#quant${ident}`);
            quantity.innerHTML++;
            quantity.hidden = false;

        }
    });

    document.querySelectorAll('.lgplace').forEach((button) => {

        button.onclick = () => {

            const ident = button.dataset.ident;
            const size = 'large';

            let tops = [];

            document.querySelectorAll(`#topSelect${ident}`).forEach((select) => {
                tops.push(select.selectedOptions[0].innerHTML);
            });

            data = {
                'item': button.name.replace('place', ''),
                'ident': ident,
                'size': size,
                'toppings': tops
            }

            let bask = JSON.parse(localStorage.getItem('basket'));

            if (bask == null) {
                localStorage.setItem('basket', JSON.stringify([data]));
            } else {
                bask.push(data);
                localStorage.setItem('basket', JSON.stringify(bask));
            }

            button.blur();

            let quantity = document.querySelector(`#quant${ident}`);
            quantity.innerHTML++;
            quantity.hidden = false;
        }
    });

    document.querySelectorAll('.place').forEach((button) => {

        button.onclick = () => {

            const ident = button.dataset.ident;

            data = {
                'item': button.name.replace('place', ''),
                'ident': ident
            }

            let bask = JSON.parse(localStorage.getItem('basket'));

            if (bask == null) {
                localStorage.setItem('basket', JSON.stringify([data]));
            } else {
                bask.push(data);
                localStorage.setItem('basket', JSON.stringify(bask));
            }

            button.blur();
        }
    });

    // menu tabs
    document.querySelector('#pizzas').onclick = () => {

        document.querySelector('#pizzas').className = 'nav-link active';
        document.querySelector('#subs').className = 'nav-link';
        document.querySelector('#pasta').className = 'nav-link';
        document.querySelector('#salads').className = 'nav-link';
        document.querySelector('#platters').className = 'nav-link';

        document.querySelector('#pizzaBody').hidden = false;
        document.querySelector('#subBody').hidden = true;
        document.querySelector('#pastaBody').hidden = true;
        document.querySelector('#saladBody').hidden = true;
        document.querySelector('#platterBody').hidden = true;

        document.querySelector('#pizzas').blur();
    };

    document.querySelector('#subs').onclick = () => {

        document.querySelector('#pizzas').className = 'nav-link';
        document.querySelector('#subs').className = 'nav-link active';
        document.querySelector('#pasta').className = 'nav-link';
        document.querySelector('#salads').className = 'nav-link';
        document.querySelector('#platters').className = 'nav-link';

        document.querySelector('#pizzaBody').hidden = true;
        document.querySelector('#subBody').hidden = false;
        document.querySelector('#pastaBody').hidden = true;
        document.querySelector('#saladBody').hidden = true;
        document.querySelector('#platterBody').hidden = true;

        document.querySelector('#subs').blur();
    };

    document.querySelector('#pasta').onclick = () => {

        document.querySelector('#pizzas').className = 'nav-link';
        document.querySelector('#subs').className = 'nav-link';
        document.querySelector('#pasta').className = 'nav-link active';
        document.querySelector('#salads').className = 'nav-link';
        document.querySelector('#platters').className = 'nav-link';

        document.querySelector('#pizzaBody').hidden = true;
        document.querySelector('#subBody').hidden = true;
        document.querySelector('#pastaBody').hidden = false;
        document.querySelector('#saladBody').hidden = true;
        document.querySelector('#platterBody').hidden = true;

        document.querySelector('#pasta').blur();
    };

    document.querySelector('#salads').onclick = () => {

        document.querySelector('#pizzas').className = 'nav-link';
        document.querySelector('#subs').className = 'nav-link';
        document.querySelector('#pasta').className = 'nav-link';
        document.querySelector('#salads').className = 'nav-link active';
        document.querySelector('#platters').className = 'nav-link';

        document.querySelector('#pizzaBody').hidden = true;
        document.querySelector('#subBody').hidden = true;
        document.querySelector('#pastaBody').hidden = true;
        document.querySelector('#saladBody').hidden = false;
        document.querySelector('#platterBody').hidden = true;

        document.querySelector('#salads').blur();
    };

    document.querySelector('#platters').onclick = () => {

        document.querySelector('#pizzas').className = 'nav-link';
        document.querySelector('#subs').className = 'nav-link';
        document.querySelector('#pasta').className = 'nav-link';
        document.querySelector('#salads').className = 'nav-link';
        document.querySelector('#platters').className = 'nav-link active';

        document.querySelector('#pizzaBody').hidden = true;
        document.querySelector('#subBody').hidden = true;
        document.querySelector('#pastaBody').hidden = true;
        document.querySelector('#saladBody').hidden = true;
        document.querySelector('#platterBody').hidden = false;

        document.querySelector('#platters').blur();
    };
});