'use strict';

const STEPHANSDOM = [48.208498, 16.373132];
const map = L.map('map').setView(STEPHANSDOM, 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> | Leaf noone behind'
}).addTo(map);


let popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);

let markers = [];

function formatTemplate(name) {
    const markerTemplate = `
<div class="flex-center">
    <h2>This is a test</h2>
    <p>Hello this is a test content field</p>
    <p>This is being replaced with the name: {{ name }}</p>

    <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg">
</div>
`.replaceAll("{{ name }}", name)

    return markerTemplate;
}


markers.push(L.marker([48.208498, 16.373132])
    .addTo(map)
    .bindPopup(formatTemplate("Alex")));
