<template>
    <div class="container">
        <div>
            <b-img :src="require('../assets/banner_taxas.png')" fluid alt="Responsive image"></b-img>
        </div>
        <div class="mt-3">
            <b-form @submit="onSubmit" @reset="onReset">
                <div>
                    <b-card bg-variant="light" text-variant="black">
                        <label for="input-valor">Valor da Nota</label>
                        <b-form-input id="input-valor"
                                      v-model="valor_nota"
                                      placeholder="Qual é o valor da nota de corretagem?"
                                      required
                                      :disabled="entrada_de_valor"
                                      autocomplete="off"></b-form-input>
                    </b-card>
                </div>

                <div>
                    <b-card class="mt-3" bg-variant="light" text-variant="black">

                        <label for="input-codigo-da-acao">Ação</label>
                        <b-form-input id="input-codigo-da-acao"
                                      v-model="form.acao"
                                      placeholder="Qual é o código da ação?"
                                      autocomplete="off"
                                      required></b-form-input>

                        <label class="mt-3" for="input-quantidade">Quantidade</label>
                        <b-form-input id="input-quantidade"
                                      v-model="form.quantidade"
                                      placeholder="Quantas ações você comprou ou vendeu?"
                                      autocomplete="off"
                                      required></b-form-input>

                        <label class="mt-3" for="input-preco">Preço unitário</label>
                        <b-form-input id="input-preco"
                                      v-model="form.preco"
                                      placeholder="Qual foi o preço unitário?"
                                      autocomplete="off"
                                      required></b-form-input>

                        <label class="mt-3" for="inline-form-custom-select-tipo">Compra/Venda</label>
                        <b-form-select id="inline-form-custom-select-tipo"
                                       v-model="form.selected_compra_venda"
                                       :options="options"></b-form-select>

                    </b-card>
                </div>
                <b-button class="mt-3 mr-1" type="submit" variant="primary">Adicionar</b-button>
                <b-button class="mt-3" type="reset" variant="danger" 
                          :disabled="valor_nota == '' 
                          && form.acao == ''
                          && form.quantidade == ''
                          && form.preco == ''
                          && form.selected_compra_venda == null
                          ">Limpar</b-button>
            </b-form>

            <div class="mt-3">
                <b-table striped hover :items="items_da_tabela" :fields="fields"></b-table>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'CalculaCorretagem',
        data() {
            return {
                entrada_de_valor: false,
                form: {
                    acao: '',
                    quantidade: '',
                    precoDaCorretagem: 0,
                    valor_sem_formatacao: 0,
                    tipo_de_operacao: '',
                    selected_compra_venda: null,
                    preco: '',
                },
                valor_nota: '',
                showDismissibleAlert: false,
                fields: ['Ação', 'Tipo', 'Quantidade', 'Valor', 'Peso', 'Taxas', 'Total'],
                options: [
                    { value: null, text: 'Escolha...' },
                    { value: 'Compra', text: 'Compra' },
                    { value: 'Venda', text: 'Venda' }
                ],
                items_da_tabela: [],
                tabela_temp: []
            };
        },
        methods: {
            converter(valor) {
                var numero = parseFloat(valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
                return numero
            },
            atualizaItems(tabela_temp_para_atualizacao) {
                var saldo_das_operacoes = 0
                var soma_de_valores = 0
                var soma_das_corretagens = 0
                for (var i = 0; i < tabela_temp_para_atualizacao.length; i++) {
                    saldo_das_operacoes += tabela_temp_para_atualizacao[i].ValorSemFormatacao
                    if (tabela_temp_para_atualizacao[i].ValorSemFormatacao > 0) {
                        soma_de_valores += tabela_temp_para_atualizacao[i].ValorSemFormatacao
                    } else {
                        soma_de_valores = soma_de_valores + (tabela_temp_para_atualizacao[i].ValorSemFormatacao * -1)
                    }
                    soma_das_corretagens += tabela_temp_para_atualizacao[i].Corretagem
                }
                                
                var taxas = this.valor_nota.replace(/,/g, '.') - saldo_das_operacoes - soma_das_corretagens

                for (var i = 0; i < tabela_temp_para_atualizacao.length; i++) {
                    var p = (tabela_temp_para_atualizacao[i].ValorSemFormatacao / soma_de_valores) * 100
                    if (p < 0) {
                        p = p * -1
                    }
                    tabela_temp_para_atualizacao[i].Peso = p.toFixed(2)
                    tabela_temp_para_atualizacao[i].Taxas = (tabela_temp_para_atualizacao[i].Peso * taxas / 100) + tabela_temp_para_atualizacao[i].Corretagem
                    tabela_temp_para_atualizacao[i].Total = tabela_temp_para_atualizacao[i].ValorSemFormatacao + tabela_temp_para_atualizacao[i].Taxas
                }

                // Conversão para o formato R$                    
                for (var i = 0; i < tabela_temp_para_atualizacao.length; i++) {
                    tabela_temp_para_atualizacao[i].Taxas = this.converter(tabela_temp_para_atualizacao[i].Taxas)
                    tabela_temp_para_atualizacao[i].Total = this.converter(tabela_temp_para_atualizacao[i].Total)
                }

                return tabela_temp_para_atualizacao
            },
            onSubmit(event) {
                event.preventDefault()
                this.entrada_de_valor = true
                this.preco_editado = this.form.preco.replace(/,/g, '.')
                let preco_da_compra = this.form.quantidade * this.preco_editado
                if (this.form.selected_compra_venda == 'Compra') {
                    preco_da_compra = preco_da_compra * -1
                }
                    
                this.tabela_temp.push({
                    Ação: this.form.acao,
                    Tipo: this.form.selected_compra_venda,
                    Quantidade: this.form.quantidade,
                    ValorSemFormatacao: preco_da_compra,
                    Valor: this.converter(preco_da_compra),
                    Corretagem: this.form.precoDaCorretagem,
                    Peso: null,
                    Taxas: null,
                    Total: null,
                })
                this.items_da_tabela = this.atualizaItems(this.tabela_temp)
                this.form.acao = ''
                this.form.quantidade = ''
                this.form.preco = ''
                this.form.selected_compra_venda = null
            },
            onReset(event) {
                event.preventDefault()
                this.entrada_de_valor = false
                this.form.acao = ''
                this.form.quantidade = ''
                this.form.preco = ''
                this.form.selected_compra_venda = null
                this.valor_nota = ''
                this.items_da_tabela = []
                this.tabela_temp = []
            }
        },
        created() {
            console.log("created")
        },
    };
</script>
