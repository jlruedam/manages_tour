const input_tour = document.getElementById('input_tour');
const price_sugested = document.getElementById('price_sugested');
// const sale_quantity = document.getElementById('sale_quantity');


const select_tour = (name_tour, price) => {
    console.log('Select_tour:', name_tour);
    input_tour.value = name_tour;
    input_value.value = price;
    price_sugested.value = price;
    // sale_quantity.value = 1;
    modalTour.style.display = "None";
}