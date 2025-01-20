document.getElementById("deleteButton").addEventListener("click", function () {
    const videogameId = document.getElementById("videogame_id").value;

    if (!videogameId) {
        alert("Please select a videogame");
        return;
    }

    const data = {
        id: videogameId
    };

    fetch(`/videogames/${videogameId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        }
    })
         .then((response) => {
            if (response.ok) {
                alert("Videogame deleted\nYou will be redirected to the list of videogames.");
                window.location.href = "/videogames";
            } else {
                return response.json().then((error) => {
                    alert("Error: " + error.error);
                });
            }
        })
        .catch((error) => {
            console.error("Error deleting the videogame:", error);
            alert("Error processing the request.");
        });
});
