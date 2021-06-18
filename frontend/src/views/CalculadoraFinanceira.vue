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
                        <b-alert :show="dismissCountDown"
                                 dismissible
                                 fade
                                 variant="warning"
                                 @dismiss-count-down="countDownChanged">
                            Data final menor ou igual à data inicial. Corrija por favor!
                        </b-alert>
                    </div>

                    <div v-if="mostra_informacoes_de_datas"> 
                        <p class="quebra_linha">
                            Data final considerada para cálculo financeiro: <strong>{{ form.para_data.data_pretty_print }}</strong>
                         </p>
                        <hr />
                        <p class="quebra_linha">
                            Data final considerada para cálculo D+2: <strong>{{ form.nova_data_d2_feriados.data_pretty_print_d2 }}</strong>
                        </p>
                    </div>


                    <div>
                        <b-button class="mt-3 mr-3" type="reset" variant="danger"
                                  :disabled="form.taxa_mensal == ''
                              && form.valor_do_cheque == ''
                              && form.para_data.dia == ''">Limpar</b-button>
                        <b-button class="mt-3" type="submit" variant="primary">Calcular desconto do cheque</b-button>
                    </div>

                </b-card>
            </b-form>

            <b-card bg-variant="light" text-variant="black" class="mb-3 mt-3">
                <b-form-group label="" v-slot="{ ariaDescribedby }">
                    <b-form-checkbox-group id="checkbox-group-2"
                                           v-model="checkboxes.selected"
                                           :aria-describedby="ariaDescribedby"
                                           name="calc_fin_checkbox"
                                           :options="checkboxes.items_de_checkbox"
                                           switches
                                           @change="action_on_check_change">
                    </b-form-checkbox-group>
                </b-form-group>

                <div v-if="this.checkboxes.selected.includes('exibir_financeiro')">
                    <b-table responsive striped hover fixed :items="items_da_tabela" :fields="fields">
                        <template slot="bottom-row" slot-scope="data" v-if="mostra_valores_totais">
                            <td />
                            <td />
                            <td><strong>Total</strong></td>
                            <td><strong>{{ valores_totais_somados.total_bruto_reais }}</strong></td>
                            <td><strong>{{ total_liquido_usual_reais }}</strong></td>
                            <td><strong>{{ total_liquido_fin_reais }}</strong></td>
                        </template>
                    </b-table>
                </div>
                <div v-else>
                    <b-table responsive striped hover fixed :items="items_da_tabela" :fields="fields">
                        <template slot="bottom-row" slot-scope="data" v-if="mostra_valores_totais">
                            <td />
                            <td />
                            <td><strong>Total</strong></td>
                            <td><strong>{{ valores_totais_somados.total_bruto_reais }}</strong></td>
                            <td><strong>{{ total_liquido_usual_reais }}</strong></td>
                        </template>
                    </b-table>
                </div>

            </b-card>

        </div>
    </div>        
</template>

