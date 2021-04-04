<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <TextoIntrodutorio v-show="true" :texto="texto7"></TextoIntrodutorio>

                <!-- <b-button class="mr-1" @click="submit()" variant="primary">Executar</b-button> -->
                <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex7">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-exercicio7" label="Digite o tamanho do lado do quadrado em metros:" label-for="input-1">
                            <b-form-input id="input-1"
                                          autocomplete="off"
                                          v-model="form.nro1"
                                          placeholder="Lado em Metros"
                                          required></b-form-input>
                        </b-form-group>

                        <b-button class="mr-1" type="submit" variant="primary">Calcular área do Quadrado</b-button>
                        <b-button type="reset" variant="danger" :disabled="(mostra_resposta == false && form.nro1 == '')">Limpar</b-button>
                    </b-form>
                    <b-alert class="mt-3" v-if="mostra_resposta" show>{{ resp.resposta07 }}</b-alert>
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
                texto7: "7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.",
                mostrar_campos_para_entrada_de_dados_ex7: true,
                resp: {
                    resposta07: "",
                    status: 0
                },                
                form: {
                    nro1: ''                    
                },
                mostra_resposta: false,
            };
        },
        methods: {
            onSubmit(event) {
                event.preventDefault()
                const path = 'http://localhost:5000/resolve_exercicios'
                //const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'

                if (this.form.nro1 != '') {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: 7,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resp.resposta07 = res.data.resposta
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
