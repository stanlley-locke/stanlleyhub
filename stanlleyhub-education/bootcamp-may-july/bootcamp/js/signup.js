// signup.js - separate logic for signup

const USERS_KEY = 'app_users';

function getUsers() {
  const stored = localStorage.getItem(USERS_KEY);
  return stored ? JSON.parse(stored) : [];
}

function saveUsers(users) {
  localStorage.setItem(USERS_KEY, JSON.stringify(users));
}

function showMessage(elementId, message, type) {
  const msgDiv = document.getElementById(elementId);
  if (!msgDiv) return;
  msgDiv.textContent = message;
  msgDiv.className = 'message-banner ' + type;
  msgDiv.style.display = 'block';
  setTimeout(() => {
    msgDiv.style.display = 'none';
  }, 4000);
}

window.togglePassword = function(fieldId) {
  const field = document.getElementById(fieldId);
  if (!field) return;
  const iconSpan = field.parentElement.querySelector('.toggle-pw i');
  if (field.type === 'password') {
    field.type = 'text';
    iconSpan.classList.remove('fa-eye-slash');
    iconSpan.classList.add('fa-eye');
  } else {
    field.type = 'password';
    iconSpan.classList.remove('fa-eye');
    iconSpan.classList.add('fa-eye-slash');
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('signupForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('signupName').value.trim();
    const email = document.getElementById('signupEmail').value.trim();
    const password = document.getElementById('signupPassword').value;
    const confirm = document.getElementById('signupConfirm').value;

    if (!name || !email || !password || !confirm) {
      showMessage('signupMessage', 'All fields are required.', 'error');
      return;
    }
    if (password !== confirm) {
      showMessage('signupMessage', 'Passwords do not match.', 'error');
      return;
    }
    if (password.length < 6) {
      showMessage('signupMessage', 'Password must be at least 6 characters.', 'error');
      return;
    }

    const users = getUsers();
    if (users.find(u => u.email === email)) {
      showMessage('signupMessage', 'Email already registered. Please log in.', 'error');
      return;
    }

    const newUser = {
      id: Date.now().toString(),
      name: name,
      email: email,
      password: password
    };
    users.push(newUser);
    saveUsers(users);
    showMessage('signupMessage', 'Account created successfully! Redirecting to login...', 'success');
    setTimeout(() => {
      window.location.href = 'login.html';
    }, 1500);
  });
});