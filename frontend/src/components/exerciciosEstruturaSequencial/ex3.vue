<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto3"></TextoIntrodutorio>
                <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button>

                <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex3">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-3" label="Digite o primeiro número da soma:" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Número 1"
                                          required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Digite o segundo número da soma:" label-for="input-2"
                                      description="Os números serão enviados para o servidor python e na sequência devolvido o valor da soma.">
                            <b-form-input id="input-2"
                                          autocomplete="off"
                                          v-model="form.nro2"
                                          placeholder="Número 2"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Somar</b-button>
                        <b-button type="reset" variant="danger">Limpar</b-button>
                    </b-form>
                    <b-alert class="mt-3" v-if="mostra_resposta" show>A soma dos dois números é: {{ resposta03 }}</b-alert>
                </div>
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
                    nro1: '',
                    nro2: ''
                },
                mostrar_campos_para_entrada_de_dados_ex3: false,
                mostra_resposta: false,
                resposta03: "",
                status: 0
            };
        },
        methods: {
            submit() {
                    this.mostrar_campos_para_entrada_de_dados_ex3 = true
            },
            onSubmit(event) {
                event.preventDefault()

                //const path = 'http://localhost:5000/resolve_exercicios'
                const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'

                if (this.form.nro1 != '' && this.form.nro2 != '') {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: 3,
                                valor1: this.form.nro1,
                                valor2: this.form.nro2
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
            onReset(event) {
                event.preventDefault()
                this.form.nro1 = '',
                this.form.nro2 = '',
                this.mostra_resposta = false
            }            
        }
    };
</script>
