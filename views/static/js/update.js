document.getElementById("updateButton").addEventListener("click", function () {
    const updateVideogameID = document.getElementById("videogame_id");
    const updateTitleElement = document.getElementById("title");
    const updateMyOpinionElement = document.getElementById("my_opinion");
    const updateMyScoreElement = document.getElementById("my_score");
    const updateCompletedElement = document.getElementById("completed");
    const updateFavouriteElement = document.getElementById("favourite");

    const updateVideogameId = parseInt(updateVideogameID.value);
    const updateTitle = updateTitleElement.value;
    const updateMyOpinion = updateMyOpinionElement.value;
    const updateMyScore = parseInt(updateMyScoreElement.value);
    const updateCompleted = updateCompletedElement.checked;
    const updateFavourite = updateFavouriteElement.checked;

    if (!updateVideogameId) {
        alert("Please, select a videogame.");
        return;
    }

    const updateData = {
        id: updateVideogameId,
        title: updateTitle,
        my_opinion: updateMyOpinion,
        completed: updateCompleted,
        my_score: updateMyScore,
        favourite: updateFavourite
    };

    fetch(`/videogames/${updateVideogameId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(updateData)
    })
    .then((response) => {
        if (response.ok) {
            window.location.reload()
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
