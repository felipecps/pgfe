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
                        <date-picker format="DD-MM-YYYY" id="input-data-dp" v-model="hoje" valueType="date"></date-picker>
                    </b-form-group>

                    <b-form-group id="input-data-fg" label="Qual é a data do cheque?" label-for="input-data-dp">
                        <date-picker format="DD-MM-YYYY" id="input-data-dp" @change="days_between" v-model="form.para.dia" class="animated-placeholder" valueType="date"></date-picker>
                    </b-form-group>
                    
                    <div>
                        <p>
                            Número de dias até o vencimento: {{ form.para.nro_de_dias_ate_vencimento }}.
                            Vencimento em um(a) {{ form.para.dia_da_semana }}
                        </p>
                        <p v-if="mostra_novo_dia_d2">
                            <strong>{{ this.form.para.nova_data_d2_feriados.novo_dia_da_semana }}</strong>
                        </p>
                    </div>
                    

                    <div>
                        <b-button class="mt-3 mr-3" type="reset" variant="danger"
                                  :disabled="form.taxa_mensal == ''
                              && form.valor_do_cheque == ''
                              && form.para.dia == ''">Limpar</b-button>
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
                    para: {
                        dia: '',
                        nro_de_dias_ate_vencimento: 0,
                        dia_da_semana: '',
                        nova_data_d2_feriados: {
                            novo_dia: '',
                            novo_nro_de_dias_ate_vencimento: 0,
                            novo_dia_da_semana: '',
                        }
                    },
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

                mostra_novo_dia_d2: false,
                mostra_valores_totais: false,
                disable_taxa_mensal: false,
                items_da_tabela: [],
                items_de_entrada_do_formulario: [],
                dias_da_semana: ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'],
                hoje: new Date(),
            };
        },
        methods: {
            action_on_check_change() {
                //console.log(this.checkboxes.selected)
            },
            converter(valor) {
                var numero = parseFloat(valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
                return numero
            },
            adiciona_dias_na_data(data_inicial, nro_de_dias) {
                const para_dia = new Date(data_inicial)
                const novo_dia_final = new Date(para_dia)

                novo_dia_final.setDate(para_dia.getDate() + nro_de_dias);
                return novo_dia_final
            },
            calcula_diff_dias(inicio, fim) {
                const diffTime = Math.abs(fim - inicio);
                return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            },
            retorna_dia_da_semana(dia) {
                return this.dias_da_semana[dia.getDay()];
            },
            days_between() {
                this.mostra_novo_dia_d2 = false
                if (this.form.para.dia == null) {
                    this.form.para.nro_de_dias_ate_vencimento = 0
                } else {
                    this.form.para.nro_de_dias_ate_vencimento = this.calcula_diff_dias(this.form.para.dia, this.hoje)
                    this.form.para.dia_da_semana = this.retorna_dia_da_semana(this.form.para.dia)

                    /*console.log("Dia de vencimento: " + this.form.para.dia)
                    console.log("Nro de dias até o vencimento: " + this.form.para.nro_de_dias_ate_vencimento)
                    console.log("Dia da semana até vencimento: " + this.form.para.dia_da_semana)*/

                    if ((this.form.para.dia_da_semana == this.dias_da_semana[0]) || (this.form.para.dia_da_semana == this.dias_da_semana[6])) {
                        if (this.form.para.dia_da_semana == this.dias_da_semana[0]) {
                            this.form.para.nova_data_d2_feriados.novo_dia = this.adiciona_dias_na_data(this.form.para.dia, 1)
                        } else if (this.form.para.dia_da_semana == this.dias_da_semana[6]) {
                            this.form.para.nova_data_d2_feriados.novo_dia = this.adiciona_dias_na_data(this.form.para.dia, 2)
                        }
                        this.form.para.nova_data_d2_feriados.novo_nro_de_dias_ate_vencimento = this.calcula_diff_dias(this.form.para.nova_data_d2_feriados.novo_dia, this.hoje)
                        this.form.para.nova_data_d2_feriados.novo_dia_da_semana = this.retorna_dia_da_semana(this.form.para.nova_data_d2_feriados.novo_dia)
                        /*console.log("Novo dia de vencimento: " + this.form.para.nova_data_d2_feriados.novo_dia)
                        console.log("Novo nro de dias até o vencimento: " + this.form.para.nova_data_d2_feriados.novo_nro_de_dias_ate_vencimento)
                        console.log("Novo dia da semana até vencimento: " + this.form.para.nova_data_d2_feriados.novo_dia_da_semana)*/
                        this.mostra_novo_dia_d2 = true
                    }
                }
            },
            calcula_pv() {
                console.log("this.form.para.nro_de_dias_ate_vencimento = " + this.form.para.nro_de_dias_ate_vencimento)
                let finance = new Finance();
                let valor_bruto = this.form.valor_do_cheque.replace(",", ".")
                let taxa = this.form.taxa_mensal.replace(",", ".").replace(" ", "").replace("%", "")
                let valor_liquido_usual = 0
                let valor_liquido_fin = 0
                var data = this.formatDate(this.form.para.dia)

                //let nro_de_dias_d2 = this.form.para.nro_de_dias_ate_vencimento + 3
                let nro_de_dias_d2 = this.form.para.nova_data_d2_feriados.novo_nro_de_dias_ate_vencimento + 3
                console.log("calcula_pv | nro_de_dias_d2: " + nro_de_dias_d2)
                //console.log("calcula_pv | this.form.para.nova_data_d2_feriados.novo_nro_de_dias_ate_vencimento: " + this.form.para.nova_data_d2_feriados.novo_nro_de_dias_ate_vencimento)
                let valor_liquido_usual_d2 = 0
                let valor_liquido_fin_d2 = 0
                
                valor_liquido_usual = valor_bruto - (((valor_bruto * taxa / 100) / 30) * this.form.para.nro_de_dias_ate_vencimento)
                valor_liquido_fin = finance.PV(taxa / 30, valor_bruto, this.form.para.nro_de_dias_ate_vencimento)
                valor_liquido_usual_d2 = valor_bruto - (((valor_bruto * taxa / 100) / 30) * nro_de_dias_d2)
                valor_liquido_fin_d2 = finance.PV(taxa / 30, valor_bruto, nro_de_dias_d2)
                
                this.valores_totais_somados.total_bruto_sem_formatacao_de_reais = this.valores_totais_somados.total_bruto_sem_formatacao_de_reais + parseFloat(valor_bruto)
                this.valores_totais_somados.total_liquido_calculo_usual = this.valores_totais_somados.total_liquido_calculo_usual + valor_liquido_usual
                this.valores_totais_somados.total_liquido_calculo_financeiro = this.valores_totais_somados.total_liquido_calculo_financeiro + valor_liquido_fin
                this.valores_totais_somados.total_liquido_calculo_usual_d2 = this.valores_totais_somados.total_liquido_calculo_usual_d2 + valor_liquido_usual_d2
                this.valores_totais_somados.total_liquido_calculo_financeiro_d2 = this.valores_totais_somados.total_liquido_calculo_financeiro_d2 + valor_liquido_fin_d2


                this.items_da_tabela.push({
                    Para: data,
                    'Nro de dias': this.form.para.nro_de_dias_ate_vencimento,
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
                this.form.para.dia = ''
                this.form.para.nro_de_dias_ate_vencimento = 0
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
            salvar_dados_de_entrada_do_formulario() {
                let dados_de_entrada = {
                    Juros: this.form.taxa_mensal,
                    Valor: this.form.valor_do_cheque,
                    'A partir': this.hoje,
                    Para: this.form.para.dia,
                    'Nro de dias': this.form.para.nro_de_dias_ate_vencimento
                }
                this.items_de_entrada_do_formulario.push(dados_de_entrada)
                //console.log("Dados de Entrada: " + dados_de_entrada)
            },
            onSubmit(event) {
                event.preventDefault()
                //let finance = new Finance();
                //console.log(finance.PV(5, 100, 5))
                this.salvar_dados_de_entrada_do_formulario()
                this.disable_taxa_mensal = true               
                this.calcula_pv()             
                this.mostra_valores_totais = true
                this.valores_totais_somados.total_bruto_reais = this.converter(this.valores_totais_somados.total_bruto_sem_formatacao_de_reais)
            },            
            onReset(event) {
                event.preventDefault()
                this.disable_taxa_mensal = false
                this.mostra_valores_totais = false
                this.form.taxa_mensal = ''
                this.form.valor_do_cheque = ''
                this.form.para.dia = ''
                this.form.para.nro_de_dias_ate_vencimento = 0
                this.items_da_tabela = []
                
                this.valores_totais_somados.total_bruto_reais = 0
                this.valores_totais_somados.total_bruto = 0
                

                this.valores_totais_somados.total_liquido_calculo_usual = 0
                this.valores_totais_somados.total_liquido_calculo_financeiro = 0
                this.valores_totais_somados.total_liquido_calculo_usual_d2 = 0
                this.valores_totais_somados.total_liquido_calculo_financeiro_d2 = 0
            }
        },
        computed: {
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
            }
        },
        watch: {
            items_de_entrada_do_formulario() {
                console.log("watch: items_de_entrada_do_formulario: " + this.items_de_entrada_do_formulario.length)
            }
        }
    }; 
</script>


