function showPage(el, targetId) {
    var navLinks = document.querySelectorAll('.nav-link');
    var pages = document.querySelectorAll('.page');
    
    // Remove active class from all links and pages
    for (var j = 0; j < navLinks.length; j++) {
        navLinks[j].classList.remove('active');
    }
    for (var k = 0; k < pages.length; k++) {
        pages[k].classList.remove('active');
    }
    
    // Add active class to clicked link
    if (el) {
        el.classList.add('active');
    }
    
    // Show corresponding page
    var targetElement = document.getElementById(targetId);
    if (targetElement) {
        targetElement.classList.add('active');
    }
    
    // Scroll to top
    window.scrollTo(0, 0);
    
    // Prevent default anchor jump
    return false;
}
