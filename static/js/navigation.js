(function () {
  "use strict";

  var nav = document.getElementById("siteNav");
  var toggle = document.getElementById("navToggle");
  var drawer = document.getElementById("mobileDrawer");

  function onScroll() {
    if (nav) nav.classList.toggle("is-scrolled", window.scrollY > 40);
  }

  function closeDrawer() {
    if (!drawer || !toggle) return;
    drawer.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toggle && drawer) {
    toggle.addEventListener("click", function () {
      var open = drawer.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    drawer.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeDrawer);
    });
  }

  document.querySelectorAll(".lang-switch").forEach(function (group) {
    group.querySelectorAll("button").forEach(function (button) {
      button.addEventListener("click", function () {
        var lang = button.dataset.lang;
        document.querySelectorAll(".lang-switch button").forEach(function (item) {
          item.classList.toggle("is-active", item.dataset.lang === lang);
        });
      });
    });
  });
})();
