<template>
    <div id="app" class="container">
        <div>
            <b-img :src="require('../assets/iss.jpg')" fluid alt="Responsive image"></b-img>
        </div>
        <!-- API:
            {{ texto }}
    <hr />
    -->
        <div class="mt-3">
            Latitude: {{ latitude }}
            <hr />
            Longitude: {{ longitude }}
            <hr />
        </div>
        <div class="mt-3 mb-3">
            <h1>
                O mapa será adicionado em breve.
            </h1>
        </div>
    </div>
</template>

<script>
// Tutorial completo: https://www.digitalocean.com/community/tutorials/vuejs-vue-google-maps
    import axios from 'axios';
    //import GoogleMap from "@/components/GoogleMap.vue";
    //import Leaflet from "@/components/Leaflet.vue";
    export default {
        name: 'App',
        components: {
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

