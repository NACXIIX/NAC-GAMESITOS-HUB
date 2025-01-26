document.querySelectorAll(".deleteButton").forEach((boton) => {
    boton.addEventListener("click", function () {
        const videojuegoId = this.getAttribute("data-id");

        const confirmButton = document.getElementById("confirmDelete");
        confirmButton.setAttribute("data-id", videojuegoId);

        const deleteModal = new bootstrap.Modal(document.getElementById("delete-form"));
        deleteModal.show();

        document.getElementById("delete-form").addEventListener('hidden.bs.modal', function () {
            confirmButton.removeAttribute("data-id");

            const backdrop = document.querySelector(".modal-backdrop");
            if (backdrop) backdrop.remove();

            document.body.classList.remove("modal-open");
            document.body.style.overflow = "auto";
        }, { once: true });
    });
});

document.getElementById("confirmDelete").addEventListener("click", function () {
    const videojuegoId = this.getAttribute("data-id");

    if (!videojuegoId) {
        alert("El ID del videojuego no está disponible.");
        return;
    }

    fetch(`/videogames/${videojuegoId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => {
            if (response.ok) {

                const deleteModal = bootstrap.Modal.getInstance(document.getElementById("delete-form"));
                if (deleteModal) deleteModal.hide();

                window.location.reload();
            } else {
                return response.json().then((error) => {
                    alert("Error: " + error.error);
                });
            }
        })
        .catch((error) => {
            console.error("Error al eliminar el videojuego:", error);
            alert("Hubo un problema al procesar la solicitud.");
        });
});
