<template>
    <div class="container">
        <b-card bg-variant="light" text-variant="black">
            <FormularioComUmaEntrada v-show="true"
                                        :texto_introdutorio="FCUE_texto_introdutorio"
                                        :texto_do_botao_submit="FCUE_texto_do_botao_submit"
                                        :texto_do_botao_reset="FCUE_texto_do_botao_reset"
                                        :mostrar_campos_para_entrada_de_dados="FCUE_mostrar_campos_para_entrada_de_dados"
                                        :label_do_exercicio="FCUE_label_do_exercicio"
                                        :placeholder="FCUE_placeholder"
                                        :numero_do_exercicio="FCUE_numero_do_exercicio"
                                        >
                                        <!--
                                            @abc="abc_m"
                                            @limpar="limpar"
                                        -->
            </FormularioComUmaEntrada>
        </b-card>
    </div>
</template>

    <script>
        import FormularioComUmaEntrada from "@/components/FormularioComUmaEntrada.vue";
        export default {
            components: {
                FormularioComUmaEntrada
            },
            data() {
                return {
                    FCUE_texto_introdutorio:"6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.",
                    FCUE_texto_do_botao_submit:"Submeter",
                    FCUE_texto_do_botao_reset:"Limpar",
                    FCUE_mostrar_campos_para_entrada_de_dados: true,
                    FCUE_label_do_exercicio: "Informe um número:",
                    FCUE_placeholder: "Digite o raio do círculo em metros:",
                    FCUE_numero_do_exercicio: "6",
                    resposta: '',
                    //path: 'http://localhost:5000/resolve_exercicios',
                    path: 'https://felipecps.pythonanywhere.com/resolve_exercicios'
                };
            },
            methods: {
                /*limpar() {
                    this.mostra_resposta = false
                },
                abc_m(resposta_filho) {
                    this.mostra_resposta = true
                    this.resposta = resposta_filho
                },*/
            },
            created() {

            },
        };
    </script>
