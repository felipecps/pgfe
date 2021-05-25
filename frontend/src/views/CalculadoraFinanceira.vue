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
                        <date-picker id="input-data-dp" v-model="hoje" valueType="date"></date-picker>
                    </b-form-group>

                    <b-form-group id="input-data-fg" label="Qual é a data do cheque?" label-for="input-data-dp">
                        <date-picker id="input-data-dp" @change="days_between" v-model="form.para_dia" class="animated-placeholder" valueType="date"></date-picker>
                    </b-form-group>

                    <p>
                        Número de dias até o vencimento: {{ form.nro_de_dias_ate_vencimento }}
                    </p>


                    <b-button class="mt-3" type="reset" variant="danger"
                              :disabled="form.taxa_mensal == ''
                              && form.valor_do_cheque == ''
                              && form.para_dia == ''">Limpar</b-button>
                    <b-button class="mt-3 ml-3" type="submit" variant="primary">Calcular desconto do cheque</b-button>
                </b-card>

                
            </b-form>

            <div class="mt-3">
                <b-table striped hover :items="items_da_tabela" :fields="fields">
                    <template slot="bottom-row" slot-scope="data" v-if="mostra_total">
                        <td />
                        <td />
                        <td><strong>Total</strong></td>
                        <td><strong>{{ total_bruto_reais }}</strong></td>
                        <td><strong>{{ total_liquido_reais }}</strong></td>
                    </template>
                </b-table>
                
            </div>
        </div>
    </div>        
</template>

<script>
    //https://www.npmjs.com/package/vue2-datepicker
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
                    para_dia: '',
                    nro_de_dias_ate_vencimento: 0
                },
                total_bruto_reais: 0,
                total_liquido_reais: 0,
                total_bruto: 0,
                total_liquido: 0,
                mostra_total: false,
                disable_taxa_mensal: false,
                items_da_tabela: [],
                fields: ['Para', 'Nro de dias', 'Juros', 'Valor Bruto', 'Valor Liquido'],
                diff: 0,
                hoje: new Date(),
            };
        },
        
        methods: {
            converter(valor) {
                var numero = parseFloat(valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
                return numero
            },
            days_between() {
                console.log("days_between")
                const diffTime = Math.abs(this.form.para_dia - this.hoje);
                const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
                console.log(diffTime + " milliseconds");
                console.log(diffDays + " days");
                this.form.nro_de_dias_ate_vencimento = diffDays
            },
            calcula_pv() {
                let finance = new Finance();
                let valor_bruto = this.form.valor_do_cheque.replace(",", ".")
                let taxa = this.form.taxa_mensal.replace(",", ".").replace(" ", "").replace("%", "")
                let valor_liquido = finance.PV(taxa / 30, valor_bruto, this.form.nro_de_dias_ate_vencimento)
                console.log(valor_liquido)
                var data = this.formatDate(this.form.para_dia)
                this.total_bruto = this.total_bruto + parseFloat(valor_bruto)
                this.total_liquido = this.total_liquido + valor_liquido

                this.items_da_tabela.push({
                    Para: data,
                    'Nro de dias': this.form.nro_de_dias_ate_vencimento,
                    Juros: taxa + '%',
                    'Valor Bruto': this.converter(valor_bruto),
                    'Valor Liquido': this.converter(valor_liquido)
                })
                this.form.valor_do_cheque = ''
                this.form.para_dia = ''
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
            onSubmit(event) {
                event.preventDefault()
                //let finance = new Finance();
                //console.log(finance.PV(5, 100, 5))
                this.disable_taxa_mensal = true
                this.calcula_pv()
                this.mostra_total = true
                this.total_bruto_reais = this.converter(this.total_bruto)
                this.total_liquido_reais = this.converter(this.total_liquido)
            },
            onReset(event) {
                event.preventDefault()
                this.disable_taxa_mensal = false
                this.mostra_total = false
                this.form.taxa_mensal = ''
                this.form.valor_do_cheque = ''
                this.form.para_dia = ''
                this.form.nro_de_dias_ate_vencimento = 0
                this.items_da_tabela = []
                this.total_liquido_reais = 0
                this.total_bruto_reais = 0
                this.total_bruto = 0
                this.total_liquido = 0
            }
        }
    }; 
</script>


