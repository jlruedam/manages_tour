const input_value= document.getElementById("input_value");
const sale_quantity = document.getElementById("sale_quantity");
const sale_total = document.getElementById("sale_total");

const calculate_total_sale = () => {
    console.log('Total Sale');
    const value = parseFloat(input_value.value) || 0;
    const quantity = parseInt(sale_quantity.value) || 0;
    sale_total.value = value * quantity;
}

input_value.addEventListener('input', calculate_total_sale);
sale_quantity.addEventListener('input', calculate_total_sale);
sale_total.addEventListener('click', calculate_total_sale);
