document.getElementById("confirmPost").addEventListener("click", function () {
    const titleElement = document.getElementById("title-post");
    const myOpinionElement = document.getElementById("my_opinion-post");
    const myScoreElement = document.getElementById("my_score-post");
    const completedElement = document.getElementById("completed-post");
    const favouriteElement = document.getElementById("favourite-post");
    
    if (!titleElement.value || !myOpinionElement.value || !myScoreElement.value) {
        return
    }
    const title = titleElement.value;
    const myOpinion = myOpinionElement.value;
    const myScore = parseInt(myScoreElement.value);
    const completed = completedElement.checked;
    const favourite = favouriteElement.checked;

    const data = {
        title: title,
        my_opinion: myOpinion,
        completed: completed,
        my_score: myScore,
        favourite: favourite
    };

    fetch(`/videogames`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })

    .then((response) => {
        if (response.ok) {
            alert("Videogame added\nYou will be redirected to the list of videogames.");
            window.location.reload()
        } else {
            return response.json().then((error) => {
                alert("Error: " + error.error);
            });
        }
    })

    .catch((error) => {
        console.error("Error adding the videogame:", error);
        alert("Error processing the request.");
    });
});
