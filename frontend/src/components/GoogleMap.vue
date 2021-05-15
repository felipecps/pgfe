<template>
    <div>
        <p>
            {{ latitude }}
            {{ longitude }}
        </p>
        <GmapMap :center='center'
                 :zoom='6'
                 style='width:100%;  height: 400px;' />
    </div>
</template>

<script>
    // Tutorial Completo: https://www.digitalocean.com/community/tutorials/vuejs-vue-google-maps
    export default {
        name: 'GoogleMap',
        props: {
            latitude: { type: Number, required: true },
            longitude: { type: Number, required: true }
        },
        data() {
            return {
                center: { lat: 45.508, lng: -73.587 },
            }
        },
        mounted() {
            this.geolocate();
        },
        methods: {
            geolocate: function () {
                navigator.geolocation.getCurrentPosition(position => {
                    this.center = {
                        //lat: position.coords.latitude,
                        //lng: position.coords.longitude,
                        lat: this.latitude,
                        lng: this.longitude,
                    };
                });
            },
        },
    }
</script>