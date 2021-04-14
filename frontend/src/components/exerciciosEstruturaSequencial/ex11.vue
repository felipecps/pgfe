<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto11"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-11" label="Digite o primeiro número Inteiro" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Z1"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-exercicio-11" label="Digite o segundo número Inteiro" label-for="input-2">
                            <b-form-input id="input-2"
                                          autocomplete="off"
                                          v-model="form.nro2"
                                          placeholder="Z2"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-exercicio-11" label="Digite o número Real" label-for="input-3">
                            <b-form-input id="input-3"
                                          autocomplete="off"
                                          v-model="form.nro3"
                                          placeholder="R"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false && form.nro1 == '' && form.nro2 == '' && form.nro3 == ''">Limpar</b-button>
                    </b-form>
                    <div v-if="resp.status==200">
                        <b-alert class="mt-3" v-if="mostra_resposta" show>
                            <p>
                                Cálculo a) {{ resp.calc1 }}
                            </p>
                            <hr>
                            <p>
                                Cálculo b) {{ resp.calc2 }}
                            </p>
                            <hr>
                            <p>
                                Cálculo c) {{ resp.calc3 }}
                            </p>
                        </b-alert>
                    </div>
                    <div v-else>
                        <RespostaAlerta :resposta="resp.resposta11" :mostra_resposta="mostra_resposta"></RespostaAlerta>
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
                texto11: "Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: a) o produto do dobro do primeiro com metade do segundo. b) a soma do triplo do primeiro com o terceiro. c) o terceiro elevado ao cubo.",
                form: {
                    nro1: '',
                    nro2: '',
                    nro3: ''
                },
                resp: {
                    resposta11: "",
                    calc1: "",
                    calc2: "",
                    calc3: "",
                    status: 0
                },     
                mostra_resposta: false
            };
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                
                 if (this.form.nro1 != '' && this.form.nro2 != '' && this.form.nro3 != '') {
                    axios.post(
                        valores.path,
                        null,
                        {
                            params: {
                                exercicio: 11,
                                valor1: this.form.nro1,
                                valor2: this.form.nro2,
                                valor3: this.form.nro3
                            }
                        })
                        .then((res) => {
                            this.resp.resposta11 = res.data.resposta
                            this.resp.calc1 = res.data.calc1
                            this.resp.calc2 = res.data.calc2
                            this.resp.calc3 = res.data.calc3
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
                this.form.nro3 = '',
                this.mostra_resposta = false
            }            
        }
    };
</script>
