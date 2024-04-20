<template>
  <div id="map"></div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default {
  mounted() {
    const STEPHANSDOM = [48.208498, 16.373132];
    const map = L.map("map").setView(STEPHANSDOM, 17);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OSM</a>',
    }).addTo(map);

    const legend = L.control({ position: "bottomleft" });
    legend.onAdd = function () {
      let div = L.DomUtil.create("div", "legend");
      div.innerHTML += "<h4>Legend</h4>";
      div.innerHTML +=
        '<i style="background: #e14b83"></i><span>Vienna today</span><br>';
      div.innerHTML +=
        '<i style="background: #985cdd"></i><span>Planned</span><br>';
      div.innerHTML += "<br />";
      div.innerHTML +=
        '<i style="background: #9e740f"></i><span>Low Potential</span><br>';
      div.innerHTML +=
        '<i style="background: #788007"></i><span>Middle Potential</span><br>';
      div.innerHTML +=
        '<i style="background: #199f6a"></i><span>High Potential</span><br>';
      return div;
    };
    legend.addTo(map);

    map.on("click", (event) => {
      console.log(`You clicked the map at ${event.latlng}!`);
    });
  },
};
</script>

<style>
#map {
  width: 100%;
  flex: 1 1 auto;
}

/* Source: https://codepen.io/haakseth/pen/KQbjdO */
.legend {
  padding: 6px 8px;
  font:
    14px Arial,
    Helvetica,
    sans-serif;
  background: white;
  background: rgba(255, 255, 255, 0.8);
  line-height: 24px;
  color: #555;

  text-align: left;
}

.legend h4 {
  text-align: center;
  font-size: 16px;
  margin: 2px 12px 8px;
  color: #777;
}

.legend span {
  position: relative;
  bottom: 3px;
}

.legend i {
  width: 18px;
  height: 18px;
  float: left;
  margin: 0 8px 0 0;
  opacity: 0.7;
}

.legend i.icon {
  background-size: 18px;
  background-color: rgba(255, 255, 255, 1);
}

/* End Source */
</style>
