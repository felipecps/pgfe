<template>
    <div class="container">
        <div>
            <b-card bg-variant="light" border-variant="light" text-variant="black"
                    style="box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12) !important">
                <b-form @submit="onSubmit" @reset="onReset">

                    <TextoIntrodutorio v-show="true" :texto="texto_ex1"></TextoIntrodutorio>
                    <b-button class="mr-1" @click="submit('1')" variant="primary">Executar</b-button>
                    <b-button type="reset" variant="danger" :disabled="mostra_resposta == false">Limpar</b-button>

                    <div v-if="mostra_resposta">
                        <b-alert class="mt-3" show>{{ resposta01 }}</b-alert>
                    </div>

                </b-form>
            </b-card>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import TextoIntrodutorio from "@/components/TextoIntrodutorio.vue";

    export default {
        name: 'PythonExercicios',
        components: {
            TextoIntrodutorio
        },
        data() {
            return {
                texto_ex1: "1. Faça um Programa que mostre a mensagem 'Alo mundo' na tela.",
                post: true,
                mostra_resposta: false,
                resposta01: "",
                status: 0
            };
        },
        methods: {
            submit(nro_do_exercicio) {
                //const path = 'http://localhost:5000/resolve_exercicios'
                const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'
                if (this.post) {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: nro_do_exercicio,
                            }
                        })
                        .then((res) => {
                            this.resposta01 = res.data.resposta
                            this.status = res.data.status
                            if (this.status = 200) {
                                this.mostra_resposta = true
                            }
                        })
                        .catch((error) => {
                            console.error(error);
                        })
                }
            },
            onSubmit(evt) {
                evt.preventDefault()

            },
            onReset(event) {
                event.preventDefault()
                this.mostra_resposta = false
            }  
        },
        created() {

        },
    };
</script>

<style scoped>
    .fade-in {
        animation: animation-fade-in 0.3s;
    }

    @keyframes animation-fade-in {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>