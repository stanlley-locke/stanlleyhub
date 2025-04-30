document.addEventListener("DOMContentLoaded", () => {
  // Mobile menu toggle
  const mobileMenuToggle = document.querySelector(".mobile-menu-toggle")
  const mainNav = document.querySelector(".main-nav")

  if (mobileMenuToggle && mainNav) {
    mobileMenuToggle.addEventListener("click", function () {
      mainNav.classList.toggle("active")
      this.classList.toggle("active")
    })
  }

  // Password toggle functionality
  const passwordToggles = document.querySelectorAll(".password-toggle")

  passwordToggles.forEach((toggle) => {
    toggle.addEventListener("click", function () {
      const input = this.previousElementSibling
      const type = input.getAttribute("type") === "password" ? "text" : "password"
      input.setAttribute("type", type)
      this.textContent = type === "password" ? "Show" : "Hide"
    })
  })

  // Flash message auto-dismiss
  const flashMessages = document.querySelectorAll(".flash-message")

  flashMessages.forEach((message) => {
    setTimeout(() => {
      message.style.opacity = "0"
      setTimeout(() => {
        message.style.display = "none"
      }, 300)
    }, 5000)
  })
})
