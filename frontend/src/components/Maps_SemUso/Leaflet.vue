﻿<template>
    <div id="mapContainer"></div>
</template>

<script>
    import "leaflet/dist/leaflet.css";
    import L from "leaflet";

    export default {
        name: "LeafletMap",
        data() {
            return {
                map: null
            };
        },
        mounted() {
            this.map = L.map("mapContainer").setView([51.959, -8.623], 12);
            L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
                attribution:
                    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);
        },
        beforeDestroy() {
            if (this.map) {
                this.map.remove();
            }
        }
    };
</script>

<style scoped>
    #mapContainer {
        width: 100vw;
        height: 100vh;
    }
</style>