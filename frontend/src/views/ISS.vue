<template>
    <div class="container">
        API: {{ texto }}
        <hr />
        Latitude: {{ latitude }}
        <hr />
        Longitude: {{ longitude }}
        <hr />
    </div>
</template>

<script>
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
                axios.get("http://api.open-notify.org/iss-now.json")
                    .then((res) => {
                        this.texto = res
                        this.latitude = res.data.iss_position.latitude
                        this.longitude = res.data.iss_position.longitude
                    })
                    .catch((error) => {console.error(error);})
            }            
        },
        created() {
            this.posicao_iss()
        }
    }         
</script>