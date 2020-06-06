document.addEventListener('DOMContentLoaded', () => {


    document.querySelectorAll('#large').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#smplace${row}`).hidden = true;
            document.querySelector(`#lgplace${row}`).hidden = false;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#small').className = 'btn btn-info';
            document.querySelector('#small').checked = false;
        }
    });

    document.querySelectorAll('#small').forEach((input) => {

        input.onchange = () => {

            const row = input.dataset.row;

            document.querySelector(`#smplace${row}`).hidden = false;
            document.querySelector(`#lgplace${row}`).hidden = true;
            input.className = 'btn btn-info active';
            input.checked = true;
            document.querySelector('#large').className = 'btn btn-info';
            document.querySelector('#large').checked = false;
        }
    });

    document.querySelectorAll('.smplace').forEach((button) => {

        button.onclick = () => {

            const ident = button.dataset.ident;
            const size = 'small';

            data = JSON.stringify({
                'ident': ident,
                'size': size
            })
            localStorage.setItem('basket', data);
        }
    });

    document.querySelector('#pizzas').onclick = () => {

        document.querySelector('#pizzas').className = 'nav-link active';
        document.querySelector('#subs').className = 'nav-link';
        document.querySelector('#pasta').className = 'nav-link';
        document.querySelector('#pizzaBody').hidden = false;
        document.querySelector('#subBody').hidden = true;
        document.querySelector('#pastaBody').hidden = true;

        document.querySelector('#pizzas').blur();
    };

    document.querySelector('#subs').onclick = () => {

        document.querySelector('#subs').className = 'nav-link active';
        document.querySelector('#pizzas').className = 'nav-link';
        document.querySelector('#pasta').className = 'nav-link';
        document.querySelector('#pizzaBody').hidden = true;
        document.querySelector('#subBody').hidden = false;
        document.querySelector('#pastaBody').hidden = true;

        document.querySelector('#subs').blur();
    };

    document.querySelector('#pasta').onclick = () => {

        document.querySelector('#pasta').className = 'nav-link active';
        document.querySelector('#subs').className = 'nav-link';
        document.querySelector('#pizzas').className = 'nav-link';
        document.querySelector('#pizzaBody').hidden = true;
        document.querySelector('#subBody').hidden = true;
        document.querySelector('#pastaBody').hidden = false;

        document.querySelector('#pasta').blur();
    };
});