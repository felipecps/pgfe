<template>
    <div class="container">
        <div>
            <b-img :src="require('../assets/banner_calculadora.png')" fluid alt="Responsive image"></b-img>
        </div>
        <div class="mt-3">
            <h5>
                Preencha os campos abaixo e calcule o desconto de cada valor futuro.
            </h5>
        </div>
        <div class="mt-3">
            <b-form @submit="onSubmit" @reset="onReset">
                <b-card bg-variant="light" text-variant="black">


                    <b-form-group id="input-taxa-fg" label="Qual é a taxa mensal?" label-for="input-taxa-fi">
                        <b-form-input id="input-taxa-fi"
                                      autocomplete="off"
                                      v-model="form.taxa_mensal"
                                      :disabled="disable_taxa_mensal"
                                      placeholder="% a.m."
                                      required></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-valor-fg" label="Qual o valor do cheque?" label-for="input-valor-fi">
                        <b-form-input id="input-valor-fi"
                                      autocomplete="off"
                                      v-model="form.valor_do_cheque"
                                      placeholder="R$"
                                      required></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-data-fg" label="A partir de quando?" label-for="input-data-dp">
                        <date-picker format="DD-MM-YYYY" id="input-data-dp" @change="verifica_datas" v-model="form.data_inicial" valueType="date"></date-picker>
                    </b-form-group>

                    <b-form-group id="input-data-fg" label="Qual é a data do cheque?" label-for="input-data-dp">
                        <date-picker format="DD-MM-YYYY" id="input-data-dp" @change="verifica_datas" v-model="form.para_data.dia" class="animated-placeholder" valueType="date"></date-picker>
                    </b-form-group>

                    
                    
                    <div>
                        <b-button class="mt-3 mr-3" type="reset" variant="danger"
                                  :disabled="form.taxa_mensal == ''
                              && form.valor_do_cheque == ''
                              && form.para_data.dia == ''">Limpar</b-button>
                        <b-button class="mt-3" type="submit" variant="primary">Calcular desconto do cheque</b-button>
                    </div>

                </b-card>
            </b-form>            
        </div>
    </div>        
</template>

<script>
    //https://www.npmjs.com/package/vue2-datepicker
    //https://www.npmjs.com/package/date-holidays
    import DatePicker from 'vue2-datepicker';
    import 'vue2-datepicker/index.css';
    import 'vue2-datepicker/locale/pt-br';
    import { Finance } from 'financejs'

    export default {
        components: { DatePicker },
        data() {
            return {
                form: {
                    taxa_mensal: '',
                    valor_do_cheque: '',
                    //hoje --> data_inicial: new Date(),
                    data_inicial: new Date(),

                    para_data: {
                        dia: '',
                        nro_de_dias_ate_vencimento: 0,
                        dia_da_semana: '',
                        data_pretty_print: ''
                    },

                    nova_data_d2_feriados: {
                        dia_d2: '',
                        nro_de_dias_ate_vencimentod_2: 0,
                        dia_da_semana_d2: '',
                        data_pretty_print_d2: ''
                    }
                },

                checkboxes: {
                    selected: ['exibir_financeiro'],
                    items_de_checkbox: [
                        { text: 'Exibir valor líquido financeiro', value: 'exibir_financeiro' },
                        { text: 'D+2', value: 'd2' }
                    ],
                },

                valores_totais_somados: {
                    total_bruto_sem_formatacao_de_reais: 0,
                    total_bruto_reais: 0,

                    total_liquido_calculo_usual: 0,
                    total_liquido_calculo_financeiro: 0,

                    total_liquido_calculo_usual_d2: 0,
                    total_liquido_calculo_financeiro_d2: 0,
                },

                nova_linha: '\n',
                mostra_informacoes_das_datas: false,
                mostra_novo_dia_d2: false,
                mostra_valores_totais: false,
                disable_taxa_mensal: false,
                items_da_tabela: [],
                items_de_entrada_do_formulario: [],
                dias_da_semana: ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'],
            };
        },
        methods: {
            verifica_datas() {
                console.log("form.data_inicial: " + this.form.data_inicial)
                console.log("form.para_data.dia: " + this.form.para_data.dia)
            },
            onSubmit(event) {
                event.preventDefault()
            },
            onReset(event) {
                event.preventDefault()
            }
        },
        computed: {
            
        },
        watch: {
            
        }
    }; 
</script>

<style>
    p.quebra_linha {
        white-space: pre-line;
    }
</style >

