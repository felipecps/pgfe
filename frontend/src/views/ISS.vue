<template>
    <div id="app" class="container">
        <div>
            <b-img :src="require('../assets/iss.jpg')" fluid alt="Responsive image"></b-img>
        </div>
        <!-- API: {{ texto }}
    <hr />
    -->
        Latitude: {{ latitude }}
        <hr />
        Longitude: {{ longitude }}
        <hr />

        <div id="app">
            <GoogleMap :latitude="latitude" :longitude="longitude"/>
        </div>
        <br />
    </div>
</template>

<script>
// Tutorial completo: https://www.digitalocean.com/community/tutorials/vuejs-vue-google-maps
    import axios from 'axios';
    import GoogleMap from "@/components/GoogleMap.vue";
    export default {
        name: 'App',
        components: {
            GoogleMap
        },
        data() {
            return {
                texto: "",
                latitude: 0,
                longitude: 0,
              
            }
        },
        methods: {
            posicao_iss() {
                axios.get("https://api.wheretheiss.at/v1/satellites/25544")
                    .then((res) => {
                        this.texto = res
                        this.latitude = res.data.latitude
                        this.longitude = res.data.longitude
                    })
                    .catch((error) => { console.error(error); })
            }
        },
        created() {
            this.posicao_iss()
        }
    }
</script>

