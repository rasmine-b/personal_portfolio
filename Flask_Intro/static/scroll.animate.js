// Animation for fade-in effects
document.addEventListener("DOMContentLoaded", () => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll(".fade-in").forEach(el => observer.observe(el));
});

document.querySelectorAll('.linkedlist-display').forEach(el => {
  el.classList.add('visible');
});
