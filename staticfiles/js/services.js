

window.onload = function () {

    console.log("Studio Flash Services Loaded");

};




function bookService(serviceName) {

    alert("✅ Booking Request Sent For: " + serviceName);

}




function searchService() {

    let input =
    document.getElementById("search")
    .value
    .toLowerCase();

    let cards =
    document.querySelectorAll(".card");

    cards.forEach(function(card) {

        let title =
        card.querySelector("h3")
        .innerText
        .toLowerCase();

        if (title.includes(input)) {

            card.style.display = "block";

        } else {

            card.style.display = "none";

        }

    });

}