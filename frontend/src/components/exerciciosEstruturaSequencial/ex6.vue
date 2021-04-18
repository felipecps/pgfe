<template>
    <div class="container">
        <div class="mt-3">
            <Breadcumb :items="itens_breadcumb"></Breadcumb>
            <b-card bg-variant="light" text-variant="black" class="shadow p-3 bg-light rounded">
                <TextoIntrodutorio v-show="true" :texto="texto6"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-6" label="Digite o raio do círculo em metros:" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Valor em Metros"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular área do círculo</b-button>
                        <b-button type="reset" variant="danger" :disabled="(mostra_resposta == false && form.nro1 == '')">Limpar</b-button>
                    </b-form>
                    <RespostaAlerta :resposta="resp.resposta06" :mostra_resposta="mostra_resposta"></RespostaAlerta>
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
                texto6: "6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.",
                post: true,
                form: {
                    nro1: ''                    
                },
                resp: {
                    resposta06: "",
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
                        text: 'Exercício 6',
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
                                exercicio: 6,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resp.resposta06 = res.data.resposta
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
