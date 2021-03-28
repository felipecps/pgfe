<template>
    <div class="container">
        <div>
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto_ex4"></TextoIntrodutorio>
                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->

                        <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex4">
                            <b-form @submit="onSubmit" @reset="onReset">
                                <b-form-group id="input-exercicio-4.1" label="Digite a primeira nota:" label-for="input-1">
                                    <b-form-input id="input-1"
                                                  autocomplete="off"
                                                  v-model="form.nro1"
                                                  placeholder="Nota do Primeiro Bimestre"
                                                  required></b-form-input>
                                </b-form-group>

                                <b-form-group id="input-exercicio-4.2" label="Digite a segunda nota:" label-for="input-1">
                                    <b-form-input id="input-2"
                                                  autocomplete="off"
                                                  v-model="form.nro2"
                                                  placeholder="Nota do Segundo Bimestre"
                                                  required></b-form-input>
                                </b-form-group>

                                <b-form-group id="input-exercicio-4.3" label="Digite a terceira nota:" label-for="input-1">
                                    <b-form-input id="input-1"
                                                  autocomplete="off"
                                                  v-model="form.nro3"
                                                  placeholder="Nota do Terceiro Bimestre"
                                                  required></b-form-input>
                                </b-form-group>

                                <b-form-group id="input-exercicio-4.4" label="Digite a quarta nota:" label-for="input-1">
                                    <b-form-input id="input-1"
                                                  autocomplete="off"
                                                  v-model="form.nro4"
                                                  placeholder="Nota do Quarto Bimestre"
                                                  required></b-form-input>
                                </b-form-group>


                                <b-button class="mr-1" type="submit" variant="primary">Média</b-button>
                                <b-button type="reset" variant="danger" :disabled="mostra_resposta == false">Limpar</b-button>
                            </b-form>
                            <b-alert class="mt-3" v-if="mostra_resposta" show>A média das notas dos 4 bimestres é: {{ resposta04 }}</b-alert>
                        </div>
                </b-card>
            </div>
        </div>
    </template>

    <script>
        import axios from 'axios';
        import TextoIntrodutorio from "@/components/TextoIntrodutorio.vue";

        export default {
            components: {
                TextoIntrodutorio
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
                    mostrar_campos_para_entrada_de_dados_ex4: true,
                    mostra_resposta: false,
                    resposta04: "",
                    status: 0
                };
            },
            methods: {
                submit() {
                    this.mostrar_campos_para_entrada_de_dados_ex4 = true
                },
                onSubmit(evt) {
                    evt.preventDefault()

                    //const path = 'http://localhost:5000/resolve_exercicios'
                    const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'

                    if (this.form.nro1 != '' && this.form.nro2 != '' && this.form.nro3 != '' && this.form.nro4 != '') {
                        axios.post(
                            path,
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
                                this.resposta04 = res.data.resposta
                                this.status = res.data.status
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
