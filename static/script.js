function showSection(sectionId) {
    var sections = document.querySelectorAll(".section");

    sections.forEach(function(section) {
        section.style.display = "none";
    });

    document.getElementById(sectionId).style.display = "block";
}

// 🔥 This keeps the page on contact after redirect
window.onload = function() {
    if (window.location.hash) {
        showSection(window.location.hash.substring(1));
    } else {
        showSection("about");
    }
};
