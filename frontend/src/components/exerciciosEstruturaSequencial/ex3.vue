<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <b-form @submit="onSubmit">

                    <TextoIntrodutorio v-show="true"
                                       :texto="texto3">
                    </TextoIntrodutorio>

                    <b-button class="mr-1" @click="submit('3')" variant="primary">Executar</b-button>
                    <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex3">
                        <b-form-group id="input-exercicio-3" label="Digite o primeiro número:" label-for="exercicio-3"
                                      description="O número será enviado para o servidor python e na sequência devolvido em uma sentença abaixo.">
                            <b-form-input id="exercicio-3"
                                          autocomplete="off"
                                          v-model="form.nro3"
                                          placeholder="Número 1"
                                          required
                                          @input="submit(3)"></b-form-input>
                        </b-form-group>
                    </div>
                    <b-alert class="mt-3" v-if="resposta03" show>{{ resposta03 }}</b-alert>
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
                texto3: "3. Faça um Programa que peça dois números e imprima a soma.",
                post: true,
                form: {
                    nro3: ''
                },
                mostrar_campos_para_entrada_de_dados_ex3: false,
                mostra_resposta: false,
                 resposta03: "",
                status: 0
            };
        },
        methods: {
            submit(nro_do_exercicio) {
                if (nro_do_exercicio == '3') {
                    this.post = true
                    this.mostrar_campos_para_entrada_de_dados_ex3 = true

                    if (this.form.nro3 == '') {
                        this.post = false
                    }
                }
                //const path = 'http://localhost:5000/resolve_exercicios'
                const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'
                if (this.post) {
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
                            this.resposta03 = res.data.resposta
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

            }
        },
        created() {

        },
    };
</script>
