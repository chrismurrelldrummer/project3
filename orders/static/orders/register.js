document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('username').onkeyup = () => {

        const un = document.getElementById('username').value;

        if (un.length > 16 || un.length < 8) {

            document.getElementById('unCheck').innerHTML = '<i class="far fa-times-circle"></i> Username does not match the requirements.';
            document.getElementById('unCheck').hidden = false;
            document.getElementById('unCheck').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else if (alphanum(un) == false) {

            document.getElementById('unCheck').innerHTML = '<i class="far fa-times-circle"></i> Username does not match the requirements.';
            document.getElementById('unCheck').hidden = false;
            document.getElementById('unCheck').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else if (caseCheck(un) == false) {

            document.getElementById('unCheck').innerHTML = '<i class="far fa-times-circle"></i> Username does not match the requirements.';
            document.getElementById('unCheck').hidden = false;
            document.getElementById('unCheck').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else {

            document.getElementById('unCheck').innerHTML = '<i class="far fa-check-circle"></i> Username meets the requirements';
            document.getElementById('unCheck').hidden = false;
            document.getElementById('unCheck').className = 'alert alert-success';
            document.getElementById('register').disabled = false;
        }
    }

    document.getElementById('password').onkeyup = () => {

        const pw = document.getElementById('password').value;

        if (pw.length > 16 || pw.length < 8) {

            document.getElementById('pwCheck').innerHTML = '<i class="far fa-times-circle"></i> Password does not match the requirements.';
            document.getElementById('pwCheck').hidden = false;
            document.getElementById('pwCheck').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else if (alphanum(pw) == false) {

            document.getElementById('pwCheck').innerHTML = '<i class="far fa-times-circle"></i> Password does not match the requirements.';
            document.getElementById('pwCheck').hidden = false;
            document.getElementById('pwCheck').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else if (caseCheck(pw) == false) {

            document.getElementById('pwCheck').innerHTML = '<i class="far fa-times-circle"></i> Password does not match the requirements.';
            document.getElementById('pwCheck').hidden = false;
            document.getElementById('pwCheck').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else {

            document.getElementById('pwCheck').innerHTML = '<i class="far fa-check-circle"></i> Password meets the requirements';
            document.getElementById('pwCheck').hidden = false;
            document.getElementById('pwCheck').className = 'alert alert-success';
            document.getElementById('register').disabled = false;
        }
    }

    document.getElementById('confirm').onkeyup = () => {

        const pw = document.getElementById('password').value;
        const con = document.getElementById('confirm').value;

        if (pw != con) {

            document.getElementById('pwMatch').innerHTML = '<i class="far fa-times-circle"></i> Oops! These passwords don\'t match.';
            document.getElementById('pwMatch').hidden = false;
            document.getElementById('pwMatch').className = 'alert alert-danger';
            document.getElementById('register').disabled = true;

        } else {

            document.getElementById('pwMatch').innerHTML = '<i class="far fa-check-circle"></i> Passwords match.';
            document.getElementById('pwMatch').hidden = false;
            document.getElementById('pwMatch').className = 'alert alert-success';
            document.getElementById('register').disabled = false;
        }
    }
});

function alphanum(txt) {

    let allow = /^[0-9a-zA-Z]+$/;
    return allow.test(txt);
};

function caseCheck(txt) {
    
    let upcount = 0;
    let lowcount = 0;

    for (i = 0; i < txt.length; i++) {

        let c = txt[i];

        if (isNaN(c)) {

            if (c == c.toUpperCase()) {
                upcount++;
            }
            if (c == c.toLowerCase()) {
                lowcount++;
            }
        }
    }

    if (upcount >= 1 && lowcount >= 1) {
        return true;
    } else {
        return false;
    }
};