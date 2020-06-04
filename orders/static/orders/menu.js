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
});