const track = document.querySelector('.carousel-track');
const images = document.querySelectorAll('.carousel-image');
const prevButton = document.querySelector('.carousel-button.prev');
const nextButton = document.querySelector('.carousel-button.next');

let currentIndex = 0;

function updateCarousel() {
  const imageWidth = images[0].clientWidth;
  track.style.transform = `translateX(-${currentIndex * imageWidth}px)`;
}

nextButton.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % images.length;
  updateCarousel();
});

prevButton.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  updateCarousel();
});

window.addEventListener('resize', updateCarousel); // ajuste en cambio de tamaño
