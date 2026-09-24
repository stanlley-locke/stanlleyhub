// login.js 

const USERS_KEY = 'app_users';
const CURRENT_USER_KEY = 'auth_user';

function getUsers() {
  const stored = localStorage.getItem(USERS_KEY);
  return stored ? JSON.parse(stored) : [];
}

function setCurrentUser(user) {
  if (user) {
    const safeUser = {
      id: user.id,
      name: user.name,
      email: user.email
    };
    localStorage.setItem(CURRENT_USER_KEY, JSON.stringify(safeUser));
  } else {
    localStorage.removeItem(CURRENT_USER_KEY);
  }
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
  const form = document.getElementById('loginForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value.trim();
    const password = document.getElementById('loginPassword').value;

    if (!email || !password) {
      showMessage('loginMessage', 'Please fill in both fields.', 'error');
      return;
    }

    const users = getUsers();
    const user = users.find(u => u.email === email && u.password === password);
    if (user) {
      setCurrentUser(user);
      showMessage('loginMessage', 'Login successful. Redirecting...', 'success');
      setTimeout(() => {
        window.location.href = 'home.html';
      }, 1200);
    } else {
      showMessage('loginMessage', 'Invalid email or password. Please try again.', 'error');
    }
  });
});