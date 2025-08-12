  document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("menu-toggle");
    const navbar = document.getElementById("navbar");

    toggleButton.addEventListener("click", () => {
      navbar.classList.toggle("active");
    });
  });