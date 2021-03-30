<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <b-form @submit="onSubmit" @reset="onReset">

                    <TextoIntrodutorio v-show="true" :texto="texto2"></TextoIntrodutorio>

                    <!-- <b-button class="mr-1" @click="submit('2')" variant="primary">Executar</b-button> -->

                    <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex2">
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
                    </div>
                    <div v-if="mostra_resposta && form.nro2 != ''">
                        <b-alert class="mt-3" show>{{ resposta02 }}</b-alert>
                    </div>
                </b-form>
                </b-card>
            </div>
        </div>
    </template>

    <script>
        import axios from 'axios';
        import TextoIntrodutorio from "@/components/TextoIntrodutorio.vue";

        export default {
            name: 'PythonExercicios',
            components: {
                TextoIntrodutorio
            },
            data() {
                return {
                    texto2: "2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].",
                    post: true,
                    form: {
                        nro2: ''
                    },
                    mostrar_campos_para_entrada_de_dados_ex2: true,
                    mostra_resposta: false,
                    resposta02: "",
                    status: 0
                };
            },
            methods: {
                submit(nro_do_exercicio) {
                    this.mostrar_campos_para_entrada_de_dados_ex2 = true

                    //const path = 'http://localhost:5000/resolve_exercicios'
                    const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'

                    if (this.form.nro2 != '') {
                        axios.post(
                            path,
                            null,
                            {
                                params: {
                                    exercicio: nro_do_exercicio,
                                    valor1: this.form.nro2
                                }
                            })
                            .then((res) => {
                                this.resposta02 = res.data.resposta
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
