<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto5"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex5">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio-5" label="Digite o valor em metros:" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Valor em Metros"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Converter</b-button>
                        <b-button type="reset" variant="danger" :disabled="mostra_resposta == false || form.nro1 == ''">Limpar</b-button>
                    </b-form>
                    <b-alert class="mt-3" v-if="mostra_resposta" show>{{ intro_resposta }} {{ resposta05 }}</b-alert>
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
                texto5: "5. Faça um Programa que converta metros para centímetros.",
                post: true,
                form: {
                    nro1: ''                    
                },
                mostrar_campos_para_entrada_de_dados_ex5: true,
                mostra_resposta: false,
                resposta05: "",
                intro_resposta: "",
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

                if (this.form.nro1 != '') {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: 5,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resposta05 = res.data.resposta
                            this.status = res.data.status
                            if (this.status == 200) {
                                this.intro_resposta = "O valor informado, convertido para centimetros é: "
                            } else {
                                this.intro_resposta = ""
                            }
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
                this.mostra_resposta = false
            }            
        }
    };
</script>
