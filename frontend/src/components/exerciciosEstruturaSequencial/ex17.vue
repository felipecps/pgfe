<template>
    <div class="container">
        <div class="mt-3">
            <Breadcumb :items="itens_breadcumb"></Breadcumb>
            <b-card bg-variant="light" text-variant="black" class="shadow p-3 bg-light rounded">
                <TextoIntrodutorio v-show="true" :texto="texto17"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-17" label="Qual é a área a ser pintada (em m²)?" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Área"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular latas de tinta</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == ''">Limpar</b-button>
                    </b-form>
                    <RespostaAlerta :resposta="resp.resposta17" :mostra_resposta="mostra_resposta"></RespostaAlerta>
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
                texto17: "17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: a) comprar apenas latas de 18 litros; b) comprar apenas galões de 3,6 litros; c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.",
                form: {
                    nro1: ''
                },
                resp: {
                    resposta17: "",
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
                        text: 'Exercício 17',
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
                                exercicio: 17,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resp.resposta17 = res.data.resposta
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
