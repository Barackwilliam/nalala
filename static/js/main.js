document.addEventListener('DOMContentLoaded', function () {
  // Sidebar open/close
  const sidebar = document.getElementById('mobileSidebar');
  const backdrop = document.getElementById('sidebarBackdrop');
  const openBtn = document.getElementById('sidebarToggle');
  const closeBtn = document.getElementById('closeSidebar');

  function openSidebar(){
    sidebar.classList.add('active');
    backdrop.classList.add('active');
    sidebar.setAttribute('aria-hidden','false');
    backdrop.setAttribute('aria-hidden','false');
    document.body.style.overflow = 'hidden';
  }
  function closeSidebar(){
    sidebar.classList.remove('active');
    backdrop.classList.remove('active');
    sidebar.setAttribute('aria-hidden','true');
    backdrop.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
  }

  if(openBtn) openBtn.addEventListener('click', openSidebar);
  if(closeBtn) closeBtn.addEventListener('click', closeSidebar);
  if(backdrop) backdrop.addEventListener('click', closeSidebar);
  document.addEventListener('keydown', (e) => { if(e.key === 'Escape') closeSidebar(); });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href.length > 1) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        closeSidebar();
      }
    });
  });

  // IntersectionObserver for fade-in
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('animate-fade-in');
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.room-card, .card, .hero-section, .booking-hero').forEach(el => io.observe(el));

  // Testimonials autoplay (Bootstrap carousel)
  const tc = document.getElementById('testimonialCarousel');
  if (tc) {
    const bs = new bootstrap.Carousel(tc, { interval: 5000, ride: 'carousel' });
  }

  // Navbar shrink on scroll
  const nav = document.querySelector('.safari-nav');
  window.addEventListener('scroll', () => {
    if(window.scrollY > 60) nav.classList.add('scrolled'); else nav.classList.remove('scrolled');
  });
});
