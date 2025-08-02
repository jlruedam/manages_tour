document.addEventListener('DOMContentLoaded', function () {
  const modalPayment = document.getElementById("modalPayment");
  const modalPaymentBtn = document.getElementById("openModalPaymentBtn");
  const closeModalPayment = document.getElementById("closeModalPayment");
  const formCreatePayment = document.getElementById("formCreatePayment");
  const totalPaymentsInput = document.getElementById("total_payments");
  const paymentsContainer = document.getElementById("paymentsContainer");

  let paymentsList = [];
  let paymentIdCounter = 1;

  // Abrir modal
  modalPaymentBtn.addEventListener("click", () => {
    modalPayment.style.display = "block";
  });

  // Cerrar modal
  closeModalPayment.addEventListener("click", () => {
    modalPayment.style.display = "none";
  });

  // Crear tarjeta HTML
  function crearTarjetaAbono(payment) {
  const card = document.createElement("div");
  card.className = "relative bg-white shadow-lg rounded-xl p-5 border border-gray-200 hover:shadow-xl transition-shadow duration-300";

  card.innerHTML = `
    <button data-id="${payment.id}" class="absolute top-3 right-3 text-red-500 hover:text-red-700 text-xl eliminar-abono" title="Eliminar abono">×</button>

    <div class="space-y-1">
      <h3 class="text-lg font-semibold text-gray-800">Abono #${payment.id}</h3>
      <p class="text-sm text-gray-600"><span class="font-medium">Fecha:</span> ${payment.payment_date}</p>
      <p class="text-sm text-gray-600"><span class="font-medium">Tour:</span> ${payment.tour}</p>
      <p class="text-sm text-gray-600"><span class="font-medium">Forma de pago:</span> ${payment.options_payment}</p>
      <p class="text-sm text-gray-600"><span class="font-medium">Valor:</span> <span class="text-green-600 font-semibold">$${payment.value.toLocaleString()}</span></p>
      <p class="text-sm text-gray-600"><span class="font-medium">Referencia:</span> ${payment.payment_reference}</p>
      <p class="text-sm text-gray-600"><span class="font-medium">Confirmado:</span> 
        ${payment.confirmed === "Sí"
          ? '<span class="text-green-600 font-semibold">Sí</span>'
          : '<span class="text-red-600 font-semibold">No</span>'}
      </p>
      ${payment.note ? `<p class="text-sm text-gray-600"><span class="font-medium">Nota:</span> ${payment.note}</p>` : ''}
      ${
        payment.document_url
          ? `<p class="text-sm"><a href="${payment.document_url}" target="_blank" class="text-blue-600 hover:underline font-medium">Ver documento</a></p>`
          : ""
      }
    </div>
  `;

  return card;
}


  // Agregar abono
  formCreatePayment.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(formCreatePayment);

    const payment = {
      id: paymentIdCounter++,
      payment_date: formData.get("payment_date") || "-",
      tour: document.getElementById("input_tour").value || "-",
      options_payment: formData.get("options_payment") || "-",
      value: parseFloat(formData.get("value")) || 0,
      payment_reference: formData.get("payment_reference") || "-",
      confirmed: formData.get("confirmed") === "true" ? "Sí" : "No",
      note: formData.get("note") || "-",
      document_url: formData.get("document_url") || ""
    };

    paymentsList.push(payment);

    // Mostrar tarjeta
    const card = crearTarjetaAbono(payment);
    paymentsContainer.appendChild(card);

    actualizarTotalPagos();

    modalPayment.style.display = "none";
    formCreatePayment.reset();
  });

  // Delegar evento para eliminar tarjetas
  paymentsContainer.addEventListener("click", function (e) {
    if (e.target.classList.contains("eliminar-abono")) {
      const id = parseInt(e.target.dataset.id);
      paymentsList = paymentsList.filter(p => p.id !== id);
      e.target.closest("div").remove();
      actualizarTotalPagos();
    }
  });

  function actualizarTotalPagos() {
    const total = paymentsList.reduce((sum, p) => sum + p.value, 0);
    totalPaymentsInput.value = total.toFixed(2);
  }
});
