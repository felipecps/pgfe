<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto10"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-10" label="Qual é a temperatura em Celsius?" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="C"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Converter para Fahrenheit</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == ''">Limpar</b-button>
                    </b-form>
                    <RespostaAlerta :resposta="resp.resposta10" :mostra_resposta="mostra_resposta"></RespostaAlerta>
                </div>
            </b-card>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import TextoIntrodutorio from "@/components/Python/modulos/TextoIntrodutorio.vue";
    import RespostaAlerta from "@/components/Python/modulos/RespostaAlerta.vue";

    export default {
        components: {
            TextoIntrodutorio,
            RespostaAlerta
        },
        data() {
            return {
                texto10: "Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.",
                form: {
                    nro1: ''
                },
                resp: {
                    resposta10: "",
                    status: 0
                },     
                mostra_resposta: false
            };
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                const path = 'http://localhost:5000/resolve_exercicios'
                //const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'

                if (this.form.nro1 != '') {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: 10,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resp.resposta10 = res.data.resposta
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
