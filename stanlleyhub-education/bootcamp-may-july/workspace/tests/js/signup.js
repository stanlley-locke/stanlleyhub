//sighup.js 
const USERS_KEY = 'app_users';

function getUsers() {
    const stored = localStorage.getItem(USERS_KEY);
    return stored ? JSON.parse(stored) : [];
}

function saveUSers(users){
    localStorage.setItem(USERS_KEY, JSON.stringify(users))
}

function showMessage(elementId, message, type) {
    const msgDiv = document.getElementById(elementId);
    if (!msgDiv) return;
    msgDiv.textContent = message;
    msgDiv.className = 'message-banner' + type;
    msgDiv.style.display = 'block';
    setTimeout(() => {
        message.style.display = 'none';
    }, 4000);
}

document.addEventListener('DOMContentLoaded', () => {
    //initializing form listener
    const form = document.getElementById('signupform');
    if (!form) return;

    //form submision trigger
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        //extract the form data
        const name = document.getElementById('sighnupName').value.trim();
        const email = document.getElementById('sighnupEmail').value.trim();
        const password = document.getElementById('sighnupPassword').value;
        const confirm = document.getElementById('sighnupConfirm').value;

        //validating inputs
        if(!name || !email || !password || !confirm ){
            showMessage('sighnupMessage', 'All fields are required', 'error');
            return;
        }

        const users = getUsers();
        if (users.find(u => u.email === email)) {
            showMessage('sighnupMessage', 'Email already registered. Please log in', 'error');
            return
        }

        const newUser = {
            id: Date.now().toString(),
            name: name,
            email: email,
            password: password
        };

        users.push(newUser);
        saveUSers(users);
        showMessage('signupMessage', 'Acount created succesfully you Login...', 'success');
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 1500);
    });
});