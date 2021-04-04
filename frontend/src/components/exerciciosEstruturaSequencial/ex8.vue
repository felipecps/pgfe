<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto8"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-3" label="Qual é o seu salário por hora?" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="R$"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Quantas horas por mês você trabalha?" label-for="input-2"
                                      description="">
                            <b-form-input id="input-2"
                                          autocomplete="off"
                                          v-model="form.nro2"
                                          placeholder="Horas por mês"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == '' && form.nro2 == ''">Limpar</b-button>
                    </b-form>
                    <RespostaAlerta :resposta="resp.resposta08" :mostra_resposta="mostra_resposta"></RespostaAlerta>
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
                texto8: "8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.",
                form: {
                    nro1: '',
                    nro2: ''
                },
                resp: {
                    resposta08: "",
                    status: 0
                },     
                mostra_resposta: false
            };
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                //const path = 'http://localhost:5000/resolve_exercicios'
                const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'

                if (this.form.nro1 != '' && this.form.nro2 != '') {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: 8,
                                valor1: this.form.nro1,
                                valor2: this.form.nro2
                            }
                        })
                        .then((res) => {
                            this.resp.resposta08 = res.data.resposta
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
                this.form.nro2 = '',
                this.mostra_resposta = false
            }            
        }
    };
</script>
