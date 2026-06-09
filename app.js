// Security features have been reverted to ensure site navigation works correctly.

function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const pages = document.querySelectorAll('.page');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all links and pages
            navLinks.forEach(l => l.classList.remove('active'));
            pages.forEach(p => p.classList.remove('active'));
            
            // Add active class to clicked link
            link.classList.add('active');
            
            // Show corresponding page
            const targetId = link.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');
            
            // Optional: smooth scroll to top if needed
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
}

// Execute immediately since script is at the bottom of the body
initNavigation();

