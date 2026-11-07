(function () {
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      const open = links.classList.contains("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll("[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const success = form.querySelector(".form-success");
      if (success) {
        success.classList.add("show");
        success.textContent =
          form.dataset.successMessage ||
          "Thanks! This is a demo submission for our class project — no real payment was processed.";
      }
      form.reset();
    });
  });

  const planSelect = document.getElementById("plan");
  const totalEl = document.getElementById("order-total");
  const planLine = document.getElementById("order-plan");
  if (planSelect && totalEl) {
    const prices = {
      free: 0,
      premium: 5.99,
      pro: 9.99,
      device: 79.99,
      "device-premium": 85.98,
    };
    const labels = {
      free: "Free plan",
      premium: "Premium (monthly)",
      pro: "Pro (monthly)",
      device: "StudyBuddy Device",
      "device-premium": "Device + Premium (1 mo)",
    };
    function update() {
      const key = planSelect.value;
      const price = prices[key] ?? 0;
      totalEl.textContent = "$" + price.toFixed(2);
      if (planLine) planLine.textContent = labels[key] || key;
    }
    planSelect.addEventListener("change", update);
    update();
  }
})();
