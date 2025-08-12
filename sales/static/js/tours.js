document.addEventListener("DOMContentLoaded", function () {
  const addTourModal = document.getElementById("addTourModal");
  const openModalAddTourBtn = document.getElementById("openModalAddTourBtn");
  const closeBtn = document.getElementById("closeModalAddTourBtn");

  openModalAddTourBtn.onclick = () => {
    addTourModal.style.display = "block";
  };

  closeBtn.onclick = () => {
    addTourModal.style.display = "none";
  };

  window.onclick = (event) => {
    if (event.target === addTourModal) {
      addTourModal.style.display = "none";
    }
  };
});
