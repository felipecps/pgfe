<template>
    <div class="container">
        <div class="mt-3">
            <Breadcumb :items="itens_breadcumb"></Breadcumb>
            <b-card bg-variant="light" text-variant="black" class="shadow p-3 bg-light rounded">
                <TextoIntrodutorio v-show="true" :texto="texto2"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit('2')" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-2" label="Informe um número:" label-for="exercicio-2"
                                      description="O número será enviado para o servidor python e na sequência devolvido em uma sentença abaixo.">
                            <b-form-input id="exercicio-2"
                                          autocomplete="off"
                                          v-model="form.nro2"
                                          placeholder="Digite um número"
                                          required
                                          @input="submit(2)"></b-form-input>
                        </b-form-group>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false || form.nro2 == ''">Limpar</b-button>
                        <RespostaAlerta :resposta="resp.resposta02" :mostra_resposta="mostra_resposta && form.nro2 != ''"></RespostaAlerta>
                    </b-form>
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
                    texto2: "2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].",
                    post: true,
                    form: {
                        nro2: ''
                    },
                    resp: {
                        resposta02: "",
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
                            text: 'Exercício 2',
                            active: true
                        }
                    ]
                };
            },
            methods: {
                submit(nro_do_exercicio) {
                    if (this.form.nro2 != '') {
                        axios.post(
                            valores.path,
                            null,
                            {
                                params: {
                                    exercicio: nro_do_exercicio,
                                    valor1: this.form.nro2
                                }
                            })
                            .then((res) => {
                                this.resp.resposta02 = res.data.resposta
                                this.resp.status = res.data.status
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
                    this.form.nro2 = '',
                    this.mostra_resposta = false
                }
            },
            created() {

            },
        };
    </script>
