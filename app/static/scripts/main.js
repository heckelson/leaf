'use strict';

const STEPHANSDOM = [48.208498, 16.373132];
const map = L.map('map').setView(STEPHANSDOM, 16);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 21,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> | Leaf noone behind'
}).addTo(map);

let markers = [];

function fetchVotesForUser() {
    const headers = new Headers();
    headers.set("Cookie", document.cookie);

    const request = new XMLHttpRequest()
    request.open("GET", "http://localhost:5000/trees/votes", false);
    // request.setRequestHeader("Cookie", document.cookie);
    request.withCredentials = true;
    request.send(null);

    return JSON.parse(request.responseText).votes;
}

function formatTemplate(tree) {
    const votes = fetchVotesForUser();

    let result = `
<div class="flex-column">
    <h2>Tree #${tree.id + 1}</h2>
    <p><b>Donations:</b> €${tree.donations}</p>
    <p><b>Votes:</b> ${tree.votes}</p>
`;

    if (tree.sponsor) {
        result += `<p><b>Sponsor</b>: + ${tree.sponsor} + </p>`;
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
</div>
`;

    return result;

}

function loadTreeData() {
    fetch("http://localhost:5000/trees").then((resp) => resp.json().then((data) => drawTreeData(data)))
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

    fetch("http://localhost:5000/trees/vote", {
        method: "POST", headers: headers, body: myVote
    }).then((resp) => console.log(resp));

    loadTreeData();

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
