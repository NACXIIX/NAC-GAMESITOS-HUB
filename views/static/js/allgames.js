document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('[id^="card-"]');
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.classList.add('bg-danger', 'text-white', 'border', 'border-primary');
            card.style.transform = 'scale(1.1)';
        });

        card.addEventListener('mouseout', function() {
            card.classList.remove('bg-danger', 'text-white', 'border', 'border-primary');
            card.style.transform = 'scale(1)';
        });
    });
});
