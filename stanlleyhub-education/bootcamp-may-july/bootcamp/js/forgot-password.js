// forgot-password.js - two-step reset

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
  const step1Div = document.getElementById('step1-email');
  const step2Div = document.getElementById('step2-reset');
  const emailInput = document.getElementById('resetEmail');
  const verifyBtn = document.getElementById('verifyEmailBtn');
  const resetForm = document.getElementById('resetPasswordForm');
  let verifiedEmail = null;

  if (verifyBtn && step1Div && step2Div) {
    verifyBtn.addEventListener('click', () => {
      const email = emailInput.value.trim();
      if (!email) {
        showMessage('forgotMessage', 'Please enter your email address.', 'error');
        return;
      }
      const users = getUsers();
      const userExists = users.find(u => u.email === email);
      if (!userExists) {
        showMessage('forgotMessage', 'No account found with this email.', 'error');
        return;
      }
      verifiedEmail = email;
      step1Div.style.display = 'none';
      step2Div.style.display = 'block';
      showMessage('forgotMessage', 'Email verified. Set your new password.', 'success');
    });
  }

  if (resetForm) {
    resetForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!verifiedEmail) {
        showMessage('forgotMessage', 'Session expired. Please restart.', 'error');
        return;
      }
      const newPw = document.getElementById('newPassword').value;
      const confirmPw = document.getElementById('confirmNewPassword').value;
      if (!newPw || !confirmPw) {
        showMessage('forgotMessage', 'Please fill both password fields.', 'error');
        return;
      }
      if (newPw !== confirmPw) {
        showMessage('forgotMessage', 'Passwords do not match.', 'error');
        return;
      }
      if (newPw.length < 6) {
        showMessage('forgotMessage', 'Password must be at least 6 characters.', 'error');
        return;
      }
      const users = getUsers();
      const userIndex = users.findIndex(u => u.email === verifiedEmail);
      if (userIndex === -1) {
        showMessage('forgotMessage', 'User not found. Please restart.', 'error');
        return;
      }
      users[userIndex].password = newPw;
      saveUsers(users);
      showMessage('forgotMessage', 'Password updated successfully. Redirecting to login...', 'success');
      setTimeout(() => {
        window.location.href = 'login.html';
      }, 1800);
    });
  }
});