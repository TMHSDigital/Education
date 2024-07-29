// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Fade in effect for section links
    const sectionLinks = document.querySelectorAll('.section-link');
    sectionLinks.forEach((link, index) => {
        setTimeout(() => {
            link.classList.add('fade-in');
        }, index * 100);
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Toggle dark mode
    const darkModeToggle = document.createElement('button');
    darkModeToggle.textContent = '🌓';
    darkModeToggle.style.position = 'fixed';
    darkModeToggle.style.top = '20px';
    darkModeToggle.style.right = '20px';
    darkModeToggle.style.zIndex = '1000';
    darkModeToggle.style.background = 'none';
    darkModeToggle.style.border = 'none';
    darkModeToggle.style.fontSize = '24px';
    darkModeToggle.style.cursor = 'pointer';
    document.body.appendChild(darkModeToggle);

    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('dark-mode', document.body.classList.contains('dark-mode'));
    });

    // Check for saved dark mode preference
    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
    }

    // Add active class to current navigation link
    const currentLocation = location.href;
    const menuItems = document.querySelectorAll('nav a');
    menuItems.forEach(link => {
        if (link.href === currentLocation) {
            link.classList.add('active');
        }
    });
});