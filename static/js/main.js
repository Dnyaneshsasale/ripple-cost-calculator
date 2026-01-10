document.addEventListener('DOMContentLoaded', function () {
    // Landing page slider demo
    const demoBags = document.getElementById('demoBags');
    const demoBagsValue = document.getElementById('demoBagsValue');
    const demoCostText = document.getElementById('demoCostText');

    if (demoBags && demoBagsValue && demoCostText) {
        function updateDemo() {
            const bags = parseInt(demoBags.value || '0');
            demoBagsValue.textContent = bags;
            const yearlyRipple = bags * 52 * 2; // ₹2 ripple per bag
            const fiveYear = yearlyRipple * 5;
            demoCostText.textContent = `Estimated 5-year ripple cost: ₹${fiveYear}`;
        }
        demoBags.addEventListener('input', updateDemo);
        updateDemo();
    }
});
