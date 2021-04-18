<template>
    <div class="container">
        <div class="mt-3">
            <Breadcumb :items="itens_breadcumb"></Breadcumb>
            <b-card bg-variant="light" text-variant="black" class="shadow p-3 bg-light rounded">
                <TextoIntrodutorio v-show="true" :texto="texto15"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-15" label="Qual é o salário por hora de trabalho?" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Salario por hora"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-exercicio-15.1" label="Quantas horas de trabalho no mês?" label-for="input-3">
                            <b-form-input id="input-3"
                                          autocomplete="off"
                                          v-model="form.nro2"
                                          placeholder="Número de horas"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular salário</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == '' && form.nro2 == ''">Limpar</b-button>
                    </b-form>
                    <RespostaAlerta :resposta="resp.resposta15" :mostra_resposta="mostra_resposta"></RespostaAlerta>
                </div>
            </b-card>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import Breadcumb from "@/components/Python/modulos/Breadcumb.vue";
    import TextoIntrodutorio from "@/components/Python/modulos/TextoIntrodutorio.vue";
    import RespostaAlerta from "@/components/Python/modulos/RespostaAlerta.vue";
    const valores = require('@/components/exerciciosEstruturaSequencial/utils/valores.js');

    export default {
        components: {
            TextoIntrodutorio,
            RespostaAlerta,
            Breadcumb
        },
        data() {
            return {
                texto15: "15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: a) salário bruto. b) quanto pagou ao INSS. c) quanto pagou ao sindicato. d) o salário líquido. e) calcule os descontos e o salário líquido",
                form: {
                    nro1: '',
                    nro2: '',
                },
                resp: {
                    resposta15: "",
                    status: 0
                },     
                mostra_resposta: false,
                itens_breadcumb: [
                    {
                        text: valores.home_text,
                        href: valores.home_path
                    },
                    {
                        text: valores.estruturaSequencial_text,
                        href: valores.estruturaSequencial_path
                    },
                    {
                        text: 'Exercício 15',
                        active: true
                    }
                ]
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
                                exercicio: 15,
                                valor1: this.form.nro1,
                                valor2: this.form.nro2
                            }
                        })
                        .then((res) => {
                            this.resp.resposta15 = res.data.resposta
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
