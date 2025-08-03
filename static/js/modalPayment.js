document.addEventListener('DOMContentLoaded', function () {
  const modalPayment = document.getElementById("modalPayment");
  const modalPaymentBtn = document.getElementById("openModalPaymentBtn");
  const closeModalPayment = document.getElementById("closeModalPayment");
  const formCreatePayment = document.getElementById("formCreatePayment");
  const totalPaymentsInput = document.getElementById("total_payments");
  const paymentsContainer = document.getElementById("paymentsContainer");

  const paymentMethodSelect = document.getElementById("payment_method");
  const bankPlatformField = document.getElementById("bankPlatformField");

  window.paymentsList = [];
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
    card.className = "payment-card";

    card.innerHTML = `
    <button data-id="${payment.id}" class="delete-payment-button" title="Eliminar abono">×</button>
    <div class="payment-info">
      <h3>Abono #${payment.id}</h3>
      <p><strong>Fecha:</strong> ${payment.payment_date}</p>
      <p><strong>Forma de pago:</strong> ${payment.options_payment}</p>
      <p><strong>Plataforma:</strong> ${payment.options_banks}</p>
      <p><strong>Valor:</strong> <span class="payment-value">$${payment.value.toLocaleString()}</span></p>
      <p><strong>Referencia:</strong> ${payment.payment_reference}</p>
      ${payment.note ? `<p><strong>Nota:</strong> ${payment.note}</p>` : ''}
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
      options_banks: formData.get("options_banks") || "-",
      options_payment: formData.get("options_payment") || "-",
      value: parseFloat(formData.get("value")) || 0,
      payment_reference: formData.get("payment_reference") || "-",
      // confirmed: formData.get("confirmed") === "true" ? "Sí" : "No",
      note: formData.get("note") || "-",
      // document_url: formData.get("document_url") || ""
    };

    window.paymentsList.push(payment);

    const card = crearTarjetaAbono(payment);
    paymentsContainer.appendChild(card);

    actualizarTotalPagos();

    modalPayment.style.display = "none";
    formCreatePayment.reset();
  });

  // Delegar evento para eliminar tarjetas
  paymentsContainer.addEventListener("click", function (e) {
    if (e.target.classList.contains("delete-payment-button")) {
      const id = parseInt(e.target.dataset.id);
      paymentsList = paymentsList.filter(p => p.id !== id);
      e.target.closest(".payment-card").remove();
      actualizarTotalPagos();
    }
  });

  function actualizarTotalPagos() {
    const total = paymentsList.reduce((sum, p) => sum + p.value, 0);
    totalPaymentsInput.value = total.toFixed(2);
  }
  // Función para mostrar u ocultar el campo según el método
  function toggleBankPlatformField() {
    const selectedMethod = paymentMethodSelect.value;
    const bankSelect = document.getElementById("payment_bank");
    if (selectedMethod === "Transferencia") {
      bankPlatformField.style.display = "block";
      bankSelect.setAttribute("required", "required");
    } else {
      bankPlatformField.style.display = "none";
      bankSelect.removeAttribute("required");
      bankSelect.value = "";  // Limpiar selección
    }
  }

  // Evento cuando cambia el método de pago
  paymentMethodSelect.addEventListener("change", toggleBankPlatformField);

  // Llamar al cargar la página (por si ya hay un valor seleccionado)
  toggleBankPlatformField();

});
