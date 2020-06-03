document.addEventListener('DOMContentLoaded', () => {


    document.querySelectorAll('#large').forEach((input) => {

        input.onchange = () => {

            document.querySelector('#smplace').hidden = true;
            document.querySelector('#lgplace').hidden = false;
        }
    });

    document.querySelectorAll('#small').forEach((input) => {

        input.onchange = () => {

            document.querySelector('#smplace').hidden = false;
            document.querySelector('#lgplace').hidden = true;
        }
    });
});