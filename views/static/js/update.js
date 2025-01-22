document.getElementById("updateButton").addEventListener("click", function () {
    const videogameID = document.getElementById("videogame_id");
    const titleElement = document.getElementById("title");
    const myOpinionElement = document.getElementById("my_opinion");
    const myScoreElement = document.getElementById("my_score");
    const completedElement = document.getElementById("completed");
    const favouriteElement = document.getElementById("favourite");

    const videogameId = parseInt(videogameID.value);
    const title = titleElement.value;
    const myOpinion = myOpinionElement.value;
    const myScore = parseInt(myScoreElement.value);
    const completed = completedElement.checked;
    const favourite = favouriteElement.checked;

    if (!videogameId) {
        alert("Por favor selecciona un videogame.");
        return;
    }

    const data = {
        id: videogameId,
        title: title,
        my_opinion: myOpinion,
        completed: completed,
        my_score: myScore,
        favourite: favourite
    };

    fetch(`/videogames/${videogameId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })
    .then((response) => {
        if (response.ok) {
            alert("Videogame updated\nYou will be redirected to the list of videogames.");
            window.location.href = "/videogames";
        } else {
            return response.json().then((error) => {
                alert("Error: " + error.error);
            });
        }
    })
    .catch((error) => {
        console.error("Error updating the videogame:", error);
        alert("Error processing the request.");
    });
});
