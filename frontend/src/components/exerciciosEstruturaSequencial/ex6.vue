<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto6"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex6">
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
                    <b-alert class="mt-3" v-if="mostra_resposta" show>{{ intro_resposta }} {{ resposta06 }} {{ m2 }}</b-alert>
                </div>
            </b-card>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import TextoIntrodutorio from "@/components/Python/modulos/TextoIntrodutorio.vue";

    export default {
        name: 'PythonExercicios',
        components: {
            TextoIntrodutorio
        },
        data() {
            return {
                texto6: "6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.",
                post: true,
                form: {
                    nro1: ''                    
                },
                mostrar_campos_para_entrada_de_dados_ex6: true,
                mostra_resposta: false,
                m2: "",
                resposta06: "",
                intro_resposta: "",
                status: 0
            };
        },
        methods: {
            submit() {
                    this.mostrar_campos_para_entrada_de_dados_ex6 = true
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
                                exercicio: 6,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resposta06 = res.data.resposta
                            this.status = res.data.status
                            if (this.status == 200) {
                                this.intro_resposta = "A área do circulo é: "
                                this.m2 = "m²"
                            } else {
                                this.intro_resposta = "",
                                this.m2 = ""
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
                this.mostra_resposta = false
            }            
        }
    };
</script>
