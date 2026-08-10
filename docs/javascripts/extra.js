document.addEventListener("DOMContentLoaded", function () {
  // Format top header brand title with Execution Blue dot
  var headerTitles = document.querySelectorAll(".md-header__title, .md-header__topic");
  headerTitles.forEach(function (el) {
    if (el.innerHTML.includes("brando.")) {
      el.innerHTML = el.innerHTML.replace("brando.", 'brando<span style="color: #2563EB; font-weight: 900;">.</span>');
    }
  });
});
