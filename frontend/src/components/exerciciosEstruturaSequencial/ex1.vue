<template>
    <div class="container">
        <div>
            <b-card bg-variant="light" text-variant="black">
                <b-form @submit="onSubmit">

                    <TextoIntrodutorio v-show="true"
                                       :texto="texto_ex1">
                    </TextoIntrodutorio>

                    <b-button class="mr-1" @click="submit('1')" variant="primary">Executar</b-button>
                    <b-alert class="mt-3" v-if="resposta01" show>{{ resposta01 }}</b-alert>
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
                const path = 'http://localhost:5000/resolve_exercicios'
                //const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'
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

            }
        },
        created() {

        },
    };
</script>
