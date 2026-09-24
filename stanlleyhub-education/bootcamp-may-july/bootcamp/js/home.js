// home.js - protected page, logout, user info

const CURRENT_USER_KEY = 'auth_user';

function getCurrentUser() {
  const stored = localStorage.getItem(CURRENT_USER_KEY);
  return stored ? JSON.parse(stored) : null;
}

function setCurrentUser(user) {
  if (user) {
    localStorage.setItem(CURRENT_USER_KEY, JSON.stringify(user));
  } else {
    localStorage.removeItem(CURRENT_USER_KEY);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const user = getCurrentUser();
  if (!user) {
    window.location.href = 'login.html';
    return;
  }

  const userNameSpan = document.getElementById('userName');
  const userEmailSpan = document.getElementById('userEmail');
  const avatarImg = document.getElementById('avatarImg');

  if (userNameSpan) userNameSpan.textContent = user.name;
  if (userEmailSpan) userEmailSpan.textContent = user.email;
  if (avatarImg) {
    avatarImg.src = `https://ui-avatars.com/api/?background=3b82f6&color=fff&name=${encodeURIComponent(user.name)}&size=80&rounded=true`;
  }

  const logoutBtn = document.getElementById('logoutBtn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      setCurrentUser(null);
      window.location.href = 'login.html';
    });
  }
});