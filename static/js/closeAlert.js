document.addEventListener("DOMContentLoaded", function () {
  setTimeout(function () {
    var alerts = document.querySelectorAll(".alert");
    alerts.forEach(function (alert) {
      alert.style.display = "none";
    });
  }, 5000); // 5000 milisaniye (5 saniye) sonra kapanacak
});
