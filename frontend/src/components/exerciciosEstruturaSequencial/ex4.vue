﻿<template>
    <div class="container">
        <div class="mt-3">
            <Breadcumb :items="itens_breadcumb"></Breadcumb>
            <b-card bg-variant="light" text-variant="black" class="shadow p-3 bg-light rounded">
                <TextoIntrodutorio v-show="true" :texto="texto_ex4"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-4.1" label="Digite a primeira nota:" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Nota do Primeiro Bimestre"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-exercicio-4.2" label="Digite a segunda nota:" label-for="input-2">
                            <b-form-input id="input-2"
                                          autocomplete="off"
                                          v-model="form.nro2"
                                          placeholder="Nota do Segundo Bimestre"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-exercicio-4.3" label="Digite a terceira nota:" label-for="input-3">
                            <b-form-input id="input-3"
                                          autocomplete="off"
                                          v-model="form.nro3"
                                          placeholder="Nota do Terceiro Bimestre"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-exercicio-4.4" label="Digite a quarta nota:" label-for="input-4">
                            <b-form-input id="input-4"
                                          autocomplete="off"
                                          v-model="form.nro4"
                                          placeholder="Nota do Quarto Bimestre"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Média</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == '' && form.nro2 == '' && form.nro3 == '' && form.nro4 == ''">Limpar</b-button>
                    </b-form>
                    <RespostaAlerta :resposta="resp.resposta04" :mostra_resposta="mostra_resposta"></RespostaAlerta>
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
                    texto_ex4: "4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.",
                    post: true,
                    form: {
                        nro1: '',
                        nro2: '',
                        nro3: '',
                        nro4: ''
                    },
                    resp: {
                        resposta04: "",
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
                            text: 'Exercício 4',
                            active: true
                        }
                    ]
                };
            },
            methods: {
                onSubmit(evt) {
                    evt.preventDefault()
                    
                    if (this.form.nro1 != '' && this.form.nro2 != '' && this.form.nro3 != '' && this.form.nro4 != '') {
                        axios.post(
                            valores.path,
                            null,
                            {
                                params: {
                                    exercicio: 4,
                                    valor1: this.form.nro1,
                                    valor2: this.form.nro2,
                                    valor3: this.form.nro3,
                                    valor4: this.form.nro4
                                }
                            })
                            .then((res) => {
                                this.resp.resposta04 = res.data.resposta
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
                onReset(event) {
                    event.preventDefault()
                    this.mostra_resposta = false
                    this.form.nro1 = '',
                    this.form.nro2 = '',
                    this.form.nro3 = '',
                    this.form.nro4 = ''
                }
            },
            created() {

            },
        };

    </script>
