'use strict';

const STEPHANSDOM = [48.208498, 16.373132];
const map = L.map('map').setView(STEPHANSDOM, 16);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 21,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> | Leaf noone behind'
}).addTo(map);


// for random map clicks
let popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);
// end for random map clicks

let markers = [];

function formatTemplate(tree) {
    return `
<div class="flex-column">
    <h2>Tree</h2>
    <p><b>Donations:</b> €${tree.donations}</p>
    ${tree.sponsor ? '<p><b>Sponsor</b>: ' + tree.sponsor + "</p>" : ""}

    <button onclick="voteForTree(${tree.id}, this)">Vote For tree!</button>


    <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg">
</div>
`;
}

function loadTreeData() {
    fetch("http://localhost:5000/trees").then((resp) => resp.json().then((data) => drawTreeData(data)))
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
            .bindPopup(popup);

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
