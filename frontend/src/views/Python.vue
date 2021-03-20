<template>
    <div class="container">
        <div>
            <b-card bg-variant="light" text-variant="black">
                <b-form @submit="onSubmit">
                    <p class="text-break">
                        1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
                    </p>
                    <b-button class="mr-1" @click="submit('1')" variant="primary">Executar</b-button>
                    <b-alert class="mt-3" v-if="resposta01" show>{{ resposta01 }}</b-alert>
                </b-form>
            </b-card>
        </div>

        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <b-form @submit="onSubmit">
                    <p class="text-break">
                        2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
                    </p>
                    <b-button class="mr-1" @click="submit('2')" variant="primary">Executar</b-button>
                    <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex2">
                        <b-form-group id="input-exercicio-2" label="Informe um número:" label-for="exercicio-2"
                                      description="O número será enviado para o servidor python e na sequência devolvido em uma sentença abaixo.">
                            <b-form-input id="exercicio-2"
                                          autocomplete="off"
                                          v-model="form.nro"
                                          placeholder="Digite um número"
                                          required
                                          @input="submit(2)"></b-form-input>
                        </b-form-group>
                    </div>
                    <b-alert class="mt-3" v-if="resposta02" show>{{ resposta02 }}</b-alert>
                </b-form>
            </b-card>
        </div>

        <div class="card mt-3 col-md-12">
            <A v-if="true"
               v-show="true"
               :texto="texto2">
            </A>
        </div>

    </div>
</template>

<script>
    import axios from 'axios';
    import A from "@/components/A.vue";
    import B from "@/components/B.vue";

    export default {
        name: 'PythonExercicios',
        components: {
            A,
            B
        },
        data() {
            return {
                texto2: "Oi meu amor",
                post: true,
                form: {
                    nro: '' 
                },
                mostrar_campos_para_entrada_de_dados_ex2: false,
                mostra_resposta: false,
                resposta01: "",
                resposta02: "",
                status: 0
            };
        },
        methods: {
            submit2(nro) {
                alert(nro)
            },
            submit(nro_do_exercicio) {
                if (nro_do_exercicio == '2') {
                    this.post = true
                    this.mostrar_campos_para_entrada_de_dados_ex2 = true

                    if (this.form.nro == '') {
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
                                valor1: this.form.nro
                            }
                        })
                        .then((res) => {
                            if (nro_do_exercicio == '1') {
                                this.resposta01 = res.data.resposta
                            } else {
                                this.resposta02 = res.data.resposta
                            }
                            //this.resposta = res.data.resposta
                            this.status = res.data.status
                            if (this.status = 200) {
                                this.mostra_resposta = true
                            }
                            //alert(this.resposta)
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
