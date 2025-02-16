document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("artCanvas");
    const ctx = canvas.getContext("2d");

    if (canvas) {
        canvas.width = 400;
        canvas.height = 400;

        function drawArt() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < 50; i++) {
                let x = Math.random() * canvas.width;
                let y = Math.random() * canvas.height;
                let size = Math.random() * 50;
                ctx.fillStyle = `hsl(${Math.random() * 360}, 100%, 50%)`;
                ctx.beginPath();
                ctx.arc(x, y, size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        drawArt(); // Dessiner dès le chargement
    }
});
