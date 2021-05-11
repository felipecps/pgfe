<template>
    <div class="container">
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
    </div>
</template>

<script>
//https://www.digitalocean.com/community/tutorials/vuejs-vue-google-maps
//https://www.npmjs.com/package/vue2-google-maps
    import axios from 'axios';
    export default {
        data() {
            return {
                texto: "",
                latitude: "",
                longitude: ""
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