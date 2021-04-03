<template>
    <div class="container">
        <div class="mt-3">
            <b-card bg-variant="light" text-variant="black">
                <FormularioComUmaEntrada v-show="true"
                                         :texto_introdutorio="FCUE_texto_introdutorio"
                                         :texto_do_botao_submit="FCUE_texto_do_botao_submit"
                                         :texto_do_botao_reset="FCUE_texto_do_botao_reset"
                                         :mostrar_campos_para_entrada_de_dados="FCUE_mostrar_campos_para_entrada_de_dados"
                                         :mostra_resposta="FCUE_mostra_resposta "
                                         :label_do_exercicio="FCUE_label_do_exercicio"
                                         :placeholder="FCUE_placeholder"
                                         >
                </FormularioComUmaEntrada>
                </b-card>
            </div>
        </div>
    </template>

    <script>
        import axios from 'axios';
        import FormularioComUmaEntrada from "@/components/FormularioComUmaEntrada.vue";

        export default {
            components: {
                FormularioComUmaEntrada
            },
            data() {
                return {
                    FCUE_texto_introdutorio:"2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].",
                    FCUE_texto_do_botao_submit:"Submeter",
                    FCUE_texto_do_botao_reset:"Limpar",
                    FCUE_mostrar_campos_para_entrada_de_dados: true,
                    FCUE_mostra_resposta: false,
                    FCUE_label_do_exercicio: "Informe um número:",
                    FCUE_placeholder: "Digite um número"
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
