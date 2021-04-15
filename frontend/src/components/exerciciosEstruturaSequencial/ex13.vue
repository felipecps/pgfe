<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto13"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-13" label="Qual é a altura da pessoa?" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Altura da pessoa em metros"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular peso ideal H/M</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == ''">Limpar</b-button>
                    </b-form>
                    <div v-if="resp.status==200">
                        <b-alert class="mt-3" v-if="mostra_resposta" show>
                            <p>
                                {{ resp.resp_h}}
                            </p>
                            <p>
                                {{ resp.resp_m}}
                            </p>
                        </b-alert>
                    </div>
                    <div v-else>
                        <RespostaAlerta :resposta="resp.resposta13" :mostra_resposta="mostra_resposta"></RespostaAlerta>
                    </div>
                </div>
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
                texto13: "13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: a) Para homens: (72.7 * h) - 58 b) Para mulheres: (62.1 * h) - 44.7",
                form: {
                    nro1: ''
                },
                resp: {
                    resposta13: "",
                    resp_h: "",
                    resp_m: "",
                    status: 0
                },     
                mostra_resposta: false
            };
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()

                if (this.form.nro1 != '') {
                    axios.post(
                        valores.path,
                        null,
                        {
                            params: {
                                exercicio: 13,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resp.resposta13 = res.data.resposta
                            this.resp.resp_h = res.data.pesoH
                            this.resp.resp_m = res.data.pesoM
                            this.resp.status = res.data.status
                            this.mostra_resposta = true

                        })
                        .catch((error) => {
                            console.error(error);
                        })
                }
            },
            onReset(event) {
                event.preventDefault()
                this.form.nro1 = '',
                this.mostra_resposta = false
            }            
        }
    };
</script>
