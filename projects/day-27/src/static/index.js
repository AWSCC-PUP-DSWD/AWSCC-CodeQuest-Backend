const updateBtns = document.querySelectorAll(".update-btn");
const deleteBtns = document.querySelectorAll(".delete-btn");
const updateBookBtn = document.getElementById("updateBookBtn");

// update book details
const updateTitle = document.getElementById("updateTitle");
const updateAuthor = document.getElementById("updateAuthor");
const updatePublishedYear = document.getElementById("updatePublishedYear");
let id;

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", (event) => {
        const parentNode = event.target.parentNode;
        id = parentNode.dataset.id;
        updateTitle.value = parentNode.dataset.title;
        updateAuthor.value = parentNode.dataset.author;
        updatePublishedYear.value = parentNode.dataset.publishedYear;
    });

    deleteBtns[i].addEventListener("click", (event) => {
        id = event.target.parentNode.dataset.id;
        fetch(`delete/${id}`, {
            method: "DELETE"
        }).then(data => data.json()).then(_ => window.location.href = "/")
    })
}

updateBookBtn.addEventListener("click", () => {
    fetch(`update/${id}`, {
        body: JSON.stringify({title: updateTitle.value, author: updateAuthor.value, publishedYear: updatePublishedYear.value}),
        headers: {
            "Content-Type": "application/json"
        },
        method: "PATCH"
    }).then(data => data.json()).then(_ => window.location.href = "/")
}); 