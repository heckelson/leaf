'use strict';

const request_url = "http://localhost:8080";

const STEPHANSDOM = [48.208498, 16.373132];
const map = L.map('map').setView(STEPHANSDOM, 17);
let markers = [];

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 21,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> | Die Zweigstelle'
}).addTo(map);


/*Legend specific*/
let legend = L.control({position: "bottomleft"});

legend.onAdd = function (map) {
    let div = L.DomUtil.create("div", "legend");
    div.innerHTML += "<h4>I am Legend</h4>";
    div.innerHTML += '<i style="background: #e14b83"></i><span>Vienna today</span><br>';
    div.innerHTML += '<i style="background: #985cdd"></i><span>Planned</span><br>';
    div.innerHTML += '<br />';
    div.innerHTML += '<i style="background: #9e740f"></i><span>Low Potential</span><br>';
    div.innerHTML += '<i style="background: #788007"></i><span>Middle Potential</span><br>';
    div.innerHTML += '<i style="background: #199f6a"></i><span>High Potential</span><br>';
    return div;
};
legend.addTo(map);


function fetchVotesForUser() {
    const headers = new Headers();
    headers.set("Cookie", document.cookie);

    const request = new XMLHttpRequest()
    request.open("GET", request_url + "/trees/votes", false);
    request.withCredentials = true;
    request.send(null);

    return JSON.parse(request.responseText).votes;
}

function formatTemplate(tree) {
    const votes = fetchVotesForUser();

    let result = `
<div class="flex-column">
    <h2>Tree #${tree.id + 1}</h2>
    <p><b>Total Donations:</b> €${tree.donations.toFixed(2)}</p>
    <p><b>Votes:</b> ${tree.votes}</p>
`;

    if (tree.sponsor) {
        result += `<p><b>Sponsor</b>: ${tree.sponsor}</p>`;
    }

    if (votes) {
        const youVotedForTree = votes.includes(tree.id);

        if (youVotedForTree) {
            result += '<p>You already voted for this tree!</p>';
        } else {
            result += `<button onclick="voteForTree(${tree.id}, this)">Vote For tree!</button>`
        }
    }

    result += `
    <p>Hold click on the image to see a preview of what it could look like!</p>

    <div class="image-preview flex-column">
        <img class="over" src="/static/vorher.jpg" alt="" onpointerdown="fadeOutImage(this)" onpointerup="fadeInImage(this)"/>
        <img class="under" src="/static/nachher.jpg" alt=""/>
    </div>

    <div>
    <form action=${request_url + "/trees/fund"} method="post" class="donation-form">
        <label>Amount to donate €</label>
        <input type="number" name="amount">
        <input type="hidden" name="tree_id" value="${tree.id}">
        <button type="submit">Send us money!</button>
    </form>
    </div>
</div>
`;

    return result;

}


function showFlashMessage(message) {
    let headerDiv = document.getElementById('header');
    let flashMessageDiv = document.createElement('div');

    flashMessageDiv.innerHTML = `
    <div class="flash-message">
        <button id='close' onClick="this.parentElement.remove()">
            ✕
        </button>

        <div class="message-{{ category }}">${message}</div>
    </div>
    `
    headerDiv.after(flashMessageDiv);
}


function loadTreeData() {
    fetch(request_url + "/trees").then((resp) => resp.json().then((data) => drawTreeData(data)))
}


function fadeOutImage(image) {
    image.style.opacity = "0";
}

function fadeInImage(image) {
    image.style.opacity = "1";
}


function voteForTree(tree_id, button) {
    const myVote = JSON
        .stringify({
            "tree_id": tree_id
        });

    button.remove();

    const headers = new Headers();
    headers.set("Cookie", document.cookie);
    headers.set("Content-type", "application/json");

    fetch(request_url + "/trees/vote", {
        method: "POST", headers: headers, body: myVote
    }).then((resp) => {
        showFlashMessage(`Thank you for voting for tree #${tree_id+1}!`)
        loadTreeData();
    });
}


function getMarkerClassForTree(tree) {
    switch (tree.status) {
        case "DONE":
            return "category_done"
        case "IN_PLANNING":
            return "category_in_planning"
        case "LOW_POTENTIAL":
            return "category_low_potential"
        case "MEDIUM_POTENTIAL":
            return "category_middle_potential"
        case "HIGH_POTENTIAL":
            return "category_high_potential"
        default:
            return ""
    }
}

function drawTreeData(treeData) {
    removeAllMarkers();
    const trees = treeData.trees;

    for (const tree of trees) {
        let newMarker = L.marker([tree.xpos, tree.ypos]);

        const popup = L.popup({
            closePopupOnClick: false, autoClose: false
        }).setContent(formatTemplate(tree));

        newMarker
            .addTo(map)
            .bindPopup(popup, {
                maxWidth: 500, minWidth: 500
            });

        newMarker._icon.classList.add(getMarkerClassForTree(tree));

        markers.push(newMarker);
    }
}

function removeAllMarkers() {
    for (const marker of markers) {
        map.removeLayer(marker);
    }

    markers = [];
}

loadTreeData();

console.log("🗿");
