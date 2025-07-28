const input_tour = document.getElementById('input_tour');



const select_tour = (name_tour) => {
    console.log('Select_tour:', name_tour);
    input_tour.value = name_tour;
    modalTour.style.display = "None";
}