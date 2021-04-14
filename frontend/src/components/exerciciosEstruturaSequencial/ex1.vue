<template>
    <div class="container">
        <div>
            <b-card bg-variant="light" border-variant="light" text-variant="black"
                    style="box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12) !important">
                <TextoIntrodutorio v-show="true" :texto="texto_ex1"></TextoIntrodutorio>

                <b-form @submit="onSubmit" @reset="onReset">
                    <b-button class="mr-1"type="submit" variant="primary">Executar</b-button>
                    <b-button type="reset" variant="danger" :disabled="mostra_resposta == false">Limpar</b-button>
                </b-form>

                <RespostaAlerta :resposta="resp.resposta01" :mostra_resposta="mostra_resposta"></RespostaAlerta>
            </b-card>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import TextoIntrodutorio from "@/components/Python/modulos/TextoIntrodutorio.vue";
    import RespostaAlerta from "@/components/Python/modulos/RespostaAlerta.vue";
    const valores = require('@/components/exerciciosEstruturaSequencial/utils/valores.js');

    export default {
        components: {
            TextoIntrodutorio,
            RespostaAlerta
        },
        data() {
            return {
                texto_ex1: "1. Faça um Programa que mostre a mensagem 'Alo mundo' na tela.",
                resp: {
                    resposta01: "",
                    status: 0
                }, 
                post: true,
                mostra_resposta: false,
            };
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault()
                axios.post(
                    valores.path,
                    null,
                    {
                        params: {
                            exercicio: 1,
                        }
                    })
                    .then((res) => {
                        this.resp.resposta01 = res.data.resposta
                        this.resp.status = res.data.status
                        if (this.status = 200) {
                            this.mostra_resposta = true
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                    })

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