<script>
    //https://www.npmjs.com/package/vue2-datepicker
    //https://npm.io/package/eh-dia-util
    //https://github.com/lfreneda/eh-dia-util/blob/master/test/index.spec.js
    import DatePicker from 'vue2-datepicker';
    import 'vue2-datepicker/index.css';
    import 'vue2-datepicker/locale/pt-br';
    import { Finance } from 'financejs'

    const ehDiaUtil = require('@lfreneda/eh-dia-util')

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
                        data_pretty_print: ''
                    },

                    nova_data_d2_feriados: {
                        dia_d2: '',
                        nro_de_dias_ate_vencimento_d2: 0,
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
                //mostra_informacoes_das_datas: false,
                //mostra_novo_dia_d2: false,
                mostra_valores_totais: false,
                disable_taxa_mensal: false,
                items_da_tabela: [],
                items_de_entrada_do_formulario: [],               

                mostra_informacoes_de_datas: false,
                dismissSecs: 5,
                dismissCountDown: 0,
            };
        },
        methods: {
            verifica_datas() {
                this.mostra_informacoes_de_datas = false
                                
                if (this.form.data_inicial != null && this.form.para_data.dia != null) {
                    if (this.form.para_data.dia <= this.form.data_inicial) {
                        this.form.para_data.dia = ''
                        
                        this.showAlert()
                    } else {                        
                        this.form.para_data.nro_de_dias_ate_vencimento = this.retorna_nro_de_dias_entre_datas(this.form.data_inicial, this.form.para_data.dia)
                        this.form.para_data.data_pretty_print = this.form.para_data.dia.toLocaleDateString()
                        let d = this.adiciona_dias_na_data(this.form.para_data.dia, 2)                        
                        var temp_dia = d.toISOString().slice(0, 10)                      

                        while (!ehDiaUtil(temp_dia)) {                            
                            d = this.adiciona_dias_na_data(d, 1)                            
                            temp_dia = d.toISOString().slice(0, 10)                            
                        }
                        
                        this.form.nova_data_d2_feriados.dia_d2 = d 
                        this.form.nova_data_d2_feriados.nro_de_dias_ate_vencimento_d2 = this.retorna_nro_de_dias_entre_datas(this.form.data_inicial, this.form.nova_data_d2_feriados.dia_d2)
                        this.form.nova_data_d2_feriados.data_pretty_print_d2 = this.form.nova_data_d2_feriados.dia_d2.toLocaleDateString()
                        this.mostra_informacoes_de_datas = true
                    }
                }                
            },
            adiciona_dias_na_data(data_inicial, nro_de_dias) {
                //console.log('adiciona_dias_na_data() | data_inicial = ' + data_inicial)
                const para_dia = new Date(data_inicial)
                let novo_dia_final = new Date(para_dia)

                novo_dia_final.setDate(para_dia.getDate() + nro_de_dias);
                return novo_dia_final
            },
            retorna_nro_de_dias_entre_datas(inicio, fim) {
                const diffTime = Math.abs(fim - inicio);
                return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            },            
            countDownChanged(dismissCountDown) {
                this.dismissCountDown = dismissCountDown
            },
            showAlert() {
                this.dismissCountDown = this.dismissSecs
            },
            salvar_dados_de_entrada_do_formulario() {
                let dados_de_entrada = {
                    Juros: this.form.taxa_mensal,
                    Valor: this.form.valor_do_cheque,
                    'A partir': this.data_inicial,
                    Para: this.form.para_data.dia,
                    'Nro de dias': this.form.para_data.nro_de_dias_ate_vencimento,
                    'Data pretty_print': this.form.para_data.data_pretty_print,
                }
                this.items_de_entrada_do_formulario.push(dados_de_entrada)
                //console.log("Dados de Entrada: " + dados_de_entrada)
            },
            calcula_pv() {
                let finance = new Finance();
                let valor_bruto = this.form.valor_do_cheque.replace(",", ".")
                let taxa = this.form.taxa_mensal.replace(",", ".").replace(" ", "").replace("%", "")
                let valor_liquido_usual = 0
                let valor_liquido_fin = 0
                var data = this.formatDate(this.form.para_data.dia)

                let nro_de_dias_d2 = this.form.nova_data_d2_feriados.nro_de_dias_ate_vencimento_d2 + 1 //D + 2
                let valor_liquido_usual_d2 = 0
                let valor_liquido_fin_d2 = 0

                valor_liquido_usual = valor_bruto - (((valor_bruto * taxa / 100) / 30) * this.form.para_data.nro_de_dias_ate_vencimento)
                valor_liquido_fin = finance.PV(taxa / 30, valor_bruto, this.form.para_data.nro_de_dias_ate_vencimento)
                valor_liquido_usual_d2 = valor_bruto - (((valor_bruto * taxa / 100) / 30) * nro_de_dias_d2)
                valor_liquido_fin_d2 = finance.PV(taxa / 30, valor_bruto, nro_de_dias_d2)

                this.valores_totais_somados.total_bruto_sem_formatacao_de_reais = this.valores_totais_somados.total_bruto_sem_formatacao_de_reais + parseFloat(valor_bruto)
                this.valores_totais_somados.total_liquido_calculo_usual = this.valores_totais_somados.total_liquido_calculo_usual + valor_liquido_usual
                this.valores_totais_somados.total_liquido_calculo_financeiro = this.valores_totais_somados.total_liquido_calculo_financeiro + valor_liquido_fin
                this.valores_totais_somados.total_liquido_calculo_usual_d2 = this.valores_totais_somados.total_liquido_calculo_usual_d2 + valor_liquido_usual_d2
                this.valores_totais_somados.total_liquido_calculo_financeiro_d2 = this.valores_totais_somados.total_liquido_calculo_financeiro_d2 + valor_liquido_fin_d2

                this.items_da_tabela.push({
                    Para: data,
                    'Nro de dias': this.form.para_data.nro_de_dias_ate_vencimento,
                    'Nro de dias D2': nro_de_dias_d2,

                    Juros: taxa + '%',
                    'Valor Bruto': this.converter(valor_bruto),

                    'Valor Líquido Usual': this.converter(valor_liquido_usual),
                    'Valor Líquido Financeiro': this.converter(valor_liquido_fin),
                    'Valor Líquido Usual D2': this.converter(valor_liquido_usual_d2),
                    'Valor Líquido Financeiro D2': this.converter(valor_liquido_fin_d2),

                    'VLiqUsual_somenteNro': valor_liquido_usual,
                    'VLiqFinanceiro_somenteNro': valor_liquido_fin,
                    'VLiqUsual_somenteNroD2': valor_liquido_usual_d2,
                    'VLiqFinanceiro_somenteNroD2': valor_liquido_fin_d2,

                })
                this.form.valor_do_cheque = ''
                this.form.para_data.dia = ''
                this.form.para_data.nro_de_dias_ate_vencimento = 0
            },
            converter(valor) {
                var numero = parseFloat(valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
                return numero
            },
            formatDate(date) {
                var d = new Date(date),
                    month = '' + (d.getMonth() + 1),
                    day = '' + d.getDate(),
                    year = d.getFullYear();

                if (month.length < 2)
                    month = '0' + month;
                if (day.length < 2)
                    day = '0' + day;

                return [day, month, year].join('-');
            },
            action_on_check_change() {
                //console.log(this.checkboxes.selected)
            },
            onSubmit(event) {
                event.preventDefault()
                this.disable_taxa_mensal = true
                this.salvar_dados_de_entrada_do_formulario()
                this.calcula_pv()
                console.log("items_da_tabela = " + this.items_da_tabela)
                this.mostra_valores_totais = true
                this.valores_totais_somados.total_bruto_reais = this.converter(this.valores_totais_somados.total_bruto_sem_formatacao_de_reais)
            },
            onReset(event) {
                event.preventDefault()
                this.items_de_entrada_do_formulario = []

                this.disable_taxa_mensal = false
                this.mostra_valores_totais = false
                this.form.taxa_mensal = ''
                this.form.valor_do_cheque = ''
                this.form.para_data.dia = ''
                this.form.para_data.nro_de_dias_ate_vencimento = 0
                this.items_da_tabela = []

                this.valores_totais_somados.total_bruto_reais = 0
                this.valores_totais_somados.total_bruto = 0


                this.valores_totais_somados.total_liquido_calculo_usual = 0
                this.valores_totais_somados.total_liquido_calculo_financeiro = 0
                this.valores_totais_somados.total_liquido_calculo_usual_d2 = 0
                this.valores_totais_somados.total_liquido_calculo_financeiro_d2 = 0


                this.form.para_data.dia = ''
                this.form.para_data.nro_de_dias_ate_vencimento = 0
                this.form.para_data.data_pretty_print = ''               

                
                this.form.nova_data_d2_feriados.dia_d2 = ''
                this.form.nova_data_d2_feriados.nro_de_dias_ate_vencimento_d2= 0
                this.form.nova_data_d2_feriados.data_pretty_print_d2 =  ''                
            }
        },
        computed: {
            total_liquido_usual_reais() {
                let total_temp = 0
                for (var i = 0; i < this.items_da_tabela.length; i++) {
                    if (this.checkboxes.selected.includes('d2')) {
                        total_temp = total_temp + this.items_da_tabela[i]['VLiqUsual_somenteNroD2']
                    } else {
                        total_temp = total_temp + this.items_da_tabela[i]['VLiqUsual_somenteNro']
                    }
                }
                return this.converter(total_temp)
            },
            total_liquido_fin_reais() {
                let total_temp = 0
                for (var i = 0; i < this.items_da_tabela.length; i++) {
                    if (this.checkboxes.selected.includes('d2')) {
                        total_temp = total_temp + this.items_da_tabela[i]['VLiqFinanceiro_somenteNroD2']
                    } else {
                        total_temp = total_temp + this.items_da_tabela[i]['VLiqFinanceiro_somenteNro']
                    }
                }
                return this.converter(total_temp)
            },
            fields() {
                if (this.checkboxes.selected.includes('exibir_financeiro') && !this.checkboxes.selected.includes('d2')) {
                    return ['Para', 'Nro de dias', 'Juros', 'Valor Bruto', 'Valor Líquido Usual', 'Valor Líquido Financeiro']
                } else if (!this.checkboxes.selected.includes('exibir_financeiro') && !this.checkboxes.selected.includes('d2')) {
                    return ['Para', 'Nro de dias', 'Juros', 'Valor Bruto', 'Valor Líquido Usual']
                } else if (!this.checkboxes.selected.includes('exibir_financeiro') && this.checkboxes.selected.includes('d2')) {
                    return ['Para', 'Nro de dias D2', 'Juros', 'Valor Bruto', 'Valor Líquido Usual D2']
                } else if (this.checkboxes.selected.includes('exibir_financeiro') && this.checkboxes.selected.includes('d2')) {
                    return ['Para', 'Nro de dias D2', 'Juros', 'Valor Bruto', 'Valor Líquido Usual D2', 'Valor Líquido Financeiro D2']
                }
            },
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

